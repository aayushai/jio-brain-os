import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_entity_pb2 import GetEntityRequest
from jio.brain.proto.knowledge.api.data.get_entity_pb2_grpc import GetEntityServiceStub

logger = get_logger("root", "get_entity")

channel = grpc.insecure_channel(get_entity_channel)

stub = GetEntityServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_entity(entity):

    logger.debug(TEST_STARTED)
    try:
        request = GetEntityRequest(
            entity_id = entity
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_entity("common_person123")
    print(api_response)    
