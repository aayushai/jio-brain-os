import os
import json
import grpc
from typing import Dict, List
from google.protobuf import json_format 
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.add_attribute_pb2 import AddAttributeRequest
from jio.brain.proto.knowledge.api.data.add_attribute_pb2_grpc import AddAttributeServiceStub
from jio.brain.proto.quantity.quantity_pb2 import BrainQuantity

curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file, encoding="utf8") as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)

logger = get_logger("root", "add_attribute")

channel = grpc.insecure_channel(add_attribute_channel)

stub = AddAttributeServiceStub(channel)

def test(request):
	response = stub.serve(request)
	return response

def test_add_attribute(entity_id, attribute_name, attribute):
	logger.debug(TEST_STARTED)
	try:
		request = AddAttributeRequest(
			entity_id = entity_id,
			attribute_name = attribute_name,
			attribute_value = attribute_val
		)
		
		test_response = test(request)
		logger.info(TEST_COMPLETED)
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)
		

if __name__ == "__main__":
	collection_name = test_data["entity_id"]
	attribute_name = test_data["attribute_name"]
	attribute = test_data["attribute"]
	attribute_val = json_format.Parse(json.dumps(attribute), BrainQuantity())		
	api_response = test_add_attribute(collection_name, attribute_name, attribute_val)
	print(api_response)







