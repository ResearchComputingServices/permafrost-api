#
# Specific view.
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from flask import request, jsonify, url_for, Blueprint
from flask import json, jsonify, Response, blueprints
from permafrost_api.models.settings import Settings, SettingsSchema
from permafrost_api.extensions import db, ma
from permafrost_api.web.common_view import permafrost_bp
from permafrost_api.decorators.crossorigin import crossdomain
from permafrost_api.decorators.authorization import authorization

settings_schema_one = SettingsSchema(many=False)
settings_schema_many = SettingsSchema(many=True)

@permafrost_bp.route("/settings")
@crossdomain(origin='*')
@authorization
def get_settings():
    properties = Settings.query.all()
    result = settings_schema_many.dump(properties)
    return jsonify(result)

@permafrost_bp.route("/settings", methods=['PUT'])
@crossdomain(origin='*')
@authorization
def update_settings():
    json_request = request.get_json()
    category = json_request[0].get('category')
    value = json_request[0].get('value')
    type = json_request[0].get('type')

    settings = Settings.query.filter(Settings.category==category).first()
    if settings:
        settings.value = json_request[0].get('value')
        settings.type = json_request[0].get('type')
        db.session.commit()

    result = settings_schema_one.dump(settings)
    return jsonify(result)
