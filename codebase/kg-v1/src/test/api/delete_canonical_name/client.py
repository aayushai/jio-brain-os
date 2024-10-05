import grpc
import json
import os
from typing import Dict
from .config import *
from jio.brain.proto.knowledge.api.data.delete_canonical_name_pb2 import DeleteCanonicalNameRequest
from jio.brain.proto.knowledge.api.data.delete_canonical_name_pb2_grpc import DeleteCanonicalNameServiceStub
from jio.brain.proto.knowledge.base.language_pb2 import Language
from jio.brain.proto.entity.entity_pb2 import BrainEntityName
from logs.log import get_logger

curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
language = test_data["language"]["language"]
canonical = test_data["entity_name"]["canonical"]
alias = list(test_data["entity_name"]["aliases"].keys())[0]

logger = get_logger("root", "delete_canonical_name")
channel = grpc.insecure_channel(delete_canonical_name_channel)
stub = DeleteCanonicalNameServiceStub(channel)
def test(request):
	response = stub.serve(request)
	return response

def test_delete_canonical_name(entity_id, language, canonical, alias):
    logger.debug("entered test method")
    try:        
        element = { "%s"%alias: True }

        request = DeleteCanonicalNameRequest(
            entity_id  = entity_id,
            language = Language(
                language = language
            ),
            entity_name = BrainEntityName (
                canonical = canonical,
                aliases = {
                    "element": element
                }
            )
        )

        test_response = test(request)
        logger.info("Testing completed")
        return test_response
        
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_delete_canonical_name(entity_id, language,  canonical, alias)
    print(api_response)