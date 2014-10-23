from flask import Flask,render_template,request
import sqlite3
import csv

app = Flask(__name__) 
postdb = "yolo.db"
###
#this is how you loop through a database using csv (instructions
#      for a future me):
#
#(after conn and curs are used)
#
#Base="insert into posts values('%(title)s','%(post)s')"
#for line in csv.DictReader(open("your csv file, remember to init")):
#    q=Base%line
#    print q            (for testing purposes)
#    curs.execute(q)
#
#      then read out the table using select & stuff and put it on
#      the HTML, or even just put it in the html as you loop through
#      though that might be difficult

#helper function for reading:
def helpReader():
    conn = sqlite3.connect("yolo.db")
    curs = conn.cursor()
    Base="insert into posts values(%(id)d,'%(title)s','%(post)s')"
    for line in csv.DictReader(open("storage.csv")):
        q=Base%line
        print q #for testing purposes
        curs.execute(q)
    conn.commit()
    conn.close()

@app.route("/")
@app.route("/test",methods=['GET','POST'])
def home():
    conn = sqlite3.connect(postdb)
    curs = conn.cursor()
    if request.method=="POST":
        query = "SELECT count(*) FROM posts"
        result = curs.execute(query)
        newid = result.fetchone()[0] + 1
        newtitle = request.form["title"]
        newbody = request.form["body"]
        query = "SELECT * FROM posts WHERE title=?"
        curs.execute(query,[newtitle])
        if len(curs.fetchall())>0:
            return render_template("error.html",
                                   title=newtitle)
        query = "INSERT INTO posts VALUES (?,?,?)"
        curs.execute(query,[newid,newtitle,newbody])
        conn.commit()
    query = "SELECT * FROM posts ORDER BY id DESC"
    result = curs.execute(query)
    posts = curs.fetchall()
    print posts
    return render_template("test.html",
                           posts=posts)

@app.route("/post/<title>",methods=['GET','POST'])
def getpost(title):
    conn = sqlite3.connect(postdb)
    curs = conn.cursor()
    if request.method=="POST":
        newcontent = request.form["comment"]
        if len(newcontent)!=0:
            newauthor = request.form["author"]
            query = "SELECT count(*) FROM comments WHERE post=?"
            result = curs.execute(query,[title])
            newid = result.fetchone()[0] + 1
            query = "INSERT INTO comments VALUES(?,?,?,?)"
            curs.execute(query,[title,newid,newauthor,newcontent])
            conn.commit()
    query = "SELECT * FROM posts WHERE title=?"
    curs.execute(query,[title])
    post = curs.fetchone()
    query = "SELECT * FROM comments WHERE post=? ORDER BY id ASC"
    curs.execute(query,[title])
    comments = curs.fetchall()
    print comments
    return render_template("post.html",
                           post=post,
                           comments=comments)

###

if __name__ == "__main__":
    app.debug = True
    app.run()
