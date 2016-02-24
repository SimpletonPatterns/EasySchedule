# -*- coding: utf-8 -*-
#
#

from flask import request, render_template, flash, Blueprint
from model import User
from database import db
import json

# For the Form
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Regexp
from wtforms_alchemy import ModelForm



blueprint = Blueprint('easyschedule', __name__, template_folder='templates')


class UserForm(ModelForm, Form):
    """Handle subscribe form neatly with WTForms."""
    class Meta:
        model = User

    ualogin = StringField(u'UA Login', validators=[DataRequired()])
    email = StringField(u'Email', validators=[Email(), DataRequired()])


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Show something."""
    return render_template('home.html')
