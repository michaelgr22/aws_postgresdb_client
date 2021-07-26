import psycopg2


class AwsPostgresDBClient:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def __del__(self):
        try:
            self.conn.close()
        except:
            pass

    def __connect(self):
        if self.conn == None:
            self.conn = psycopg2.connect(host=self.host,
                                         port=self.port,
                                         dbname=self.database,
                                         user=self.user,
                                         password=self.password)

    def execute_sql(self, sql, values=(), autocommit=False):
        self.__connect()
        self.conn.set_session(autocommit=autocommit)
        cur = self.conn.cursor()
        cur.execute(sql, values)
        data = None
        try:
            data = cur.fetchall()
        except:
            pass
        self.conn.commit()
        cur.close()
        return data
