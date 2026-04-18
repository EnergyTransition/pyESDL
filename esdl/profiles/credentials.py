import logging
from dataclasses import dataclass
from os import environ

import esdl


@dataclass
class Credential:
    username: str
    password: str


class Credentials:
    credentials_dict: dict[str, Credential] = dict()

    # add a default credential based based on environment variables
    host = environ.get("DB_HOST", None)
    username = environ.get("DB_USER", None)
    password = environ.get("DB_PASSWORD", None)

    if host and username and password:
        credentials_dict[host] = Credential(username=username, password=password)
        logging.info(f"Detected DB credentials for {host}")

    @classmethod
    def add_credential(cls, id: str, username: str, password: str) -> None:
        """
        Adds credentials
        :param id: id of the DatabaseConfiguration, 'host' or 'host:port' for more generic matching.
        :param username: username
        :param password: password
        """
        cls.credentials_dict[id] = Credential(username, password)

    @classmethod
    def get_credential(cls, configuration: esdl.DatabaseConfiguration) -> Credential | None:
        # get credentials, first try on id of configuration
        credential = cls.credentials_dict.get(configuration.id, None)
        if credential is None and configuration.port is not None:
            # try on host:port
            credential = cls.credentials_dict.get(f"{configuration.host}:{configuration.port}", None)
        if credential is None:
            # try on host
            credential = cls.credentials_dict.get(configuration.host, None)

        if credential is None:
            logging.debug(
                f"No associated credentials found from DataConfiguration.id '{configuration.id}' or"
                f" DataConfiguration.host '{configuration.host}'."
                f" Assuming a public database and attempting to connect without credentials."
            )

        return credential
