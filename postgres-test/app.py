# https://www.ashisuto.co.jp/db_blog/article/20160308_postgresql_with_python.html
import psycopg2
ip = "host=" + "172.20.0.121" + " "
port = "port=" + "5432" + " "
db = "dbname=" + "test" + " "
user = "user=" + "postgres" + ""
password  = "password=" + "code6513"
dsn = ip + port + db + user + password
conn = psycopg2.connect(dsn)
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
cur.execute("SELECT * FROM test;")
cur.fetchone()
conn.commit()
cur.close()
conn.close()