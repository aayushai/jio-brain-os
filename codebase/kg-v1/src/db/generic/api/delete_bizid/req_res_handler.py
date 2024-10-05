import logging as logger
from .config import *
from jio.brain.proto.knowledge.api.data.delete_bizid_pb2 import DeleteBizIdResponse

def pre_process_function(request): 
	logger.debug(PREPROCESSING)
	
	is_valid, msg = validate(request)
	if not is_valid:
		brain_status["is_ok"] = is_valid
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
		logger.debug(PREPROCESSING_INCOMPLETE)
		return None, None, brain_status
	
	static_request = build_static_request(request)
	dyamic_request = None
	
	logger.info(PREPROCESSING_COMPLETED)
	return static_request,dyamic_request,brain_status


def validate(request):
	logger.debug(VALIDATION)
	if request.entity_id is None or request.biz_id is None:
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
    
    response = DeleteBizIdResponse(status = status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response