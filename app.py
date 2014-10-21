from flask import Flask,render_template,request


app = Flask(__name__) 



@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("home2.html")
    else:
        title  = request.form['title']
        content = request.form['content']
        return render_template('print.html', title=title, content=content)
        
@app.route("/post", methods=["GET","POST"])
def post():
    return render_template("post.html")




if __name__ == "__main__":
    app.debug = True
    app.run()
