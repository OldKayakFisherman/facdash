from gsa_config import APISettings, ImportSettings
from gsa_data import get_last_import
import requests
from requests.auth import HTTPDigestAuth
import json
from datetime import datetime, timedelta



def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def read_general_records() -> []:

    result = []
    last_import_date = get_last_import()

    if not last_import_date[0]:
        last_import_date = ImportSettings().dissemination_start
    else:
        last_import_date = datetime.combine(last_import_date[0], datetime.min.time())

    start_seed_date = last_import_date + timedelta(days=1)
    end_seed_date = datetime.now() - timedelta(days=1)

    for target_date in daterange(start_seed_date, end_seed_date):
        target_date_parameter = target_date.strftime("%Y-%m-%d")
        url_part = f"general?fac_accepted_date=eq.{target_date_parameter}"

        general_data = poll_api(url_part)

        for general_record in general_data:
            result.append(general_record)

    return result
    
def read_awards_records(reports:[]):

    url_part = f'federal_awards?report_id=in.({report_params(reports)})'
    return poll_api(url_part)

def read_cpa_records(reports: []):

    url_part = f'secondary_auditors?report_id=in.({report_params(reports)})'
    return poll_api(url_part)

def read_notes_to_sefa(reports: []):

    url_part = f'notes_to_sefa?report_id=in.({report_params(reports)})'
    return poll_api(url_part)

def read_corrective_action_plans(reports: []):
    url_part = f'corrective_action_plans?report_id=in.({report_params(reports)})'
    return poll_api(url_part)


def read_findings(reports: []):
    url_part = f'findings?report_id=in.({report_params(reports)})'
    return poll_api(url_part)


def read_passthroughs(reports: []):
    url_part = f'passthrough?report_id=in.({report_params(reports)})'
    return poll_api(url_part)

def read_additional_ueis(reports: []):
    url_part = f'additional_ueis?report_id=in.({report_params(reports)})'
    return poll_api(url_part)

def read_findings_text(reports: []):
    url_part = f'findings_text?report_id=in.({report_params(reports)})'
    return poll_api(url_part)


def poll_api(url_part: str):

    api_settings = APISettings()

    url = f'{api_settings.api_url}/{url_part}'

    headers = {
        'X-Api-Key': api_settings.api_key
    }

    response = requests.get(url, auth=None, headers=headers)

    if response and response.ok:
        return response.json()
    else:
        return None

def report_params(reports):
    return ','.join(reports)
