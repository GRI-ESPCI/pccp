from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FileField, BooleanField
from wtforms.validators import (
    DataRequired,
    Length,
    Optional
)

from pccp.extensions import db
from pccp.frontend.models import Projet, IndexContent

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

class IndexContentModelForm(BaseModelForm):
    class Meta:
        model = IndexContent

    @classmethod
    def get_session(self):
        return db.session

class IndexContentForm(IndexContentModelForm):
    submit = SubmitField(
        "Valider"
    )