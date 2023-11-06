from facdata import connection_pool
import os, shutil
from urllib.request import urlretrieve
from zipfile import ZipFile

class HealthCheck:

    @staticmethod
    def check():
        result = {}

        try:
            cn = connection_pool.getconn()

            if cn:
                result['database'] = 'Database check passed'
                connection_pool.putconn(cn)
        except Exception as ex:

            result['database'] = f'Database check failed: {str(ex)}'


        return result

class CensusFACImporter:

    @staticmethod
    def do_import():

        result = {}

        # Check the dir
        local_path = os.path.dirname(os.path.relpath(__file__))
        target_dir = os.path.join(local_path, os.getenv("WORK.DIR"))

        result['work.dir'] = target_dir

        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)
        else:
            # clean the directory
            for filename in os.listdir(target_dir):
                file_path = os.path.join(target_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

        #download the file
        target_url = os.getenv('FAC.DOWNLOAD.FILE')
        download_file = os.path.join(target_dir, 'AllFAC.zip')

        result['download.file'] = download_file

        urlretrieve(target_url, download_file)

        result['file.downloaded'] = True

        ZipFile(download_file).extractall(target_dir)

        result['files'] = []

        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            result['files'].append(file_path)

        return result
