from flask import Flask,jsonify,request
from werkzeug.routing import BaseConverter,ValidationError

_USERS = {'1':'Vinod','2':'Vukkalam'}
_IDS = {val: id for id,val in _USERS.items()}

class RegisteredUser(BaseConverter):
    def to_python(self,value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()

    def to_url(self,value):
        return _IDS[value]
app = Flask(__name__)
app.url_map.converters['registered']=RegisteredUser

@app.route('/<registered:name>')
def person(name):
    response=jsonify({'Hi! welcome':name})
    return response

if __name__=='__main__':
    app.run(debug=True)
