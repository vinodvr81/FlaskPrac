from flask import Flask
app=Flask(__name__)

@app.route("/<enter>")
def hello_enter(enter):
    return "The string that you have entered is %s which results in dynamic web page creation"%enter

if __name__=='__main__':
    app.run(debug=True)

