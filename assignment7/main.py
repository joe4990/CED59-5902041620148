from flask import Flask,render_template , request
from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class JoeRegister(FlaskForm):
    user = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, message="Please enter password 8 character.")])
    name = StringField("Name", validators=[InputRequired()])
    lname = StringField("Lastname", validators=[InputRequired()])
    email = StringField("E-mail",  validators=[InputRequired("Please enter your email."), Email("Please enter your email again.")])

@app.route('/')
def joeForm():
    form = JoeRegister()
    return render_template('Register.html', form=form)


@app.route('/joeForm', methods=["GET", "POST"])
def register():
    form = JoeRegister()
    if form.validate_on_submit():
        return "Welcome"
    return render_template('Register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)