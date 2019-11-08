# auth/forms.py
# Frontend validation for user input
# from flask_wtf import FlaskForm
# from wtforms import Form, StringField, PasswordField, validators, SubmitField
# from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional
# from wtforms import Form, StringField, PasswordField, validators, SubmitField
# from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional


class SignupForm(Form):
    """User signup form."""
    
    name = StringField("Name", 
                        validators=[DataRequired(message=("A username is required."))]
                        )   
    email = StringField("Email", 
                        validators=[Length(min=3, message=("Please enter a valid email address.")),
                                    Email(message=("Please enter a valid email address.")),
                                    DataRequired(message=("Please enter a valid email address."))]
                        )
    password = PasswordField("Password",
                            validators=[DataRequired(message="Please enter a password."),
                                        Length(min=6, message=("Please select a stronger password.")),
                                        EqualTo("confirm", message="Passwords must match.")]
                            )
    confirm = PasswordField("Confirm your password.",)
    submit = SubmitField("Register")


class LoginForm(Form):
    """User login form."""
    email = StringField("Email", 
                        validators=[DataRequired("Please enter a valid email address."),
                                    Email("Please enter a valid email address.")]
                        )
    password = PasswordField("Password", 
                            validators=[DataRequired("Please enter your password.")])
    submit = SubmitField("Log in")
