import os
from configparser import ConfigParser

env_file = os.path.join(os.path.dirname(os.path.relpath(__file__)), '.env')


def read_config_boolean(config, section:str, key:str):

    result: bool = False

    if config[section] is not None:
        result = str(config[section][key]).lower() in ("yes", "true", "t", "1", "y")

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


class ParserSettings:

    def __init__(self):
        config = ConfigParser()
        config.read(env_file)

        self._import_dir = os.path.expanduser(config['parser']['data.dir'])
        self._general_file = os.path.join(self._import_dir, 'general.txt')
        self._cfda_file = os.path.join(self._import_dir, 'cfda.txt')
        self._findings_file = os.path.join(self._import_dir, 'findings.txt')
        self._cpas_file = os.path.join(self._import_dir, 'cpas.txt')
        self._agency_file = os.path.join(self._import_dir, 'agency.txt')
        self._eins_file = os.path.join(self._import_dir, 'eins.txt')
        self._duns_file = os.path.join(self._import_dir, 'duns.txt')
        self._captext_file = os.path.join(self._import_dir, 'captext.txt')
        self._findingstext_file = os.path.join(self._import_dir, 'findingstext.txt')
        self._notes_file = os.path.join(self._import_dir, 'notes.txt')
        self._passthrough_file = os.path.join(self._import_dir, 'passthrough.txt')
        self._revisions_file = os.path.join(self._import_dir, 'revisions.txt')
        self._ueis_file = os.path.join(self._import_dir, 'ueis.txt')
    @property
    def import_dir(self) -> str:
        return self._import_dir

    @property
    def general_file(self) -> str:
        return self._general_file

    @property
    def cfda_file(self) -> str:
        return self._cfda_file

    @property
    def findings_file(self) -> str:
        return self._findings_file


    @property
    def cpas_file(self)-> str:
        return self._cpas_file


    @property
    def agency_file(self) -> str:
        return self._agency_file

    @property
    def eins_file(self) -> str:
        return self._eins_file

    @property
    def duns_file(self) -> str:
        return self._duns_file

    @property
    def captext_file(self) -> str:
        return self._captext_file

    @property
    def findingstext_file(self) -> str:
        return self._findingstext_file

    @property
    def notes_file(self) -> str:
        return self._notes_file

    @property
    def passthrough_file(self) -> str:
        return self._passthrough_file

    @property
    def revisions_file(self) -> str:
        return self._revisions_file


    @property
    def ueis_file(self) -> str:
        return self._ueis_file


class ImportSettings:

    def __init__(self):
        config = ConfigParser()
        config.read(env_file)
        self._import_general = read_config_boolean(config, 'import', 'import.general')
        self._import_cfda = read_config_boolean(config, 'import', 'import.cfda')
        self._import_findings = read_config_boolean(config, 'import', 'import.findings')
        self._import_cpas = read_config_boolean(config, 'import', 'import.cpas')
        self._import_agencies = read_config_boolean(config, 'import', 'import.agencies')
        self._import_eins = read_config_boolean(config, 'import', 'import.eins')
        self._import_duns = read_config_boolean(config, 'import', 'import.duns')
        self._import_captext = read_config_boolean(config, 'import', 'import.captext')
        self._import_findingstext = read_config_boolean(config, 'import', 'import.findingstext')
        self._import_notes = read_config_boolean(config, 'import', 'import.notes')
        self._import_passthrough = read_config_boolean(config, 'import', 'import.passthroughs')
        self._import_revisions = read_config_boolean(config, 'import', 'import.revisions')
        self._import_ueis = read_config_boolean(config, 'import', 'import.ueis')

    @property
    def import_general(self) -> bool:
        return self._import_general

    @property
    def import_cfda(self) -> bool:
        return self._import_cfda

    @property
    def import_findings(self) -> bool:
        return self._import_findings

    @property
    def import_cpas(self) -> bool:
        return  self._import_cpas


    @property
    def import_agencies(self) -> bool:
        return self._import_agencies

    @property
    def import_eins(self) -> bool:
        return self._import_eins

    @property
    def import_duns(self) -> bool:
        return self._import_duns

    @property
    def import_captext(self) -> bool:
        return self._import_captext

    @property
    def import_findingstext(self) -> bool:
        return self._import_findingstext

    @property
    def import_notes(self) -> bool:
        return self._import_notes

    @property
    def import_passthrough(self) -> bool:
        return self._import_passthrough

    @property
    def import_revisions(self) -> bool:
        return self._import_revisions

    @property
    def import_ueis(self) -> bool:
        return self._import_ueis
