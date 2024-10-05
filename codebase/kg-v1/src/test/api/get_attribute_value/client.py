import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_attribute_value_pb2 import GetAttributeValueRequest
from jio.brain.proto.knowledge.api.data.get_attribute_value_pb2_grpc import GetAttributeValueServiceStub

logger = get_logger("root", "get_attribute_value")

channel = grpc.insecure_channel(get_attribute_value_channel)

stub = GetAttributeValueServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_attribute_value(from_node_id, to_node_id, value_id):

    logger.debug(TEST_STARTED)
    try:
        request = GetAttributeValueRequest(
            from_node_id = from_node_id,
            to_node_id = to_node_id,
            value_id = value_id
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_attribute_value(21, 211, 2111)
    print(api_response)    
