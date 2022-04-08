from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional
)

class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Email non valide")
        ]
    )
    password = PasswordField("Mot de passe", validators=[DataRequired()])
    submit = SubmitField("Se connecter")