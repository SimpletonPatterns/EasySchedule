# -*- coding: utf-8 -*-
#
# 

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

db = SQLAlchemy()
session = scoped_session(sessionmaker())
