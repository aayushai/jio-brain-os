import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.search_entity_by_context_pb2 import SearchEntityByContextRequest
from jio.brain.proto.knowledge.api.data.search_entity_by_context_pb2_grpc import SearchEntityByContextServiceStub

logger = get_logger("root", "search_entity_by_context")

channel = grpc.insecure_channel(search_entity_by_context_channel)

stub = SearchEntityByContextServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_search_entity_by_context(entity_type, keyword, context_id):

    logger.debug(TEST_STARTED)
    try:
        request = SearchEntityByContextRequest(
            entity_type = entity_type,
            keyword = keyword,
            context_id = context_id
        )

        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_search_entity_by_context("symptom", "pain", 311)
    print(api_response)    
