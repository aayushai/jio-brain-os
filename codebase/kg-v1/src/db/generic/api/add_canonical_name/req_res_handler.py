from .config import *
from jio.brain.proto.knowledge.api.data.add_canonical_name_pb2 import AddCanonicalNameResponse
import logging as logger
from db.generic.api.add_canonical_name.config import *

'''
The pre_process function takes the request as input, fetches the schema and builds the
static request from the client request.
i/p: request
o/p: static_request
'''

def pre_process_function(request):
    logger.debug(PREPROCESSING)
    is_valid, msg = validate(request)
    if not is_valid:
        brain_status["is_ok"] = is_valid
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
        logger.debug(PREPROCESSING_INCOMPLETE)
        return None, None, brain_status
    
    static_request = build_static_request(request)
    dynamic_request = None
    logger.info(PREPROCESSING_COMPLETED)
    return static_request,dynamic_request,brain_status


def validate(request):
	logger.debug(VALIDATION)
	if request.entity_id is None or request.entity_name is None:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False,INPUT_PARAMETER_COUNT_ERROR
	else:
		logger.info(VALIDATED)
		return True,None 


def build_static_request(request):
	logger.debug(BUILD_STATIC_REQ)
	#returning same request as static request
	logger.info(STATIC_REQ_BUILT)
	return request
    

def post_process_function(cursor,status): 
	logger.debug(POSTPROCESSING)
	
	response = AddCanonicalNameResponse(status = status) 

	logger.debug(POSTPROCESSING_COMPLETED)
	return response