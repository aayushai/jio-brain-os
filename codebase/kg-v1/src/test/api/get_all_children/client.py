import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_all_children_pb2 import GetAllChildrenRequest
from jio.brain.proto.knowledge.api.data.get_all_children_pb2_grpc import GetAllChildrenServiceStub

logger = get_logger("root", "get_all_children")

channel = grpc.insecure_channel(get_all_children_channel)

stub = GetAllChildrenServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_all_children(predicate_name, from_node):

    logger.debug(TEST_STARTED)
    try:
        request = GetAllChildrenRequest(
            predicate_name = predicate_name,
            from_node = from_node
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_all_children("is_a", "healthcare_disease")
    print(api_response)    
