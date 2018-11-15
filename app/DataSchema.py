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
    ID =            fields.Integer(required=True)
    AD_URLS =       fields.String(required=False)
    PROPERTY_TYPE = fields.String(required=False)
    DEPT_CODE =     fields.Integer(required=False)
    ZIP_CODE =      fields.Integer(required=False)
    CITY =          fields.String(required=False)
    INSEE_CODE =    fields.Integer(required=False)
    LATITUDE =      fields.Float(required=False)
    LONGITUDE =     fields.Float(required=False)
    BLUR_RADIUS =   fields.Float(required=False)
    MARKETING_TYPE =fields.String(required=False)
    PRICE =         fields.Integer(required=False)
    DESCRIPTION =   fields.String(required=False)
    SURFACE =       fields.Float(required=False)
    CONDOMINIUM_EXPENSES = fields.Float(required=False)
    CARETAKER =     fields.Float(required=False)
    HEATING_MODE =  fields.String(required=False)
    WATER_HEATING_MODE = fields.Float(required=False)
    ELEVATOR =      fields.Float(required=False)
    FLOOR =         fields.Float(required=False)
    FLOOR_COUNT =   fields.Float(required=False)
    LOT_COUNT =     fields.Float(required=False)
    CONSTRUCTION_YEAR = fields.Float(required=False)
    BUILDING_TYPE = fields.Float(required=False)
    PARKING =       fields.String(required=False)
    PARKING_COUNT = fields.Float(required=False)
    TERRACE =       fields.Float(required=False)
    TERRACE_SURFACE = fields.Float(required=False)
    SWIMMING_POOL = fields.Float(required=False)
    GARDEN =        fields.Float(required=False)
    STANDING =      fields.Float(required=False)
    NEW_BUILD =     fields.Boolean(required=False)
    SMALL_BUILDING = fields.Float(required=False)
    CORNER_BUILDING = fields.Float(required=False)
    PUBLICATION_START_DATE = fields.Float(required=False)
    DEALER_NAME =   fields.Float(required=False)
    DEALER_TYPE =   fields.Float(required=False)
    REFERENCE_NUMBER = fields.String(required=False)
    ENERGY_CLASSIFICATION = fields.String(required=False)
    ordered = False

data_schema = DataSchema()
datas_schema = DataSchema(many=True)

# class UserSchema(ma.Schema):
#     name = fields.fields.String(required=False)(required=True)
#     age = fields.fields.Integer(required=True)
#     ID = fields.fields.Integer(required=True)
#
# result = UserSchema().load({'age': 42, 'ID':1}, partial=('name',))
# print(result)