import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_alias_pb2 import GetAliasRequest
from jio.brain.proto.knowledge.api.data.get_alias_pb2_grpc import GetAliasServiceStub
from jio.brain.proto.knowledge.base.language_pb2 import Language

logger = get_logger("root", "get_alias")

channel = grpc.insecure_channel(get_alias_channel)
stub = GetAliasServiceStub(channel)

def test(request):
	
	response = stub.serve(request)

	return response
def test_get_alias(entity_id, language):
    logger.debug("entered test method")
    try:

        request = GetAliasRequest(
            entity_id = entity_id,
            language = Language(
                language = language,
            )
        )
        test_response = test(request)
        logger.info("Testing completed")
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)
    
if __name__ == "__main__":
    api_response = test_get_alias("common_person/12211", "english")
    print(api_response)    