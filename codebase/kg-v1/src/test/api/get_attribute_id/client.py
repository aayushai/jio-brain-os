import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_attribute_id_pb2 import GetAttributeIdRequest
from jio.brain.proto.knowledge.api.data.get_attribute_id_pb2_grpc import GetAttributeIdServiceStub

logger = get_logger("root", "get_attribute_id")

channel = grpc.insecure_channel(get_attribute_id_channel)

stub = GetAttributeIdServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_attribute_id(attribute_name):

    logger.debug(TEST_STARTED)
    try:
        request = GetAttributeIdRequest(
            attribute_name = attribute_name
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_attribute_id("Cough|Type")
    print(api_response)    
