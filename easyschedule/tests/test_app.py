# -*- coding: utf-8 -*-
#
#

from flask import url_for
from easyschedule.model import User as U


def test_user_insert(session):
    """Test the User insertion."""
    u = U('ualogin',
          'email')
    session.add(u)
    assert U.query.count() == 1
