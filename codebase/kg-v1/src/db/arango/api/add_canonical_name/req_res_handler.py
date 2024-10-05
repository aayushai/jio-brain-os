import grpc
from .query import query
import json
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
	canonical_name = entity_name.canonical
	alias = list((entity_name.aliases.element).keys())[0]

	canonical_name_dict = {
				"canonical":canonical_name,
				"aliases": {
					"element": {
						"%s"%alias: True
					}
				}	
	}

	canonical_name_str = json.dumps(canonical_name_dict) #converting dictionary to string
	response = has_canonical_name(entity_id, language,canonical_name)
	if response.is_present:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = CANONICAL_ALREADY_EXIST
		return None ,brain_status
	else:
		query_dict = {}
		query_dict["query_type"] = QueryType.Query
		query_dict["query"] = query%(entity_id,language,canonical_name_str,entity_type)

		logger.info(PREPROCESSING_COMPLETED)
		return query_dict,brain_status
	
'''
Validate method checks if all the required inputs are present
it returns an Input parameter count error if not
i/p: string(request)
o/p:flag,error message
'''
def validate(req):
	logger.debug(VALIDATION)

	if "entity_id" in req and "entity_name" in req:
		logger.info(VALIDATED)
		return True,None 

	else:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False,INPUT_PARAMETER_COUNT_ERROR

'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, status):
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
	