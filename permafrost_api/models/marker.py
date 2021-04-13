#
# Marker model
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from pprint import pformat

from marshmallow import Schema, fields, ValidationError, pre_load
from sqlalchemy import func, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from permafrost_api.extensions import db, ma

class Marker(db.Model):
    __tablename__ = 'Markers'

    text = db.Column(db.String(), primary_key=True)
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())
    state = db.Column(db.String())

    def __init__(self, marker):
        self.text = marker.get('text')
        self.lat = marker.get('lat')
        self.lng = marker.get('lng')
        self.state = marker.get('state')

    def __repr__(self):
        return '<marker %r>' % self.name

class MarkerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marker

    text = fields.String(dump_only=True)
    lat = fields.Float()
    lng = fields.Float()
    state = fields.String()
