import grpc
import os
import json
from typing import Dict
from .config import *
from jio.brain.proto.knowledge.api.data.delete_bizid_pb2 import DeleteBizIdRequest
from jio.brain.proto.knowledge.api.data.delete_bizid_pb2_grpc import DeleteBizIdServiceStub
from jio.brain.proto.knowledge.base.biz_id_pb2 import BizId
from logs.log import get_logger

curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
biz_id = test_data["bizId"]

logger = get_logger("root", "delete_bizid")
channel = grpc.insecure_channel(delete_bizid_channel)
stub = DeleteBizIdServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response

def test_delete_bizid(entity_id, biz_id):
	logger.debug("entered test method")
	try:
		request = DeleteBizIdRequest(
			entity_id = entity_id,
			biz_id =  biz_id
		)
		test_response = test(request)
		logger.info("Testing completed")
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
    api_response = test_delete_bizid(entity_id, biz_id)
    print(api_response)