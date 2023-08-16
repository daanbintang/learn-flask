from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class Siswa(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    jurusan = StringField('Jurusan', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('submit')

