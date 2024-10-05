import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_entities_instance_pb2 import GetEntitiesInstanceRequest
from jio.brain.proto.knowledge.api.data.get_entities_instance_pb2_grpc import GetEntitiesInstanceServiceStub

logger = get_logger("root", "get_entities_instance")

channel = grpc.insecure_channel(get_entities_instance_channel)

stub = GetEntitiesInstanceServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_entities_instance(entity, limit):

    logger.debug(TEST_STARTED)
    try:
        request = GetEntitiesInstanceRequest(
            entity_type = entity,
            limit = limit,
            page_size = 5,
            page_token = "2"
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_entities_instance("common_person123", 5)
    print(api_response)    
