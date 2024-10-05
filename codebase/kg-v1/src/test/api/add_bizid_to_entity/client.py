import grpc
import os
import json
from typing import Dict, List
from jio.brain.proto.knowledge.api.data.add_bizid_to_entity_pb2 import AddBizIdToEntityRequest
from jio.brain.proto.knowledge.api.data.add_bizid_to_entity_pb2_grpc import AddBizIdToEntityServiceStub
from jio.brain.proto.knowledge.base.biz_id_pb2 import BizId
from logs.log import get_logger
from .config import *

logger = get_logger("root", "add_bizid_to_entity")

channel = grpc.insecure_channel(add_bizid_to_entity_channel)
stub = AddBizIdToEntityServiceStub(channel)


curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)

entity_id = test_data["entity_id"]
biz_id_ = test_data["bizId"]


def test(request):
	response = stub.serve(request)
	return response

def test_add_bizid_to_entity(entity_id, biz_id_):
    logger.debug("entered test method")

    try:
        request = AddBizIdToEntityRequest(
			entity_id = entity_id,
			biz_id =  biz_id_    
		)

        test_response = test(request)
        logger.info("Testing completed")
        return test_response
		
    except Exception as e:
        return str(e)
	
		
if __name__ == "__main__":
	api_reponse = test_add_bizid_to_entity(entity_id, biz_id_)
	print(api_reponse)
