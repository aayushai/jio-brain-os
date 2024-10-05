import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_all_biz_id_types_of_entity_id_pb2 import GetAllBizIdTypesOfEntityIdRequest
from jio.brain.proto.knowledge.api.data.get_all_biz_id_types_of_entity_id_pb2_grpc import GetAllBizIdTypesOfEntityIdServiceStub

logger = get_logger("root", "get_all_biz_id_types_of_entity_id")

channel = grpc.insecure_channel(get_all_biz_id_types_of_entity_id_channel)

stub = GetAllBizIdTypesOfEntityIdServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response

def test_get_all_biz_id_types_of_entity_id(entity_id):
    try:
        logger.debug(TEST_STARTED)
        request = GetAllBizIdTypesOfEntityIdRequest(
            entity_id = entity_id
        )
        
        test_response = test(request)
        
        logger.info(TEST_COMPLETED)
        return test_response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_get_all_biz_id_types_of_entity_id("common_person/12211")
    print(api_response)    


    
    

  




