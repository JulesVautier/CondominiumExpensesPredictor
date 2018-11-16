from flask import request
from flask.json import jsonify
from app import flask_app
from app import ma
from app import dataHelper
from app.DataSchema import data_schema
from marshmallow import ValidationError


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
    data = request.get_json()
    try:
        data_schema.validate(data)
    except ValidationError as err:
        print('error', err.messages)
        return jsonify(err)
    res = data_schema.load(data)
    if res.errors:
        return jsonify(res.errors)
    return jsonify(dataHelper.postData(res.data))

@flask_app.route("/data/predict", methods=['POST'])
def predict():
    data = request.get_json()
    try:
        data_schema.validate(data)
    except ValidationError as err:
        print('error', err.messages)
        return jsonify(err)
    res = data_schema.load(data)
    if res.errors:
        return jsonify(res.errors)
    return jsonify(dataHelper.predict(res.data))


@flask_app.route("/data/train")
def train():
    return jsonify(dataHelper.train())


@flask_app.route("/data/clean")
def clean():
    return jsonify(dataHelper.clean())


@flask_app.route("/data/createTrainSet")
def createTrainSet():
    return jsonify(dataHelper.createTrainSet())


@flask_app.route("/data/trainAll")
def trainAll():
    return jsonify(dataHelper.trainAll())

@flask_app.route("/data/isTrained")
def isTrained():
    return jsonify(dataHelper.isTrainedfct())

@flask_app.route("/data/trainResults")
def getTrainResult():
    return jsonify(dataHelper.getTrainResult())

