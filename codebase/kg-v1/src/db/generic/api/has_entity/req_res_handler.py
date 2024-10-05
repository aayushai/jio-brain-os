from db.generic.api.has_entity.config import *
from jio.brain.proto.knowledge.api.data.has_entity_pb2 import HasEntityResponse
import logging as logger

def pre_process_function(request): 
	logger.debug(PREPROCESSING)

	brain_status = {
		"is_ok": True,
		"brain_status_instance": [{
			"status_code": BrainStatusCode.BRAIN_STATUS_CODE_OK,
			"parameters": {
				"NO_ERROR": "no error"
			}
		}]
	}

	is_valid, msg = validate(request)
	if not is_valid:
		brain_status["is_ok"] = is_valid

		if request.entity_id == "":
			parameters = {     
				"INVALID_INPUT": "Wrong format: Empty Entity ID"
			}
			brain_status["brain_status_instance"][0]["parameters"] = parameters
			
		else:
			parameters = {     
				"INVALID_INPUT": msg
			}
			brain_status["brain_status_instance"][0]["parameters"] = parameters

		logger.debug(PREPROCESSING_INCOMPLETE)
		return None, None, brain_status
	
	static_request = build_static_request(request)
	dynamic_request = None
	logger.info(PREPROCESSING_COMPLETED)
	return static_request,dynamic_request,brain_status


def build_static_request(request):
	logger.debug(BUILD_STATIC_REQ)
	#returning same request as static request
	logger.info(STATIC_REQ_BUILT)
	return request

def validate(request):
	logger.debug(VALIDATION)

	if request.entity_id:
		if "/" not in str(request.entity_id): # use regex?
			msg = "Wrong format: Invalid/Missing Delimiter"
			logger.debug(PREPROCESSING_INCOMPLETE)
			return False, msg
		elif NAMESPACE_DELIMITER not in str(request.entity_id):
			msg = "Wrong format: Invalid Entity ID"
			logger.debug(PREPROCESSING_INCOMPLETE)
			return False, msg
		logger.info(VALIDATED)
		return True, None
	else:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False, INPUT_PARAMETER_COUNT_ERROR


def post_process_function(cursor,status):
	logger.debug(POSTPROCESSING)
	
	if cursor["static_cursor"] is None:
		response = HasEntityResponse(is_present = False , status = status)
	else:
		response = HasEntityResponse(is_present = True, status = status)


	logger.debug(POSTPROCESSING_COMPLETED)
	return response