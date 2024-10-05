import os
import json
import grpc
from typing import Dict, List
from google.protobuf import json_format 
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.delete_attribute_pb2 import DeleteAttributeRequest
from jio.brain.proto.knowledge.api.data.delete_attribute_pb2_grpc import DeleteAttributeServiceStub

logger = get_logger("root", "delete_attribute")
channel = grpc.insecure_channel(delete_attribute_channel)
stub = DeleteAttributeServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response

def test_delete_attribute(collection_name, attribute_name):
    logger.debug("entered test method")
    try:
        request = DeleteAttributeRequest(
            collection_id = collection_name,
            attribute_name = attribute_name
        )
        
        test_response = test(request)
        
        logger.info("Testing completed")
        return test_response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_delete_attribute("common_person_celebrity/124026","age")
    print(api_response)