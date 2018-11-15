from flask import request
from flask.json import jsonify
from app import flask_app
from app import ma
from app import dataHelper


@flask_app.route("/")
def HelloWorld():
    return 'hello world'


@flask_app.route("/datas", methods=['GET'])
def getDatas():
    limit_one = request.args.get('limite_one', default=None, type=int)
    limit_two = request.args.get('limite_two', default=None, type=int)
    resp = dataHelper.getDatas(limit_one, limit_two)
    return jsonify(resp)


@flask_app.route("/data/<int:id>", methods=['GET'])
def getData(id):
    resp = dataHelper.getData(id)
    return jsonify(resp)

@flask_app.route("/data/<int:id>", methods=['DELETE'])
def deleteData(id):
    resp = dataHelper.deleteData(id)
    return jsonify(resp)

@flask_app.route("/data", methods=['POST'])
def postOneRow():
    pass