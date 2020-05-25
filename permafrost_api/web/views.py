#
# Main entry point for all views.
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from flask import request, jsonify, url_for, Blueprint
from flask import json, jsonify, Response, blueprints
from permafrost_api.web.common_view import permafrost_bp
from permafrost_api.decorators.crossorigin import crossdomain
from permafrost_api.decorators.authorization import authorization
import permafrost_api.web.settings_view
import permafrost_api.web.marker_view
import permafrost_api.web.image_view
import permafrost_api.web.overly_map_view
import permafrost_api.web.file_upload_view

@permafrost_bp.route("/", methods=['GET'])
@crossdomain(origin='*')
@authorization
def hello():
    return "Hello World!"

