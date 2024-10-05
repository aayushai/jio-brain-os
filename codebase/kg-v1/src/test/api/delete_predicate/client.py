import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.delete_predicate_pb2 import DeletePredicateRequest
from jio.brain.proto.knowledge.api.data.delete_predicate_pb2_grpc import DeletePredicateServiceStub

logger = get_logger("root", "delete_predicate")

channel = grpc.insecure_channel(delete_predicate_channel)
stub = DeletePredicateServiceStub(channel)
def test(request):
    response = stub.serve(request)
    return response
    
def test_delete_predicate(predicate_name, from_entity_id, to_entity_id):
    logger.debug(TEST_STARTED)
    try:
        request = DeletePredicateRequest(
            predicate_name = predicate_name,
            from_entity_id = from_entity_id,
            to_entity_id = to_entity_id
        )
        
        test_response = test(request)
        logger.info(TEST_COMPLETED)

        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_delete_predicate("is_a", "metadata_entity_predicate/common_person_celebrity_politician", "metadata_entity_predicate/common_person_celebrity")
    print(api_response)    







