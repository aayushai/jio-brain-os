import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_entity_name_by_id_pb2 import GetEntityNameByIdRequest
from jio.brain.proto.knowledge.api.data.get_entity_name_by_id_pb2_grpc import GetEntityNameByIdServiceStub

logger = get_logger("root", "get_entity_name_by_id")

channel = grpc.insecure_channel(get_entity_name_by_id_channel)

stub = GetEntityNameByIdServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_entity_name_by_id(collection_name, entity_id):

    logger.debug(TEST_STARTED)
    try:
        request = GetEntityNameByIdRequest(
            collection_name = collection_name,
            entity_id = entity_id
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_entity_name_by_id("healthcare_entity_type", 11)
    print(api_response)    
