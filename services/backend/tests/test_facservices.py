import unittest

from facservices import CensusFACImporter

class CensusFACImporterTestCase(unittest.TestCase):

    def test_do_import(self):
        result = CensusFACImporter.do_import()

        self.assertIsNotNone(result['work.dir'])
        self.assertIsNotNone(result['download.file'])
        self.assertTrue(result['file.downloaded'])
        self.assertTrue(len(result['files']) > 0)
