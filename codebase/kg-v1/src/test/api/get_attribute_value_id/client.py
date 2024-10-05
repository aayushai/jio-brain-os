import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_attribute_value_id_pb2 import GetAttributeValueIdRequest
from jio.brain.proto.knowledge.api.data.get_attribute_value_id_pb2_grpc import GetAttributeValueIdServiceStub

logger = get_logger("root", "get_attribute_value_id")

channel = grpc.insecure_channel(get_attribute_value_id_channel)

stub = GetAttributeValueIdServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_attribute_value_id(attribute_value_name):

    logger.debug(TEST_STARTED)
    try:
        request = GetAttributeValueIdRequest(
            attribute_value_name = attribute_value_name
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_attribute_value_id("Cough|Colour|Yellow")
    print(api_response)    
