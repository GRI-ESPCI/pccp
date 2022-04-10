from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FileField
from wtforms.validators import (
    DataRequired,
    Length,
    Optional
)

from pccp.frontend.models import Projet

BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    class Meta:
        model = Projet

    @classmethod
    def get_session(self):
        return db.session

class ProjetForm(ModelForm):
    cover_img = FileField("Image de couverture")
    thumbnail = FileField("Vignette")
    submit = SubmitField(
        "Valider"
    )