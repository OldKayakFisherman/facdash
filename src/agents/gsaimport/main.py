from gsa_api_reader import *
from gsa_data import *

def perform_import():

    general_records = read_general_records()

    if general_records:

        unique_reports = [x['report_id'] for x in general_records]

        # pull the records for the identified reports
        awards = read_awards_records(unique_reports)
        secondary_auditors = read_cpa_records(unique_reports)
        notes_to_sefa = read_notes_to_sefa(unique_reports)
        corrective_action_plans = read_corrective_action_plans(unique_reports)
        findings = read_findings(unique_reports)
        passthroughs = read_passthroughs(unique_reports)
        ueis = read_additional_ueis(unique_reports)
        findings_text = read_findings_text(unique_reports)

        # save the records
        save_general_records(general_records)
        save_awards(awards)
        save_secondary_auditors(secondary_auditors)
        save_notes_to_sefa(notes_to_sefa)
        save_corrective_action_plans(corrective_action_plans)
        save_findings(findings)
        save_passthroughs(passthroughs)
        save_ueis(ueis)
        save_findings_text(findings_text)
        print("Operation complete")
    else:
        print("Nothing to do")

if __name__ == '__main__':
    perform_import()


