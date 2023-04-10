#Install MySQL Connector using pip --> pip install mysql-connector-python
import mysql.connector

dbconfig = {'host': '0.0.0.0',
            'port': 33060,
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB',}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """insert into log
        (phrase, letters, ip, browser_string, results)
        values
        (%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('hitch-hicker', 'xyz', '127.0.0.1', 'Chrome', 'set()'))

conn.commit()

# res = cursor.fetchall()

# for row in res:
#     print(row)