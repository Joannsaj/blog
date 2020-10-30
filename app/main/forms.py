from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class OpinionForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    opinion = TextAreaField('What is your opinion?', validators=[Required()])
    submit = SubmitField('Submit')
