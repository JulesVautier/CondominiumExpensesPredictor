import os

from flask_marshmallow import fields
from marshmallow import fields

from app import ma


def read_dtypes():
    fields = ()
    file = open("./ressources/types.txt", 'r')
    lines = file.readlines()
    for line in lines:
        fields = fields + (line.partition(' ')[0], )
    return fields


class DataSchema(ma.Schema):
    ID = fields.Integer(required=True)
    # Fields to expose
    fields = read_dtypes()

    ordered = False


data_schema = DataSchema()
datas_schema = DataSchema(many=True)

# class UserSchema(ma.Schema):
#     name = fields.String(required=True)
#     age = fields.Integer(required=True)
#     ID = fields.Integer(required=True)
#
# result = UserSchema().load({'age': 42, 'ID':1}, partial=('name',))
# print(result)