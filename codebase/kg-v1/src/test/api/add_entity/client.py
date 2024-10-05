import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from google.protobuf import json_format 
from jio.brain.proto.knowledge.base.entity_pb2 import Entity
from jio.brain.proto.knowledge.api.data.add_entity_pb2 import AddEntityRequest
from jio.brain.proto.knowledge.api.data.add_entity_pb2_grpc import AddEntityServiceStub

curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file, encoding="utf8") as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)

logger = get_logger("root", "add_entity")

channel = grpc.insecure_channel(add_entity_channel)

stub = AddEntityServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_add_entity(entity):

    logger.debug(TEST_STARTED)
    try:
        request = AddEntityRequest(
            entity = entity
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_add_entity(json_format.Parse(json.dumps(test_data), Entity()))
    print(api_response)    
