from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__) 
postdb = "yolo.db"
###

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

@app.route("/post/<title>")
def getpost(title):
    conn = sqlite3.connect(postdb)
    curs = conn.cursor()
    query = "SELECT * FROM posts WHERE title=?"
    curs.execute(query,[title])
    post = curs.fetchone()
    return render_template("post.html",
                           post=post)

@app.route("/newpost",methods=['GET','POST'])
def newpost():
    return render_template("newpost.html")

###

if __name__ == "__main__":
    app.debug = True
    app.run()
