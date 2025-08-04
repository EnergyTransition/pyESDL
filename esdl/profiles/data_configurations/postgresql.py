from typing import Any

import psycopg

from esdl import esdl
from esdl.profiles.data_configurations.credentials import Credentials


class PostgresqlConfiguration():
    connection: Any
    datatable_profile: esdl.DataTableProfile

    def __init__(self, datatable_profile: esdl.DataTableProfile, credentials_dict: dict[str, Credentials]):
        self.datatable_profile = datatable_profile
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
                    raise InvalidCredentials(f"DataConfiguration {configuration.id} is has no associated credentials"
                                               f"to use for connecting to the Postgres database")

            print(f'Connecting to Postgres database at {credential.username}@{configuration.host}:'
                  f'{configuration.port or 5432}/{configuration.database}')
            self.connection = psycopg.connect(user=credential.username,
                                               password=credential.password,
                                               host=configuration.host,
                                               port=configuration.port or 5432,
                                               dbname=configuration.database,
                                               )
        except Exception as error:
            print("Error while connecting to PostgreSQL", error)
        return self.connection

    def connection(self):
        return self.connection


    def disconnect(self):
        if self.connection:
            self.connection.close()

    def load_data(self):
        with self.connection.cursor() as cursor:
            if self.datatable_profile.schema:
                table = self.datatable_profile.schema + "." + self.datatable_profile.tableName
            else:
                table = self.datatable_profile.tableName

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


class InvalidCredentials(Exception):
    pass