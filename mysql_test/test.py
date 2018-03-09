import mysql_test.mysql_conn as mysql_conn

test1       = mysql_conn.MyslqConn('localhost', '3306', 'root', 'root', 'kms')
sql         = 'select count(*) from kms_user'
r1          = test1.query(sql)

print(r1)

