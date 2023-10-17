from configparser import ConfigParser
import os

env_file = os.path.join(os.path.dirname(os.path.relpath(__file__)), '.env')

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
