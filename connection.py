import pymysql

host = "localhost"
user = "root"
password = ""
database = "library"


con = pymysql.connect(host,user,password,database)
cur = con.cursor()