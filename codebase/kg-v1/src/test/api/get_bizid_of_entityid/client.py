import grpc
import json
from typing import Dict, List
import os
from jio.brain.proto.knowledge.api.data.get_bizid_of_entityid_pb2 import GetBizidOfEntityidRequest
from jio.brain.proto.knowledge.api.data.get_bizid_of_entityid_pb2_grpc import GetBizidOfEntityidServiceStub
from jio.brain.proto.knowledge.base.language_pb2 import Language
from test.utils.config import *
from logs.log import get_logger

channel = grpc.insecure_channel(get_bizid_of_entityid_channel)
stub = GetBizidOfEntityidServiceStub(channel)

logger = get_logger("root", "get_bizid_of_entityid")

curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)

def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
biz_id_type = test_data["biz_id_type"]


def test_get_bizid_of_entityid(entity_id,biz_id_type):
    logger.debug(TEST_STARTED)
    try:
        request = GetBizidOfEntityidRequest(
            entity_id = entity_id,
            biz_type = biz_id_type
        )
        
        response = stub.serve(request)
        logger.info(TEST_COMPLETED)
        return response
        
    except Exception as e:
        logger.error(e)
        return str(e)


if __name__ == "__main__":
	api_response = test_get_bizid_of_entityid(entity_id, biz_id_type)
	print(api_response)    
  