import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.delete_entity_pb2 import DeleteEntityRequest
from jio.brain.proto.knowledge.api.data.delete_entity_pb2_grpc import DeleteEntityServiceStub

logger = get_logger("root", "delete_entity")

channel = grpc.insecure_channel(delete_entity_channel)

stub = DeleteEntityServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_delete_entity(entity):

    logger.debug(TEST_STARTED)
    try:
        request = DeleteEntityRequest(
            entity_id = entity
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_delete_entity("schema_vertical/common")
    print(api_response)    
