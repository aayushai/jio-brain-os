import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_context_value_name_pb2 import GetContextValueNameRequest
from jio.brain.proto.knowledge.api.data.get_context_value_name_pb2_grpc import GetContextValueNameServiceStub

logger = get_logger("root", "get_context_value_name")

channel = grpc.insecure_channel(get_context_value_name_channel)

stub = GetContextValueNameServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_context_value_name(context_id , value_id):

    logger.debug(TEST_STARTED)
    try:
        request = GetContextValueNameRequest(
            context_id  = context_id,
            value_id = value_id
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_context_value_name(31, 311)
    print(api_response)    
