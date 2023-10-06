from facimport import *

def import_data():
    logging.basicConfig(level=logging.DEBUG)
    import_general()
    import_cfda()
    import_findings()
    import_cpas()
    import_agencies()
    import_eins()
    import_duns()
    import_captext()
    import_findingstext()
    import_notes()
    import_passthroughs()
    import_revisions()
    import_ueis()


if __name__ == '__main__':
    import_data()

