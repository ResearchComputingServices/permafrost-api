#
# Specific view.
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from flask import request, jsonify, url_for, Blueprint
from flask import json, jsonify, Response, blueprints
from permafrost_api.models.marker import Marker, MarkerSchema
from permafrost_api.extensions import db, ma
from permafrost_api.web.common_view import permafrost_bp
from permafrost_api.decorators.crossorigin import crossdomain
from permafrost_api.decorators.authorization import authorization

marker_schema = MarkerSchema(many=False)
marker_schema_many = MarkerSchema(many=True)

@permafrost_bp.route("/markers")
@crossdomain(origin='*')
@authorization
def get_markers():
    properties = Marker.query.all()
    result = marker_schema_many.dump(properties)
    return jsonify(result[0])

@permafrost_bp.route("/markers", methods=['POST'])
@crossdomain(origin='*')
@authorization
def add_marker():
    # Insert a new marker
    data = request.get_json()
    marker = Marker(data)
    db.session.add(marker)
    db.session.commit()

    # Return the inserted marker
    result = marker_schema.dump(marker)
    return jsonify(result)

@permafrost_bp.route("/markers", methods=['PUT'])
@crossdomain(origin='*')
@authorization
def update_marker():
    data = request.get_json()
    marker = Marker.query.filter_by(text=data.get('text')).first()
    if marker:
        marker.lat = data.get('lat')
        marker.lng = data.get('lng')
        marker.state = data.get('state')
        db.session.commit()
        response = Response(json.dumps(data), 200, mimetype="application/json")
    else:
        response = Response(json.dumps(data), 404, mimetype="application/json")

    return response

@permafrost_bp.route("/markers", methods=['DELETE'])
@crossdomain(origin='*')
@authorization
def delete_marker():
    data = request.get_json()
    marker = Marker.query.filter_by(text=data.get('text')).first()
    if marker:
        db.session.delete(marker)
        db.session.commit()
        response = Response(json.dumps(data), 200, mimetype="application/json")
    else:
        response = Response(json.dumps(data), 404, mimetype="application/json")

    return response
