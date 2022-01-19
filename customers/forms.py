from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators, ValidationError
from flask_wtf.file import FileRequired, FileAllowed, FileField


class CustomerRegistrationForm(Form):
    name = StringField('Name: ')
    username = StringField('Username:',validators=[validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ',[validators.DataRequired(), validators.EqualTo('confirm',message='Both password must match! ')])
    confirm = PasswordField('Repeat Password: ',[validators.DataRequired()])
    country = StringField('Country: ',[validators.DataRequired()])
    state = StringField('State: ',[validators.DataRequired()])
    contact = StringField('Contact: ',[validators.DataRequired()])
    address = StringField('Address: ',[validators.DataRequired()])
    zipcode = StringField('Zipcode: ',[validators.DataRequired()])

    submit = SubmitField('Register')


class CustomerLogin(Form):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ',[validators.DataRequired()])

    # submit = SubmitField('Login')
