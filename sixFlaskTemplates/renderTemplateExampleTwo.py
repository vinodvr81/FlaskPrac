from flask import Flask,render_template

app=Flask(__name__)

@app.route("/vinodvr81")
def exampleRender():
    return render_template("githubVinodvr81.html")

if __name__=='__main__':
    app.run(debug=True)
