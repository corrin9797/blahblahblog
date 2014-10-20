import sqlite3
import csv
conn=sqlite3.connect("test.db")

c=conn.cursor()
#q="CREATE TABLE posts(title text, post text)"

#c.execute(q)

Base="insert into posts values('%(title)s','%(post)s')"
for line in csv.DictReader(open("storage.csv")):
	q=Base%line
	print q
	c.execute(q)


conn.commit()

