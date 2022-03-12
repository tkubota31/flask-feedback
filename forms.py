# from wtforms import StringField, PasswordField
# from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
# from flask_wtf import FlaskForm

# class RegisterForm(FlaskForm):
#     """Form to register user"""
#     username = StringField("username", validators=[InputRequired()])

#     password= StringField("password", validators=[InputRequired()])

#     email = StringField("email", validators=[InputRequired()])

#     first_name = StringField("first_name", validators=[InputRequired()])

#     last_name = StringField("last_name", validators=[InputRequired()])


# class LoginForm(FlaskForm):
#     """Form to login"""

#     username = StringField("username", validators=[InputRequired()])

#     password = StringField("password", validators=[InputRequired()])


# class FeedbackForm(FlaskForm):
#     """Add feedback form."""

#     title = StringField(
#         "Title",
#         validators=[InputRequired(), Length(max=100)],
#     )
#     content = StringField(
#         "Content",
#         validators=[InputRequired()],
#     )

# class DeleteForm(FlaskForm):
#     """Delete form -- this form is intentionally blank."""

"""Forms for flask-feedback."""

from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )


class RegisterForm(FlaskForm):
    """User registration form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Length(max=50)],
    )
    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
    )


class FeedbackForm(FlaskForm):
    """Add feedback form."""

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=100)],
    )
    content = StringField(
        "Content",
        validators=[InputRequired()],
    )


class DeleteForm(FlaskForm):
    """Delete form -- this form is intentionally blank."""
