from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired
import datetime


class AssessmentForm(FlaskForm):
    title = StringField("Assessment Title", validators=[DataRequired()])
    module = StringField("Module Code", validators=[DataRequired()])
    description = TextAreaField("Description")
    dueDate = DateField("Date due", validators=[DataRequired()])
    dueTime = TimeField("Time due", default=datetime.time(0))