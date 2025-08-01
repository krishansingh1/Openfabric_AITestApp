from dataclasses import dataclass
from marshmallow import Schema, fields, post_load

from openfabric_pysdk.fields import Resource
from openfabric_pysdk.utility import SchemaUtil


################################################################
# Output concept class - AUTOGENERATED
################################################################
@dataclass
class OutputClass:
    def __init__(self):
        self.message = ""
        self.image_path = ""
        self.model_3d = ""


################################################################
# OutputSchema concept class - AUTOGENERATED
################################################################
class OutputClassSchema(Schema):
    message = fields.Str(required=True)
    image_path = fields.Str(required=True)
    model_3d = fields.Str(required=True)

    @post_load
    def create(self, data, **kwargs):
        return SchemaUtil.create(OutputClass(), data)
