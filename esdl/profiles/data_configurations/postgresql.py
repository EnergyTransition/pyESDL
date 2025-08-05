from typing import Any, Optional, List

import psycopg
from psycopg import Connection, sql

from esdl import esdl
from esdl.profiles.data_configurations.credentials import Credentials


class PostgresqlConfiguration:
    connection: Optional[Connection]
    datatable_profile: esdl.DataTableProfile

    def __init__(self, datatable_profile: esdl.DataTableProfile, credentials_dict: dict[str, Credentials]):
        self.datatable_profile = datatable_profile
        self.connection: Optional[Connection] = None
        self.credentials_dict = credentials_dict
        self._connect_postgres(datatable_profile, credentials_dict)


    def _connect_postgres(self, datatable_profile: esdl.DataTableProfile, credentials_dict: dict[str, Credentials]):
        try:
            configuration = datatable_profile.configuration
            # try on id of configuration
            credential = credentials_dict.get(configuration.id, None)
            if credential is None:
                # try on host name
                credential = credentials_dict.get(configuration.host, None)
                if credential is None:
                    raise InvalidCredentials(f"DataConfiguration '{configuration.id}' is has no associated credentials"
                                               f" to use for connecting to the Postgres database")

            print(f'Connecting to Postgres database at {credential.username}@{configuration.host}:'
                  f'{configuration.port or 5432}/{configuration.database}')
            self.connection = psycopg.connect(user=credential.username,
                                               password=credential.password,
                                               host=configuration.host,
                                               port=configuration.port or 5432,
                                               dbname=configuration.database,
                                               )
        except Exception as e:
            print("Error while connecting to PostgreSQL: ", e)
            if self.connection and not self.connection.closed:
                self.connection.close()
                raise e
        return self.connection

    def get_connection(self):
        return self.connection


    def disconnect(self):
        if self.connection:
            self.connection.close()

    def load_data(self):
        if not self.connection:
            raise Exception('PostgreSQL connection not established')
        with self.connection.cursor() as cursor:
            if self.datatable_profile.schema:
                table = self.datatable_profile.schema + "." + self.datatable_profile.tableName
            else:
                table = self.datatable_profile.tableName

            # warning: this is unquoted SQL...
            if self.datatable_profile.filter:
                where = "WHERE self.datatable_profile.filter"
            else:
                where = ""

            cursor.execute(f'SELECT '
                           f'{self.datatable_profile.datetimeColumnName},{self.datatable_profile.columnName} '
                           f'FROM {table} {where};')
            result = cursor.fetchall()
            # process results
            header = [self.datatable_profile.datetimeColumnName, self.datatable_profile.columnName]
            profile_values = []
            for row in result:
                profile_values.append([row[0], row[1]])
            return profile_values, header


    def save_data(self, profile_values: List[List[Any]], header: List[str]):
        """
        Saves data to Postgres. It will insert all the columns in the profile_values by default.
        :param profile_values:
        :param header:
        :return:
        """
        if not self.connection:
            raise Exception('PostgreSQL connection not established')

        if self.datatable_profile.schema:
            table = sql.Identifier(self.datatable_profile.schema, self.datatable_profile.tableName)
        else:
            table = sql.Identifier(self.datatable_profile.tableName)

        # COMMENT ON COLUMN essim_run_20250804.csv_data_table.column2 IS 'unit=PJ';

        with self.connection.cursor() as cursor:
            non_datetime_columns = list(header)
            non_datetime_columns.remove(self.datatable_profile.datetimeColumnName)
            insert_columns = [f"{c} DOUBLE PRECISION" for c in non_datetime_columns]
            insert_columns.insert(0, f"{self.datatable_profile.datetimeColumnName} TIMESTAMP")
            insert_column_statement = ",\n".join(insert_columns)
            # create schema and table if not exists
            if self.datatable_profile.schema:
                query = sql.SQL('CREATE SCHEMA IF NOT EXISTS {schema}').format(schema=sql.Identifier(self.datatable_profile.schema))
                print(query.as_string(cursor))
                cursor.execute(query)
            sql_string = f"CREATE TABLE IF NOT EXISTS " + "{table}" + f" ({insert_column_statement})"
            query = sql.SQL(sql_string).format(table=table)
            #print(query.as_string(cursor))
            cursor.execute(query)

            columns = sql.SQL(', ').join(sql.Identifier(h) for h in header)
            query = sql.SQL("COPY {table} ({columns}) FROM STDIN").format(table=table, columns=columns)
            #print("Insert query: ", query.as_string(cursor))
            with cursor.copy(query) as copy:
                for row in profile_values:
                    copy.write_row(row)


            # Set extra information in tableName_metadata table (in same schema)
            # such as Unit, Quantity, multiplier, and name of profile (and id?)



            self.connection.commit()



class InvalidCredentials(Exception):
    pass