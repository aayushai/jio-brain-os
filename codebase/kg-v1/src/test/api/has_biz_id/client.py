import grpc
import os
import json
from typing import Dict, List
from jio.brain.proto.knowledge.api.data.has_biz_id_pb2 import HasBizIdRequest
from jio.brain.proto.knowledge.api.data.has_biz_id_pb2_grpc import HasBizIdServiceStub
from test.api.has_biz_id.config import *
from logs.log import get_logger

logger = get_logger("root", "has_biz_id")

channel = grpc.insecure_channel(has_biz_id_channel)
stub = HasBizIdServiceStub(channel)

curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)

entity_id = test_data["entity_id"]
biz_id = test_data["biz_id"]
def test(request):
    response = stub.serve(request)
    return response

#This is the test service of KG that can be added to JioFabric
def test_has_biz_id(entity_id, biz_id):
	logger.debug("entered test method")
	try:
		request = HasBizIdRequest(
			entity_id = entity_id,
      		biz_id = biz_id
		)

		test_response = test(request)
		
		logger.info("Testing completed")
		
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
	api_response = test_has_biz_id(entity_id, biz_id)
	print(api_response)    

