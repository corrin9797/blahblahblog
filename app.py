from flask import Flask,render_template,request

app = Flask(__name__) 

###

@app.route("/test")
def home():
    return render_template("test.html")

###

if __name__ == "__main__":
    app.debug = True
    app.run()
