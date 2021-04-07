#
# OverlyMap model
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from marshmallow import Schema, fields, ValidationError, pre_load
from permafrost_api.extensions import db, ma

class OverlyMap(db.Model):
    __tablename__ = 'OverlyMap'

    title = db.Column(db.String(), primary_key=True)
    south_west_lat = db.Column(db.Float())
    south_west_lng = db.Column(db.Float())
    north_east_lat = db.Column(db.Float())
    north_east_lng = db.Column(db.Float())
    image = db.Column(db.String())
    active = db.Column(db.Boolean())

    def __init__(self, overly_map):
        self.title = overly_map.get('title')
        self.south_west_lat = overly_map.get('south_west_lat')
        self.south_west_lng = overly_map.get('south_west_lng')
        self.north_east_lat = overly_map.get('north_east_lat')
        self.north_east_lng = overly_map.get('north_east_lng')
        self.image = overly_map.get('image')
        self.active = overly_map.get('active')

    def __repr__(self):
        return '<overly_map %r>' % self.name

class OverlyMapSchema(ma.ModelSchema):
    class Meta:
        model = OverlyMap

    title = fields.String(dump_only=True)
    south_west_lat = fields.Float()
    south_west_lng = fields.Float()
    north_east_lat = fields.Float()
    north_east_lng = fields.Float()
    image = fields.String()
    active = fields.Boolean()
