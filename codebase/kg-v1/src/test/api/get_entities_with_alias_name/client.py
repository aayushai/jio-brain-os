import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from jio.brain.proto.knowledge.api.data.get_entities_with_alias_name_pb2 import GetEntitiesWithAliasNameRequest
from jio.brain.proto.knowledge.api.data.get_entities_with_alias_name_pb2_grpc import GetEntitiesWithAliasNameServiceStub
from jio.brain.proto.knowledge.base.language_pb2 import Language

logger = get_logger("root", "get_entities_with_alias_name")

channel = grpc.insecure_channel(get_entities_with_alias_name_channel)
stub = GetEntitiesWithAliasNameServiceStub(channel)

#This is the test service of KG that can be added to JioFabric
def test_get_entities_with_alias_name(entity_type,language,alias):
	
	logger.debug(TEST_STARTED)
	try:
		request = GetEntitiesWithAliasNameRequest(
			entity_type = entity_type,
			language = Language(
				language = language,
			),
		alias = alias
		)
		response = stub.serve(request)
		
		logger.info(TEST_COMPLETED)
		return response

	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
    api_response = test_get_entities_with_alias_name("agriculture_crop", "english", "angur")
    print(api_response)    