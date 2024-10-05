import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_all_attributes_pb2 import GetAllAttributesRequest
from jio.brain.proto.knowledge.api.data.get_all_attributes_pb2_grpc import GetAllAttributesServiceStub

logger = get_logger("root", "get_all_attributes")

channel = grpc.insecure_channel(get_all_attributes_channel)

stub = GetAllAttributesServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_all_attributes(entity_type):

    logger.debug(TEST_STARTED)
    try:
        request = GetAllAttributesRequest(
            entity_type = entity_type
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_all_attributes("healthcare_symptom_fever")
    print(api_response)    
