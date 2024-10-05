import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_edge_pb2 import GetEdgeRequest
from jio.brain.proto.knowledge.api.data.get_edge_pb2_grpc import GetEdgeServiceStub

logger = get_logger("root", "get_edge")

channel = grpc.insecure_channel(get_edge_channel)

stub = GetEdgeServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_get_edge(edge_collection, from_id, to_id):

    logger.debug(TEST_STARTED)
    try:
        request = GetEdgeRequest(
            edge_collection = edge_collection,
            from_id = from_id,
            to_id = to_id
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_edge("has_symptom", 12, 21)
    print(api_response)    
