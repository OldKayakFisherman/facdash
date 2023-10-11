from facparser import *
from facdata import *
import logging
from facconfig import ImportSettings

def import_general():

    settings = ImportSettings()
    process_name = 'general'

    if settings.import_general:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_general_import()
        log_process_import(process_name)
        insert_general_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)

def import_cfda():

    settings = ImportSettings()
    process_name = 'cfdas'

    if settings.import_cfda:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_cfda_records()
        log_process_import(process_name)
        insert_cfda_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)


def import_findings():

    settings = ImportSettings()
    process_name = 'findings'

    if settings.import_findings:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_finding_records()
        log_process_import(process_name)
        insert_finding_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)


def import_cpas():

    settings = ImportSettings()
    process_name = 'cpas'

    if settings.import_cpas:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_cpa_records()
        log_process_import(process_name)
        insert_cpa_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)


def import_agencies():

    settings = ImportSettings()
    process_name = 'agencies'

    if settings.import_agencies:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_agency_records()
        log_process_import(process_name)
        insert_agency_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)


def import_eins():

    settings = ImportSettings()
    process_name = 'eins'

    if settings.import_eins:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_ein_records()
        log_process_import(process_name)
        insert_ein_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)


def import_duns():

    settings = ImportSettings()
    process_name = 'duns'

    if settings.import_duns:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_dun_records()
        log_process_import(process_name)
        insert_dun_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)

def import_captext():

    settings = ImportSettings()
    process_name = 'captext'

    if settings.import_captext:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_captext_records()
        log_process_import(process_name)
        insert_captext_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)


def import_findingstext():

    settings = ImportSettings()
    process_name = 'findingstext'

    if settings.import_findingstext:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_findingstext_records()
        log_process_import(process_name)
        insert_findingstext_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)


def import_notes():

    settings = ImportSettings()
    process_name = 'notes'

    if settings.import_notes:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_notes_records()
        log_process_import(process_name)
        insert_notes_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)

def import_passthroughs():

    settings = ImportSettings()
    process_name = 'passthrough'

    if settings.import_passthrough:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_passhthrough_records()
        log_process_import(process_name)
        insert_passthrough_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)

def import_revisions():

    settings = ImportSettings()
    process_name = 'revisions'

    if settings.import_revisions:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_revision_records()
        log_process_import(process_name)
        insert_revision_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)

def import_ueis():

    settings = ImportSettings()
    process_name = 'ueis'

    if settings.import_ueis:
        log_process_clean(process_name)
        clean_import_table(process_name)
        log_process_parse(process_name)
        parsed_records = parse_uei_records()
        log_process_import(process_name)
        insert_uei_records(parsed_records)
        log_process_complete(process_name)
    else:
        log_process_skipped(process_name)


def log_process_skipped(process_name):
    logging.debug(f'Skipping process {process_name} due to configuration setting')

def log_process_clean(process_name):
    logging.debug(f"Cleaning {process_name} import Table")


def log_process_parse(process_name):
    logging.debug(f"Parsing {process_name} records")


def log_process_import(process_name):
    logging.debug(f"Importing {process_name} records")


def log_process_complete(process_name):
    logging.debug(f"{process_name} import complete")
