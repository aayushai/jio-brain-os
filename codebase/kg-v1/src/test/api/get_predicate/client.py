import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_predicate_pb2 import GetPredicateRequest
from jio.brain.proto.knowledge.api.data.get_predicate_pb2_grpc import GetPredicateServiceStub

logger = get_logger("root", "get_predicate")

channel = grpc.insecure_channel(get_predicate_channel)

stub = GetPredicateServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response

#This is the test service of KG that can be added to JioFabric
def test_get_predicate(predicate_id):
	logger.debug(TEST_STARTED)
	try:
		request = GetPredicateRequest(
			vertical = "common",
			collection_name = "is_a",
			from_id = "common_person_celebrity/124026",
			to_id = "common_person_celebrity_politician/1080"
		)

		test_response = test(request)
		
		logger.info(TEST_COMPLETED)
		
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
	api_response = test_get_predicate("entity")
	print(api_response)    

