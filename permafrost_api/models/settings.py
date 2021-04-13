#
# Settings model
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from pprint import pformat

from marshmallow import Schema, fields, ValidationError, pre_load
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import relationship
from permafrost_api.extensions import db, ma

class Settings(db.Model):
    __tablename__ = 'Settings'

    category = db.Column(db.String(), primary_key=True)
    value = db.Column(db.String())
    type = db.Column(db.String())

    def __init__(self, settings):
        self.category = settings.get('category')
        self.value = settings.get('value')
        self.type = settings.get('zoom')

    def __repr__(self):
        return '<settings %r>' % self.name

class SettingsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Settings

    category = fields.String(dump_only=True)
    value = fields.String()
    type = fields.String()
