import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_valid_entity_attribute_values_given_filter_pb2 import GetValidEntityAttributeValuesGivenFilterRequest
from jio.brain.proto.knowledge.api.data.get_valid_entity_attribute_values_given_filter_pb2_grpc import GetValidEntityAttributeValuesGivenFilterServiceStub

logger = get_logger("root", "get_valid_entity_attribute_values_given_filter")

channel = grpc.insecure_channel(get_valid_entity_attribute_values_given_filter_channel)

stub = GetValidEntityAttributeValuesGivenFilterServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_valid_entity_attribute_values_given_filter(entity_id, context_id, entity_type, attribute_id):

    logger.debug(TEST_STARTED)
    try:
        request = GetValidEntityAttributeValuesGivenFilterRequest(
            entity_id = entity_id,
            context_id = context_id,
            entity_type = entity_type,
            attribute_id = attribute_id
        )

        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_valid_entity_attribute_values_given_filter(21, 311, "symptom", 211)
    print(api_response)    
