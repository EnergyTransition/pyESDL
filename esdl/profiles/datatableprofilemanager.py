#  This work is based on original code developed and copyrighted by TNO 2023.
#  Subsequent contributions are licensed to you by the developers of such code and are
#  made available to the Project under one or several contributor license agreements.
#
#  This work is licensed to you under the Apache License, Version 2.0.
#  You may obtain a copy of the license at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Contributors:
#      TNO         - Initial implementation
#  Manager:
#      TNO
from dataclasses import dataclass
from datetime import datetime
from typing import TypedDict, Dict
from uuid import uuid4

import psycopg2
import pytz
from pyecore.ecore import EDate

import esdl
from esdl import DatabaseConfiguration
from esdl.profiles.data_configurations.credentials import Credentials
from esdl.profiles.data_configurations.postgresql import PostgresqlConfiguration
from esdl.profiles.excelprofilemanager import ExcelProfileManager
from esdl.profiles.profilemanager import ProfileManager, UnknownProfileNameException, ProfileType
from influxdb import InfluxDBClient

from esdl.utils.datetime_utils import parse_date



class DataTableProfileManager(ProfileManager):
    """
    InfluxDBProfileManager: manages profile data that can be loaded from and saved to InfluxDB (v1 only).
    InfluxDBProfileManager is a subclass of ProfileManager, so it also provides functionality to convert from/to
    different ESDL profiles and to load/save to CSV
    """
    data_table_profile: esdl.DataTableProfile

    def __init__(self, data_table_profile: esdl.DataTableProfile = None, source_profile=None):
        """
        Constructor of the InfluxDBProfileManager

        :param data_table_profile: the DataTableProfile to load
        :param source_profile: the source profile of which the data is copied into this profiles manager instance
        """
        super().__init__()
        self.profile_type = ProfileType.DATETIME_LIST
        self.connection = None

        if data_table_profile:
            self.data_table_profile = data_table_profile
        else:
            self.data_table_profile = esdl.DataTableProfile()

        if source_profile:
            self.convert(source_profile)

    def load_database_configuration(self, configuration: esdl.DatabaseConfiguration, credentials_dict: dict[str, Credentials]):
        """
        Loads profile information from a database configuration

        :param configuration: the database configuration
        :param credentials_dict: optional credentials dict to use to connect to the database
        :return: None
        """
        self.clear_profile()
        self.profile_type = ProfileType.DATETIME_LIST

        if configuration.type == esdl.DatabaseTypeEnum.POSTGRESQL:
            # handle postgres
            postgres = PostgresqlConfiguration(self.data_table_profile, credentials_dict)
            self.profile_data_list, self.profile_header = postgres.load_data()
            postgres.disconnect()
            self.num_profile_items = len(self.profile_data_list)
            if self.num_profile_items > 0:
                dt_index = self.get_profile_name_index(self.data_table_profile.datetimeColumnName)
                self.start_datetime = self.profile_data_list[0][dt_index]
                self.end_datetime = self.profile_data_list[-1][dt_index]

        else:
            raise UnsupportedDataConfiguration(
                f"DataConfiguration of type {configuration.type.name} is not yet supported")


    @staticmethod
    def _parse_esdl_profile_filters(esdl_filters):
       pass

    @staticmethod
    def create(data_table_profile: esdl.DataTableProfile, credentials_dict: dict[str, Credentials] = None) -> 'DataTableProfileManager':
        """
        method to create an instance of DataTableProfileManager using an esdl.DataTableProfile. The data referenced to in
        the profile is loaded from the associated DataConfiguration (e.g. DatabaseConfiguration or FileConfiguration)

        :param data_table_profile: esdl.DataTableProfile that is used as an input profile
        :param credentials_dict: dictionary of credentials to use for authentication with ['id' -> Credentials] mapping, where
        'id' refers to the id of the AbstractDataConfiguration that belongs to these credentials
        """
        configuration = data_table_profile.configuration

        if configuration is None:
            raise InvalidDataConfiguration("No DataConfiguration provided")
        if isinstance(configuration, esdl.DatabaseConfiguration):
            dtpman = DataTableProfileManager(data_table_profile)
            dtpman.load_database_configuration(configuration, credentials_dict)
            return dtpman
        elif isinstance(configuration, esdl.FileConfiguration):
            if configuration.type == esdl.FileTypeEnum.EXCEL:
                epm = ExcelProfileManager()
                # tableName is used as sheet name (see ecore model documentation)
                # TODO: load_excel ignores currently datetimeColumnName and columnName
                epm.load_excel(configuration.uri, data_table_profile.tableName)
                dtpman = DataTableProfileManager(data_table_profile, epm)
                return dtpman
            elif configuration.type == esdl.FileTypeEnum.CSV:
                dtpman = DataTableProfileManager(data_table_profile)
                dtpman.load_csv(configuration.uri)
                return dtpman
            else:
                raise UnsupportedDataConfiguration(f"DataConfiguration of type {configuration.type.name} is not yet supported")
        else:
            raise UnsupportedDataConfiguration(
                f"DataConfiguration {configuration} is not yet supported")



    def get_esdl_influxdb_profile(self, measurement: str, field_names: list, tags: dict = None):
        """
        Creates an esdl.InfluxDBProfile instance (or a list of instances) that refers to the data in the database.
        Is called by load_influxdb and save_influxdb

        :param measurement: name of the InfluxDB measurement where the data must be written to
        :param field_names: list of the fields that should be written to InfluxDB
        :param tags: dictionary with tags and tag values, that should be used when writing this data to InfluxDB
        :return: an esdl.InfluxDBProfile instance or a list of esdl.InfluxDBProfile instances in case multiple fields
                 were specified, with proper references to the data in the database
        """
        pass

    def save_influxdb(self, measurement: str, field_names: list, tags: dict = None):
        """
        Saves profile information to InfluxDB

        :param measurement: name of the InfluxDB measurement where the data must be written to
        :param field_names: list of the fields that should be written to InfluxDB
        :param tags: dictionary with tags and tag values, that should be used when writing this data to InfluxDB
        :return: an esdl.InfluxDBProfile instance or a list of esdl.InfluxDBProfile instances in case multiple fields
                 were specified, with proper references to the data in the database
        """
        pass


class NoDataException(Exception):
    """Thrown when no profile data can be written to InfluxDB"""
    pass


class WrongFilterFormatException(Exception):
    """Thrown when filter specification in ESDL profile cannot be parsed"""
    pass


class WrongTagsFormatException(Exception):
    """Thrown when the tags parameter has the wrong structure"""
    pass

class InvalidDataConfiguration(Exception):
    """Thrown when there is no or invalid DataConfiguration"""
    pass

class UnsupportedDataConfiguration(Exception):
    """Thrown when this DataConfiguration is not supported"""
    pass
