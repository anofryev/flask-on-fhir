from fhirclient.models.codesystem import *
from fhirclient.models.namingsystem import NamingSystem

from flask_on_fhir.restful_resources import FHIRResource
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('code', type=str, required=False)
parser.add_argument('system', type=str, required=False)


class NamingSystemResource(FHIRResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def resource_type(cls) -> str:
        return NamingSystem.resource_type

