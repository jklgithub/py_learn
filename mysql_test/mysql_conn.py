import pymysql

class MyslqConn:
    conf        = {}

    def __init__(self, host, port, user, passwd, db):
        self.sqlCount   = 0
        self.connCount  = 0
        self.host       = host
        self.port       = port
        self.user       = user
        self.passwd     = passwd
        self.db         = db
        self.conn       = False
        self.cur        = False
        print('Mysql conn init ok: ' + self.host + ':' + self.port + '/' + self.db)

    def reConn(self):
        print('Mysql conn start: ' + self.host + ':' + self.port + '/' + self.db)
        self.conn       = pymysql.connect(host = self.host, port = int(self.port), user = self.user, passwd = self.passwd, db = self.db)
        print('11')
        self.cur        = self.conn.cursor()
        self.connCount  = self.connCount + 1
        print('Mysql conn success: ' + self.host + ':' + self.port + '/' + self.db)

    def __del__(self):
        if self.cur:
            self.cur.close()
            self.conn.close()
        self.connCount = self.connCount - 1

    def query(self, sql):
        self.reConn()
    #    if not self.cur:
    #        self.reConn()
        self.cur.execute(sql)
        r = []
        for row in self.cur:
            r.append(row)
        return r



#        sql = "select count(id) from tabName"
#        rd = query(sql)
#        print(rd[0])