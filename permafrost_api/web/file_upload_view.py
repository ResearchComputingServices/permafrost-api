#
# Specific view.
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

import io
from flask import request, jsonify, abort,render_template,request,redirect,url_for, json, Response, send_file
from werkzeug import secure_filename
import os
from permafrost_api.web.common_view import permafrost_bp
from permafrost_api.decorators.crossorigin import crossdomain
from permafrost_api.decorators.authorization import authorization

def download_file(fullpath, filename):
    with open(fullpath, 'rb') as binary:
        return send_file(
            io.BytesIO(binary.read()),
            attachment_filename=filename,
            as_attachment=True,
            mimetype="application/binary")
    return Response(json.dumps([]), 404, mimetype="application/json")

@permafrost_bp.route("/file_upload", methods=['POST'])
@crossdomain(origin='*')
@authorization
def file_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            folder = 'file_upload'
            filename = secure_filename(file.filename)
            if not os.path.exists(folder):
                os.makedirs(folder)
            fullpath = os.path.join(folder, filename)
            file.save(fullpath)
            os.system("python ./permafrost_api/providers/process_file.py " + fullpath)
            return Response(json.dumps([]), 201, mimetype="application/json")
    return Response(json.dumps([]), 404, mimetype="application/json")

@permafrost_bp.route("/get_file", methods=['GET'])
@crossdomain(origin='*')
@authorization
def get_file():
    filename = request.args.get('name')
    fullpath = "file_upload/" + filename
    if filename:
        return download_file(fullpath, filename)
    return Response(json.dumps([]), 404, mimetype="application/json")

