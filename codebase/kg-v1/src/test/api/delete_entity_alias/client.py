import grpc
import json
from typing import Dict, List
import os
from jio.brain.proto.knowledge.api.data.delete_entity_alias_pb2 import DeleteEntityAliasRequest
from jio.brain.proto.knowledge.api.data.delete_entity_alias_pb2_grpc import DeleteEntityAliasServiceStub
from test.utils.config import *
from jio.brain.proto.knowledge.base.language_pb2 import Language
from logs.log import get_logger

channel = grpc.insecure_channel(delete_entity_alias_channel)
stub = DeleteEntityAliasServiceStub(channel)

logger = get_logger("root", "delete_entity_alias")

curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)

def read_json_file(file:str) -> Dict:
    with open(file) as f:
        data = json.load(f)
    return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
alias = test_data["alias"]
language = test_data["language"]


def test_delete_entity_alias(entity_id, alias, language):
    logger.debug(TEST_STARTED)
    try:
        request =  DeleteEntityAliasRequest(
            entity_id = entity_id,
            alias = alias,
            language = Language (
                language = language,
            )
        )
        
        response = stub.serve(request)
        logger.info(TEST_COMPLETED)
        return response
        
    except Exception as e:
        logger.error(e)
        return str(e)


if __name__ == "__main__":
    api_response = test_delete_entity_alias(entity_id, alias, language)
    print(api_response)    
  