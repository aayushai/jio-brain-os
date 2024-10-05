import grpc
import os
import json
from typing import Dict, List
from jio.brain.proto.knowledge.api.data.get_all_entity_ids_using_biz_id_pb2 import GetAllEntityIdsUsingBizIdRequest
from jio.brain.proto.knowledge.api.data.get_all_entity_ids_using_biz_id_pb2_grpc import GetAllEntityIdsUsingBizIdServiceStub
from jio.brain.proto.knowledge.base.biz_id_pb2 import BizId
from logs.log import get_logger
from .config import *

logger = get_logger("root", "get_all_entity_ids_using_biz_id")

channel = grpc.insecure_channel(get_all_entity_ids_using_biz_id_channel)
stub = GetAllEntityIdsUsingBizIdServiceStub(channel)


curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)

collection_name = test_data["collection_name"]
biz_id = test_data["bizId"]


def test(request):
	response = stub.serve(request)
	return response

def test_get_all_entity_ids_using_biz_id(collection_name, biz_id):
    logger.debug("entered test method")

    try:
        request = GetAllEntityIdsUsingBizIdRequest(
			collection_name = collection_name,
			biz_id =  biz_id
		)
        test_response = test(request)
        logger.info("Testing completed")
        return test_response
		
    except Exception as e:
        return str(e)
	
		
if __name__ == "__main__":
	api_reponse = test_get_all_entity_ids_using_biz_id(collection_name, biz_id)
	print(api_reponse)
