from flask import Flask,render_template

app=Flask(__name__)

@app.route("/vinodvr")
def exampleRender():
    return render_template("githubVinodvr.html")

if __name__=='__main__':
    app.run(debug=True)
