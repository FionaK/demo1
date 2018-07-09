import pymysql
connection = pymysql.connect(host='localhost',user='root',password='',db='details',)
cur = connection.cursor()