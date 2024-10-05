import grpc
import os
import json
from typing import Dict
from .config import *
from jio.brain.proto.knowledge.api.schema.add_collection_type_pb2 import AddCollectionTypeRequest
from jio.brain.proto.knowledge.api.schema.add_collection_type_pb2_grpc import AddCollectionTypeServiceStub
from google.protobuf.struct_pb2 import Struct
from logs.log import get_logger

curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)

logger = get_logger("root", "add_collection_type")
channel = grpc.insecure_channel(add_collection_type_channel)
stub = AddCollectionTypeServiceStub(channel)

def test(request):
	response = stub.serve(request)
	return response

#get_struct function takes schema_dictionary as input and converts it to google.protobuf.Struct format
def get_struct(schema_dict):
	s = Struct()
	s.update(schema_dict)
	return s

def test_add_collection_type(vertical, collection_name, is_predicate, collection_schema):
	logger.debug(TEST_STARTED)
	try:
		request = AddCollectionTypeRequest(
			vertical = vertical, #common
			collection_name = collection_name,#person
			is_predicate = is_predicate, #True/False
			schema = get_struct(collection_schema)
			)
		
		test_response = test(request)
		
		logger.info(TEST_COMPLETED)
		return test_response

	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
	api_response = test_add_collection_type(test_data["vertical"], test_data["collection_name"], test_data["is_predicate"], test_data["attribute_schema"])
	print(api_response)