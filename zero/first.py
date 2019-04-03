from flask import Flask,jsonify
app=Flask(__name__)

@app.route('/')
def myflaskservice():
    return jsonify({'Hi': 'Welcome! Vinod to the world of synchronus python flask microservice framework'})
	
if __name__=='__main__':
    app.run(debug=True)
