from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    blog = TextAreaField('What is your opinion?', validators=[Required()])
    submit = SubmitField('Submit')
