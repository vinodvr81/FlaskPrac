from flask import Flask
from flask_mail import Mail,Message

app=Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='vukkalamvinod@gmail.com'
app.config['MAIL_PASSWORD']='****'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route('/')
def index():
    msg = Message('Hello',sender='vukkalamvinod@gmail.com',recipients=['vinod.vukkalam@gmail.com'])
    msg.body = "Hello Flask! This is sent from my Alias gmail account"
    mail.send(msg)
    return "Message Sent"

if __name__=='__mail__':
    app.run(debug=True)
