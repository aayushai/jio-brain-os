import grpc
import json
from typing import Dict, List
import os
from jio.brain.proto.knowledge.api.data.update_bizid_to_entity_pb2 import UpdateBizidToEntityRequest
from jio.brain.proto.knowledge.api.data.update_bizid_to_entity_pb2_grpc import UpdateBizidToEntityServiceStub
from test.utils.config import *
from jio.brain.proto.knowledge.base.biz_id_pb2 import BizId
from logs.log import get_logger

channel = grpc.insecure_channel(update_bizid_to_entity_channel)
stub = UpdateBizidToEntityServiceStub(channel)

logger = get_logger("root", "update_bizid_to_entity")

curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)

def read_json_file(file:str) -> Dict:
    with open(file) as f:
        data = json.load(f)
    return data

test_data = read_json_file(test_data_file)
entity_id = test_data["entity_id"]
old_biz_id_type = test_data["old_biz_id_type"]
old_biz_id_value = test_data["old_biz_id_value"]
new_biz_id_type = test_data["new_biz_id_type"]
new_biz_id_value = test_data["new_biz_id_value"]


def test_update_bizid_to_entity(entity_id, old_biz_id_type, old_biz_id_value, new_biz_id_type, new_biz_id_value):
    logger.debug(TEST_STARTED)
    try:
        request =  UpdateBizidToEntityRequest(
            entity_id = entity_id,
            old_biz_id = BizId(
                type = old_biz_id_type,
                value = old_biz_id_value),
            new_biz_id = BizId(
                type = new_biz_id_type,
                value = new_biz_id_value)
        )
        
        response = stub.serve(request)
        logger.info(TEST_COMPLETED)
        return response
        
    except Exception as e:
        logger.error(e)
        return str(e)


if __name__ == "__main__":
    api_response = test_update_bizid_to_entity(entity_id, old_biz_id_type, old_biz_id_value, new_biz_id_type, new_biz_id_value)
    print(api_response)    
  