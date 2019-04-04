from flask_wtf import Form
from wtforms import TextField,IntegerField,TextAreaField,SubmitField,RadioField,SelectField

from wtforms import validators,ValidationError

class FormContact(Form):
    name = TextField("Name Of Employee",[validators.Required("Please enter your name.")])
    Gender = RadioField('Gender',choices=[('M','Male'),('F','Female')])
    Address = TextAreaField("Adress")

    email = TextField("Email",[validators.Required("Please enter your email address."),validators.Email("Please enter your email address.")])
    Age = IntegerField("age")
    language = SelectField('Languages',choices = [('cpp','C++'),('py','python')])
    submit = SubmitField("send")
