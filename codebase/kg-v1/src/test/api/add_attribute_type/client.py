import grpc
import os
import json
from typing import Dict
from .config import *
from google.protobuf.struct_pb2 import Struct
from jio.brain.proto.knowledge.api.schema.add_attribute_type_pb2 import AddAttributeTypeRequest
from jio.brain.proto.knowledge.api.schema.add_attribute_type_pb2_grpc import AddAttributeTypeServiceStub


curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)

collection_type = test_data["collection_type"]
attribute_name = test_data["attribute_name"]
attribute_required = test_data["attribute_required"]
attribute_schema = test_data["attribute_schema"] 

channel = grpc.insecure_channel(add_attribute_type_channel)
stub = AddAttributeTypeServiceStub(channel)
def test(request_proto):
    response = stub.serve(request_proto)
    return response

#get_struct function takes schema_dictionary as input and converts it to google.protobuf.Struct format
def get_struct(schema_dict):
    s = Struct()
    s.update(schema_dict)
    return s

def test_add_attribute_type(collection_type, attribute_name, attribute_schema, attribute_required):    
    request_proto = AddAttributeTypeRequest(
        collection_type = collection_type,
        attribute_name = attribute_name,
        attribute_schema = get_struct(attribute_schema),
        attribute_required = attribute_required
    )
    print(attribute_schema)
    test_response = test(request_proto)
    return test_response


if __name__ == "__main__":
    api_response = test_add_attribute_type(collection_type, attribute_name, attribute_schema, attribute_required)
    print(api_response)