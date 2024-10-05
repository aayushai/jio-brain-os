import grpc
import json
from typing import Dict, List
import os
from test.utils.config import *
from .config import filename
from jio.brain.proto.knowledge.api.data.add_entity_alias_pb2 import AddEntityAliasRequest
from jio.brain.proto.knowledge.api.data.add_entity_alias_pb2_grpc import AddEntityAliasServiceStub
from jio.brain.proto.knowledge.base.language_pb2 import Language

from logs.log import get_logger

logger = get_logger("root", "add_entity_alias")
channel = grpc.insecure_channel(add_entity_alias_channel)
stub = AddEntityAliasServiceStub(channel)

curr_dir = os.path.dirname(os.path.realpath(__file__))#fetching current directory
test_data_file = os.path.join(curr_dir,filename)

#read_json_file function is used to read_json file and convert it to dictionary
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
alias = test_data["alias"]
canonical_name = test_data["canonical_name"]
language = test_data["language"]


#This is the test service of KG that can be added to JioFabric
def test(request):
	
	response = stub.serve(request)

	return response

def test_add_entity_alias(entity_id, alias, language, canonical_name):	
    logger.debug("entered test method")
    
    try:
        entity_id=entity_id
        alias = alias
        language = Language(
            language = language,
        )
        
        request = AddEntityAliasRequest(
            entity_id = entity_id,
            language = language,
            alias = alias,
            canonical_name = canonical_name
            )
        print(request)
        test_response = test(request)
        logger.info("Testing completed")
        return test_response
        
    except Exception as e:
        logger.error(e)
        return str(e)


if __name__ == "__main__":
    api_response = test_add_entity_alias(entity_id, alias, language, canonical_name)
    print(api_response)




