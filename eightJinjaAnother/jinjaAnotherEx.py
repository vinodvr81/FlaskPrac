from flask import Flask, render_template

app=Flask(__name__)

@app.route("/marks/<int:score>")
def getmarks(score):
    return render_template("marks.html",marks=score)

if __name__=='__main__':
    app.run(debug=True)
