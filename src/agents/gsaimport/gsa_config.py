import os
from configparser import ConfigParser
from datetime import datetime

env_file = os.path.join(os.path.dirname(os.path.relpath(__file__)), '.env')


def read_config_boolean(config, section:str, key:str):

    result: bool = False

    if config[section] is not None:
        result = str(config[section][key]).lower() in ("yes", "true", "t", "1", "y")

    return result


def read_config_date(config, section:str, key:str):

    result: datetime = None

    if config[section] is not None:
        result = datetime.strptime(str(config[section][key]), "%Y-%m-%d")

    return result


class DatabaseSettings:

    def __init__(self):
        config = ConfigParser()
        config.read(env_file)

        self._host = str(config['database']['pg.host'])
        self._port = int(config['database']['pg.port'])
        self._user = str(config['database']['pg.user'])
        self._database = str(config['database']['pg.database'])
        self._schema = str(config['database']['pg.schema'])

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def user(self) -> str:
        return self._user

    @property
    def database(self):
        return  self._database

    @property
    def schema(self):
        return self._schema


class ImportSettings:
    def __init__(self):
        config = ConfigParser()
        config.read(env_file)
        self._dissemination_start = read_config_date(config, 'import', 'gsa.dissemination.start')

    @property
    def dissemination_start(self) -> datetime:
        return self._dissemination_start

class APISettings:

    def __init__(self):
        config = ConfigParser()
        config.read(env_file)
        self._api_key = str(config['api']['api.key'])
        self._api_user = str(config['api']['api.user'])
        self._api_url = str(config['api']['api.url'])


    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def api_user(self) -> str:
        return self._api_user

    @property
    def api_url(self) -> str:
        return self._api_url

