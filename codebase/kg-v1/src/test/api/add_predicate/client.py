import os
import json
import grpc
from typing import Dict, List
from jio.brain.proto.knowledge.api.data.add_predicate_pb2 import AddPredicateRequest
from jio.brain.proto.knowledge.api.data.add_predicate_pb2_grpc import AddPredicateServiceStub
from test.utils.config import *
from logs.log import get_logger
from google.protobuf import json_format 
from jio.brain.proto.knowledge.base.predicate_pb2 import Predicate

from logs.log import get_logger

logger = get_logger("root", "add_predicate")

channel = grpc.insecure_channel(add_predicate_channel)
stub = AddPredicateServiceStub(channel)
def test(request):
    response = stub.serve(request)
    return response

curr_dir = os.path.dirname(os.path.realpath(__file__))
test_data_file = os.path.join(curr_dir,test_data_file_name)

def read_json_file(file:str) -> Dict:
	with open(file) as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)
from_entity_id = test_data["from_entity_id"]
to_entity_id = test_data["to_entity_id"]
predicate1 = test_data["predicate"]
predicate =json_format.Parse(json.dumps(predicate1), Predicate())

def test_add_predicate(predicate, from_entity_id, to_entity_id):
    logger.debug(TEST_STARTED)
    try:
        request = AddPredicateRequest(
            predicate = predicate,
            from_entity_id = from_entity_id,
            to_entity_id = to_entity_id
        )
        print(request.predicate.predicate_name)
        test_response = test(request)
        logger.info(TEST_COMPLETED)

        return test_response
    
    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
   api_response = test_add_predicate(predicate,from_entity_id, to_entity_id)
   print(api_response)    
