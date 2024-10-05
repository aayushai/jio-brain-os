import grpc
import os
import json
from typing import Dict, List
from jio.brain.proto.knowledge.api.data.has_any_biz_id_pb2 import HasAnyBizIdRequest
from jio.brain.proto.knowledge.api.data.has_any_biz_id_pb2_grpc import HasAnyBizIdServiceStub
from test.utils.config import *
from logs.log import get_logger

logger = get_logger("root", "has_any_biz_id")

channel = grpc.insecure_channel(has_any_biz_id_channel)
stub = HasAnyBizIdServiceStub(channel)

curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)

entity_id = test_data["entity_id"]

def test(request):
    response = stub.serve(request)
    return response

#This is the test service of KG that can be added to JioFabric
def test_has_any_biz_id(entity_id):
	logger.debug(TEST_STARTED)
	try:
		request = HasAnyBizIdRequest(
			entity_id = entity_id
		)

		test_response = test(request)
		
		logger.info(TEST_COMPLETED)
		
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
	api_response = test_has_any_biz_id(entity_id)
	print(api_response)    

