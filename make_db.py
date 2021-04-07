#
# Create database schema based on the model specification.
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from permafrost_api.extensions import db, ma
from permafrost_api import permafrost_factory
from permafrost_api.models.marker import Marker, MarkerSchema

app = permafrost_factory.create_app(__name__)

with app.app_context():
    db.engine.execute("drop schema if exists public cascade")
    db.engine.execute("create schema public")

    db.reflect()
    db.drop_all()
    db.create_all()

    db.session.commit()
