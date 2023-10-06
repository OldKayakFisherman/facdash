from facconfig import ParserSettings
import csv
import sys

GENERAL_INPORT_COLUMNS = 69
CFDA_IMPORT_COLUMNS = 28
FINDING_IMPORT_COLUMNS = 14
CPAS_IMPORT_COLUMNS = 13
AGENCIES_IMPORT_COLUMNS = 4
EINS_IMPORT_COLUMNS = 4
DUNS_IMPORT_COLUMNS = 4
CAPTEXT_IMPORT_COLUMNS = 6
FINDINGSTEXT_IMPORT_COLUMNS = 6
NOTES_IMPORT_COLUMNS = 10
PASSTHROUGH_IMPORT_COLUMNS = 5
REVISION_IMPORT_COLUMNS = 19
UEIS_IMPORT_COLUMNS = 4

csv.field_size_limit(sys.maxsize)

def parse_general_import():
    records = []
    settings = ParserSettings()

    with open(settings.general_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == GENERAL_INPORT_COLUMNS:
                records.append(
                    {
                        "audityear": row[0],
                        "dbkey": row[1],
                        "typeofentity": row[2],
                        "fyenddate": row[3],
                        "audittype": row[4],
                        "periodcovered": row[5],
                        "numbermonths": row[6],
                        "ein": row[7],
                        "multipleeins": row[8],
                        "einsubcode": row[9],
                        "duns": row[10],
                        "multipleduns": row[11],
                        "auditeename": row[12],
                        "street1": row[13],
                        "street2": row[14],
                        "city": row[15],
                        "state": row[16],
                        "zipcode": row[17],
                        "auditeecontact": row[18],
                        "auditeetitle": row[19],
                        "auditeephone": row[20],
                        "auditeefax": row[21],
                        "auditeeemail": row[22],
                        "auditeedatesigned": row[23],
                        "auditeenametitle": row[24],
                        "cpafirmname": row[25],
                        "cpastreet1": row[26],
                        "cpastreet2": row[27],
                        "cpacity": row[28],
                        "cpastate": row[29],
                        "cpazipcode": row[30],
                        "cpacontact": row[31],
                        "cpatitle": row[32],
                        "cpaphone": row[33],
                        "cpafax": row[34],
                        "cpaemail": row[35],
                        "cpadatesigned": row[36],
                        "cog_over": row[37],
                        "cogagency": row[38],
                        "oversightagency": row[39],
                        "typereport_fs": row[40],
                        "sp_framework": row[41],
                        "sp_framework_required": row[42],
                        "typereport_sp_framework": row[43],
                        "goingconcern": row[44],
                        "reportablecondition": row[45],
                        "materialweakness": row[46],
                        "materialnoncompliance": row[47],
                        "typereport_mp": row[48],
                        "dup_reports": row[49],
                        "dollarthreshold": row[50],
                        "lowrisk": row[51],
                        "reportablecondition_mp": row[52],
                        "materialweakness_mp": row[53],
                        "qcosts": row[54],
                        "cyfindings": row[55],
                        "pyschedule": row[56],
                        "totfedexpend": row[57],
                        "datefirewall": row[58],
                        "previousdatefirewall": row[59],
                        "reportrequired": row[60],
                        "multiple_cpas": row[61],
                        "auditor_ein": row[62],
                        "facaccepteddate": row[63],
                        "cpaforeign": row[64],
                        "cpacountry": row[65],
                        "entity_type": row[66],
                        "uei": row[67],
                        "multipleueis": row[68]
                    }
                )

    return records


def parse_cfda_records():

    records = []
    settings = ParserSettings()

    with open(settings.cfda_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == CFDA_IMPORT_COLUMNS:
                records.append(
                    {
                        "audityear": row[0],
                        "dbkey": row[1],
                        "ein": row[2],
                        "cfda": row[3],
                        "awardidentification": row[4],
                        "rd": row[5],
                        "federalprogramname": row[6],
                        "amount": row[7],
                        "clustername": row[8],
                        "stateclustername": row[9],
                        "programtotal": row[10],
                        "clustertotal": row[11],
                        "direct": row[12],
                        "passthroughaward": row[13],
                        "passthroughamount": row[14],
                        "majorprogram": row[15],
                        "typereport_mp": row[16],
                        "typerequirement": row[17],
                        "qcosts2": row[18],
                        "findings": row[19],
                        "findingrefnums": row[20],
                        "arra": row[21],
                        "loans": row[22],
                        "loanbalance": row[23],
                        "findingscount": row[24],
                        "elecauditsid": row[25],
                        "otherclustername": row[26],
                        "cfdaprogramname": row[27],
                    }
                )

    return records


def parse_finding_records():

    records = []
    settings = ParserSettings()

    with open(settings.findings_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == FINDING_IMPORT_COLUMNS:
                records.append(
                    {
                        "dbkey": row[0],
                        "audityear": row[1],
                        "elecauditsid": row[2],
                        "elecauditfindingsid": row[3],
                        "findingsrefnums": row[4],
                        "typerequirement": row[5],
                        "modifiedopinion": row[6],
                        "othernoncompliance": row[7],
                        "materialweakness": row[8],
                        "significantdeficiency": row[9],
                        "otherfindings": row[10],
                        "qcosts": row[11],
                        "repeatfinding": row[12],
                        "priorfindingrefnums": row[13]
                    })

    return records

def parse_cpa_records():

    records = []
    settings = ParserSettings()

    with open(settings.cpas_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == CPAS_IMPORT_COLUMNS:
                records.append(
                    {
                        "dbkey": row[0],
                        "audityear": row[1],
                        "cpafirmname": row[2],
                        "cpaein": row[3],
                        "cpastreet1": row[4],
                        "cpacity": row[5],
                        "cpastate": row[6],
                        "cpazipcode": row[7],
                        "cpacontact": row[8],
                        "cpatitle": row[9],
                        "cpaphone": row[10],
                        "cpafax": row[11],
                        "cpaemail": row[12]
                    }
                )

    return records


def parse_agency_records():

    records = []
    settings = ParserSettings()

    with open(settings.agency_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == AGENCIES_IMPORT_COLUMNS:
                records.append(
                    {
                        "audityear": row[0],
                        "dbkey": row[1],
                        "ein": row[2],
                        "agency": row[3]
                    }
                )

    return records


def parse_ein_records():

    records = []
    settings = ParserSettings()

    with open(settings.eins_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == EINS_IMPORT_COLUMNS:
                records.append(
                    {
                        "audityear": row[0],
                        "dbkey": row[1],
                        "ein": row[2],
                        "einseqnum": row[3]
                    }
                )

    return records


def parse_dun_records():

    records = []
    settings = ParserSettings()

    with open(settings.duns_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == DUNS_IMPORT_COLUMNS:
                records.append(
                    {
                        "audityear": row[0],
                        "dbkey": row[1],
                        "duns": row[2],
                        "dunseqnum": row[3]
                    }
                )

    return records

def parse_captext_records():

    records = []
    settings = ParserSettings()

    with open(settings.captext_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == CAPTEXT_IMPORT_COLUMNS:
                records.append(
                    {
                        "seq_number": row[0],
                        "dbkey": row[1],
                        "audityear": row[2],
                        "findingrefnums": row[3],
                        "text": row[4],
                        "chartstables": row[5]
                    }
                )

    return records


def parse_findingstext_records():

    records = []
    settings = ParserSettings()

    with open(settings.findingstext_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == FINDINGSTEXT_IMPORT_COLUMNS:
                records.append(
                    {
                        "seq_number": row[0],
                        "dbkey": row[1],
                        "audityear": row[2],
                        "findingrefnums": row[3],
                        "text": row[4],
                        "chartstables": row[5]
                    }
                )

    return records


def parse_passhthrough_records():

    records = []
    settings = ParserSettings()

    with open(settings.passthrough_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == PASSTHROUGH_IMPORT_COLUMNS:
                records.append(
                    {
                        "dbkey": row[0],
                        "audityear": row[1],
                        "elecauditsid": row[2],
                        "passthroughname": row[3],
                        "passthroughid": row[4]
                    }
                )

    return records


def parse_notes_records():

    records = []
    settings = ParserSettings()

    with open(settings.notes_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == NOTES_IMPORT_COLUMNS:
                records.append(
                    {
                        "source_id": row[0],
                        "reportid": row[1],
                        "version": row[2],
                        "audityear": row[3],
                        "dbkey": row[4],
                        "seq_number": row[5],
                        "type_id": row[6],
                        "note_index": row[7],
                        "title": row[8],
                        "content": row[9]
                    }
                )

    return records


def parse_revision_records():

    records = []
    settings = ParserSettings()

    with open(settings.revisions_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == REVISION_IMPORT_COLUMNS:
                records.append(
                    {
                        "dbkey": row[0],
                        "audityear": row[1],
                        "geninfo": row[2],
                        "geninfo_explain": row[3],
                        "federalawards": row[4],
                        "federalawards_explain": row[5],
                        "notestosefa": row[6],
                        "notestosefa_explain": row[7],
                        "auditinfo": row[8],
                        "auditinfo_explain": row[9],
                        "findings": row[10],
                        "findings_explain": row[11],
                        "findingstext": row[12],
                        "findingstext_explain": row[13],
                        "cap": row[14],
                        "cap_explain": row[15],
                        "other": row[16],
                        "other_explain": row[17],
                        "elecrptrevisionid": row[18]
                    }
                )

    return records


def parse_uei_records():

    records = []
    settings = ParserSettings()

    with open(settings.ueis_file, encoding="us-ascii", errors="ignore") as csvfile:
        census_csv_reader = csv.reader(csvfile, delimiter='|')

        # skip the header
        next(census_csv_reader, None)

        for row in census_csv_reader:

            if len(row) == UEIS_IMPORT_COLUMNS:
                records.append(
                    {
                        "audityear": row[0],
                        "dbkey": row[1],
                        "uei": row[2],
                        "ueiseqnum": row[3]
                    }
                )

    return records

