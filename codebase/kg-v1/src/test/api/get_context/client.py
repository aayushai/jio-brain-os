import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_context_pb2 import GetContextRequest
from jio.brain.proto.knowledge.api.data.get_context_pb2_grpc import GetContextServiceStub

logger = get_logger("root", "get_context")

channel = grpc.insecure_channel(get_context_channel)

stub = GetContextServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_context(context_id):

    logger.debug(TEST_STARTED)
    try:
        request = GetContextRequest(
            context_id = context_id
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_context(31)
    print(api_response)    
