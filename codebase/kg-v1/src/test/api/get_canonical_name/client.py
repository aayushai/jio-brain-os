import grpc
import json
from typing import Dict, List
import os
from jio.brain.proto.knowledge.api.data.get_canonical_name_pb2 import GetCanonicalNameRequest
from jio.brain.proto.knowledge.api.data.get_canonical_name_pb2_grpc import GetCanonicalNameServiceStub
from jio.brain.proto.knowledge.base.language_pb2 import Language
from test.api.get_canonical_name.config import *
from logs.log import get_logger

channel = grpc.insecure_channel(get_canonical_name_channel)
stub = GetCanonicalNameServiceStub(channel)
logger = get_logger("root", "get_canonical_name")
curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)
#read_json_file function is used to read_json file and convert it to dictionary
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
language = test_data["language"]


def test_get_canonical_name(entity_id,language):
    logger.debug("entered test method")
    try:
        request = GetCanonicalNameRequest(
            entity_id = entity_id,
            language = Language(
                language = language,
            )
        )
        
        response = stub.serve(request)
        logger.info("Testing completed")
        return response
        
    except Exception as e:
        logger.error(e)
        return str(e)


if __name__ == "__main__":
	api_response = test_get_canonical_name(entity_id, language)
	print(api_response)    
  

	







