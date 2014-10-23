import sqlite3

conn = sqlite3.connect("yolo.db")
curs = conn.cursor()
query = "CREATE TABLE comments(post text, id integer, author text, content text)"
result = curs.execute(query)
query = "CREATE TABLE posts(id integer, title text, content text)"
result = curs.execute(query)
query = "INSERT INTO posts VALUES(1,'testpost1','testbody1')"
result = curs.execute(query)
conn.commit();
conn.close();
