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
from flask import send_file

@permafrost_bp.route("/get_image", methods=['GET'])
@crossdomain(origin='*')
@authorization
def get_image():
    name = request.args.get('name')
    if name:
        return send_file("images/" + name, mimetype='image/gif', cache_timeout=-1)
    return Response(json.dumps([]), 404, mimetype="application/json")
