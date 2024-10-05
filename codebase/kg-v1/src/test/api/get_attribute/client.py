import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_attribute_pb2 import GetAttributeRequest
from jio.brain.proto.knowledge.api.data.get_attribute_pb2_grpc import GetAttributeServiceStub

logger = get_logger("root", "get_attribute")

channel = grpc.insecure_channel(get_attribute_channel)

stub = GetAttributeServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_attribute(from_node_id, to_node_id):

    logger.debug(TEST_STARTED)
    try:
        request = GetAttributeRequest(
            from_node_id = from_node_id,
            to_node_id = to_node_id
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_attribute(21, 212)
    print(api_response)    
