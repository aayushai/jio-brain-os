import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_context_value_id_pb2 import GetContextValueIdRequest
from jio.brain.proto.knowledge.api.data.get_context_value_id_pb2_grpc import GetContextValueIdServiceStub

logger = get_logger("root", "get_context_value_id")

channel = grpc.insecure_channel(get_context_value_id_channel)

stub = GetContextValueIdServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_context_value_id(context_value_name):

    logger.debug(TEST_STARTED)
    try:
        request = GetContextValueIdRequest(
            context_value_name = context_value_name
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_context_value_id("Gender|Male")
    print(api_response)    
