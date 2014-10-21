import sqlite3

conn = sqlite3.connect("yolo.db")
curs = conn.cursor()
query = "CREATE TABLE posts(id integer, title text, content text)"
result = curs.execute(query)
query = "INSERT INTO posts VALUES(1,'testpost1','testbody1')"
result = curs.execute(query)
query = "INSERT INTO posts VALUES(2,'testpost2','testbody2')"
result = curs.execute(query)
query = "INSERT INTO posts VALUES(3,'testpost3','testbody3')"
result = curs.execute(query)
query = "INSERT INTO posts VALUES(4,'testpost4','testbody4')"
result = curs.execute(query)
conn.commit();
conn.close();
