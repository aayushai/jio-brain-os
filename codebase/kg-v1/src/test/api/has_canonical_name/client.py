import grpc
import os
import json
from typing import Dict, List
from jio.brain.proto.knowledge.api.data.has_canonical_name_pb2 import HasCanonicalNameRequest
from jio.brain.proto.knowledge.api.data.has_canonical_name_pb2_grpc import HasCanonicalNameServiceStub
from test.api.has_canonical_name.config import *
from jio.brain.proto.knowledge.base.language_pb2 import Language
from logs.log import get_logger

channel = grpc.insecure_channel(has_canonical_name_channel)
stub = HasCanonicalNameServiceStub(channel)
logger = get_logger("root", "has_canonical_name")
curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)
#read_json_file function is used to read_json file and convert it to dictionary
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
canonical_name = test_data["canonical_name"]
language = test_data["language"]

def test(request):
    response = stub.serve(request)
    return response

#This is the test service of KG that can be added to JioFabric
def test_has_canonical_name(entity_id, language, canonical_name):
	logger.debug("entered test method")
	try:
		request = HasCanonicalNameRequest(
			entity_id = entity_id,
			language = Language(
				language = language
				),
			canonical_name = canonical_name
			)

		test_response = test(request)
		
		logger.info("Testing completed")
		
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
	api_response = test_has_canonical_name(entity_id, language, canonical_name)
	print(api_response)    









