from facdata import connection_pool

class HealthCheck:

    def check(self):

        result = {}

        try:
            cn = connection_pool.getconn()

            if cn:
                result['database'] = 'Database check passed'
                connection_pool.putconn(cn)
        except Exception as ex:

            result['database'] = f'Database check failed: {str(ex)}'

        return result
