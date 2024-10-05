import grpc
import json
from typing import Dict, List
import os
from jio.brain.proto.knowledge.api.data.update_canonical_name_pb2 import UpdateCanonicalNameRequest
from jio.brain.proto.knowledge.api.data.update_canonical_name_pb2_grpc import UpdateCanonicalNameServiceStub
from test.utils.config import *
from jio.brain.proto.knowledge.base.language_pb2 import Language
from logs.log import get_logger

channel = grpc.insecure_channel(update_canonical_name_channel)
stub = UpdateCanonicalNameServiceStub(channel)

logger = get_logger("root", "update_canonical_name")

curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)

def read_json_file(file:str) -> Dict:
    with open(file) as f:
        data = json.load(f)
    return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
old_canonical_name = test_data["old_canonical_name"]
new_canonical_name = test_data["new_canonical_name"]
language = test_data["language"]


def test_update_canonical_name(entity_id, old_canonical_name, new_canonical_name, language):
    logger.debug(TEST_STARTED)
    try:
        request =  UpdateCanonicalNameRequest(
            entity_id = entity_id,
            old_canonical_name = old_canonical_name,
            new_canonical_name = new_canonical_name,
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
    api_response = test_update_canonical_name(entity_id, old_canonical_name, new_canonical_name, language)
    print(api_response)    
  