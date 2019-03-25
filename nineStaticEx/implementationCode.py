from flask import Flask,render_template

app=Flask(__name__)

@app.route("/hello")

def staticImplement():
    return render_template("form.html")

if __name__=='__main__':
    app.run(debug=True)


#http://localhost:5000/hello?Name=vinod&EMail=vinod.vukkalam%40gmail.com&Zip=50015&Country=3#
