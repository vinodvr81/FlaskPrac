from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/<strEnter>')
def stringEnter(strEnter):
    return jsonify({'Hi':'Welcome '+strEnter})

if __name__=='__main__':
    app.run(debug=True)
