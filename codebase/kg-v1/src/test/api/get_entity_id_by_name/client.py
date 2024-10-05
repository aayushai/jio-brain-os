import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_entity_id_by_name_pb2 import GetEntityIdByNameRequest
from jio.brain.proto.knowledge.api.data.get_entity_id_by_name_pb2_grpc import GetEntityIdByNameServiceStub

logger = get_logger("root", "get_entity_id_by_name")

channel = grpc.insecure_channel(get_entity_id_by_name_channel)

stub = GetEntityIdByNameServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_entity_id_by_name(collection_name,entity_name):

    logger.debug(TEST_STARTED)
    try:
        request = GetEntityIdByNameRequest(
            collection_name = collection_name,
            entity_name = entity_name
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_entity_id_by_name("healthcare_entity_type","Corona")
    print(api_response)    
