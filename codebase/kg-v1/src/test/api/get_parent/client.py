import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_parent_pb2 import GetParentRequest
from jio.brain.proto.knowledge.api.data.get_parent_pb2_grpc import GetParentServiceStub

logger = get_logger("root", "get_parent")

channel = grpc.insecure_channel(get_parent_channel)

stub = GetParentServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_parent(child_node):

    logger.debug(TEST_STARTED)
    try:
        request = GetParentRequest(
            child_node = child_node
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_parent("healthcare_symptom_headache")
    print(api_response)    
