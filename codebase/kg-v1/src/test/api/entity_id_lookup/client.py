import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.entity_id_lookup_pb2 import EntityIdLookupRequest
from jio.brain.proto.knowledge.api.data.entity_id_lookup_pb2_grpc import EntityIdLookupServiceStub

logger = get_logger("root", "entity_id_lookup")

channel = grpc.insecure_channel(entity_id_lookup_channel)

stub = EntityIdLookupServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_entity_id_lookup(key, id):

    logger.debug(TEST_STARTED)
    try:
        request = EntityIdLookupRequest(
            key = key,
            id = id
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_entity_id_lookup("healthcare_entity", "546423964")
    print(api_response)    
