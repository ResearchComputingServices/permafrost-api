#
# Specific view.
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from flask import request, jsonify, url_for, Blueprint
from flask import json, jsonify, Response, blueprints
from permafrost_api.models.overly_map import OverlyMap, OverlyMapSchema
from permafrost_api.extensions import db, ma
from permafrost_api.web.common_view import permafrost_bp
from permafrost_api.decorators.crossorigin import crossdomain
from permafrost_api.decorators.authorization import authorization

overly_map_schema = OverlyMapSchema(many=False)
overly_map_schema_many = OverlyMapSchema(many=True)

@permafrost_bp.route("/overly_maps")
@crossdomain(origin='*')
@authorization
def get_overly_maps():
    properties = OverlyMap.query.all()
    result = overly_map_schema_many.dump(properties)
    return jsonify(result)

@permafrost_bp.route("/overly_maps", methods=['POST'])
@crossdomain(origin='*')
@authorization
def add_overly_map():
    # Insert a new overly_map
    data = request.get_json()
    overly_map = OverlyMap(data)
    db.session.add(overly_map)
    db.session.commit()

    # Return the inserted overly_map
    result = overly_map_schema.dump(overly_map)
    return jsonify(result)

@permafrost_bp.route("/overly_maps", methods=['PUT'])
@crossdomain(origin='*')
@authorization
def update_overly_map():
    data = request.get_json()
    overly_map = OverlyMap.query.filter_by(title=data.get('title')).first()
    if overly_map:
        overly_map.active = data.get('active')
        overly_map.image = data.get('image')
        overly_map.north_east_lat = data.get('north_east_lat')
        overly_map.north_east_lng = data.get('north_east_lng')
        overly_map.south_west_lat = data.get('south_west_lat')
        overly_map.south_west_lng = data.get('south_west_lng')
        db.session.commit()
        response = Response(json.dumps(data), 200, mimetype="application/json")
    else:
        response = Response(json.dumps(data), 404, mimetype="application/json")

    return response

@permafrost_bp.route("/overly_maps/active", methods=['PUT'])
@crossdomain(origin='*')
@authorization
def update_active_overly_map():
    data = request.get_json()
    overly_map = OverlyMap.query.filter_by(title=data.get('title')).first()
    if overly_map:
        overly_map.active = data.get('active')
        db.session.commit()
        response = Response(json.dumps(data), 200, mimetype="application/json")
    else:
        response = Response(json.dumps(data), 404, mimetype="application/json")

    return response

@permafrost_bp.route("/overly_maps", methods=['DELETE'])
@crossdomain(origin='*')
@authorization
def delete_overly_map():
    data = request.get_json()
    overly_map = OverlyMap.query.filter_by(title=data.get('title')).first()
    if overly_map:
        db.session.delete(overly_map)
        db.session.commit()
        response = Response(json.dumps(data), 200, mimetype="application/json")
    else:
        response = Response(json.dumps(data), 404, mimetype="application/json")

    return response
