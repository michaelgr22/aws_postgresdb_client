import psycopg2


class PostgresDB:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None
        self.cur = None

    def __del__(self):
        try:
            self.cur.close()
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
        if self.cur == None:
            self.cur = self.conn.cursor()

    def execute_sql(self, sql):
        self.__connect()
        self.cur.execute(sql)
        data = None
        try:
            data = self.cur.fetchall()
        except:
            pass
        self.conn.commit()
        return data
