from .query import query
import json
import grpc
from .config import *
import logging as logger

def pre_process_function(request):
	logger.debug(PREPROCESSING)

	brain_status = {
		"is_ok": True,
		"brain_status_instance": [{
			"status_code": BrainStatusCode.BRAIN_STATUS_CODE_OK,
			"parameters": {
				"msg": "no error"
			}
		}]
	}
	
	entity_id = request.entity_id
	entity_type = entity_id.split("/")[0].strip() #collection_name
	entity_name = request.entity_name

	language_proto = request.language
	language = language_proto.language
	script  = language_proto.script

	canonical_name = entity_name.canonical
	alias = list((entity_name.aliases.element).keys())[0]
	response = has_canonical_name(entity_id, language,canonical_name)
	if not response.is_present:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = CANONICAL_DOES_NOT_EXIST
		return None ,brain_status
	else:
		query_dict = {}
		query_dict["query_type"] = QueryType.Query
		query_dict["query"] = query%(entity_type,entity_id,language)

		logger.info(PREPROCESSING_COMPLETED)
		return query_dict,brain_status
	


def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)
	
	logger.debug(POSTPROCESSING)
	try:		
		logger.info(POSTPROCESSING_COMPLETED)
		return cursor,status
	except Exception as e:
		logger.error(e)
		status["is_ok"] = False
		status["brain_status_instance"][0]["parameters"]["msg"] = ERROR_MESSAGE
		return cursor ,status


def has_canonical_name(entity_id, language,canonical_name):
	from jio.brain.proto.knowledge.api.data.has_canonical_name_pb2 import HasCanonicalNameRequest
	from jio.brain.proto.knowledge.api.data.has_canonical_name_pb2_grpc import HasCanonicalNameServiceStub
	from jio.brain.proto.knowledge.base.language_pb2 import Language
	channel = grpc.insecure_channel('10.161.209.143:31020')
	stub = HasCanonicalNameServiceStub(channel)
	def test(request):
		response = stub.serve(request)
		return response
	try:
		request = HasCanonicalNameRequest(
			entity_id = entity_id,
			language = Language(
				language = language
				),
			canonical_name = canonical_name
		)
		test_response = test(request)
		
		logger.info("Testing completed")
		
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)