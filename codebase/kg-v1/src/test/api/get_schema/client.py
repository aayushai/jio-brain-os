import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.schema.get_type_schema_pb2 import GetTypeSchemaRequest
from jio.brain.proto.knowledge.api.schema.get_type_schema_pb2_grpc import GetTypeSchemaServiceStub

logger = get_logger("root", "get_schema")

channel = grpc.insecure_channel(get_schema_channel)

stub = GetTypeSchemaServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_schema(collection_name):

    logger.debug(TEST_STARTED)
    try:
        request = GetTypeSchemaRequest(
            collection_name = collection_name
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_schema("common_celeb1")
    print(api_response)    
