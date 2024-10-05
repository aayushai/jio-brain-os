import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_entities_with_canonical_name_pb2 import GetEntitiesWithCanonicalNameRequest
from jio.brain.proto.knowledge.api.data.get_entities_with_canonical_name_pb2_grpc import GetEntitiesWithCanonicalNameServiceStub
from jio.brain.proto.knowledge.base.language_pb2 import Language

logger = get_logger("root", "get_entities_with_canonical_name")

channel = grpc.insecure_channel(get_entities_with_canonical_name_channel)
stub = GetEntitiesWithCanonicalNameServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response

def test_get_entities_with_canonical_name(entity_type,canonical_name,language):
	logger.debug(TEST_STARTED)
	try:
		request = GetEntitiesWithCanonicalNameRequest(
			entity_type = entity_type,
			canonical_name = canonical_name,
			language = Language(
				language = language,
			)			
		)
		test_response = test(request)
		logger.info(TEST_COMPLETED)
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
	api_response = test_get_entities_with_canonical_name("agriculture_water_source", "CanalA", "english")
	print(api_response)    







		







