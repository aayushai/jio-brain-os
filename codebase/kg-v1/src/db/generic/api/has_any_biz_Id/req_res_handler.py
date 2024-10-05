from google.protobuf.json_format import MessageToDict
from db.generic.api.has_any_biz_id.config import *
from jio.brain.proto.knowledge.api.data.has_any_biz_id_pb2 import HasAnyBizIdResponse
import logging as logger
from google.protobuf.json_format import Parse
import json
import grpc

def pre_process_function(request): 
    logger.debug(PREPROCESSING)

    is_valid, msg = validate(request)
    if not is_valid:
        brain_status["is_ok"] = is_valid
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
        logger.debug(PREPROCESSING_INCOMPLETE)
        return None, None, brain_status
  
    entity_id = request.entity_id

    print(entity_id)

    static_request = build_static_request(request)
    dynamic_request = None
    logger.info(PREPROCESSING_COMPLETED)
    return static_request,dynamic_request,brain_status
   


def build_static_request(request):
    return request

def validate(request):
	logger.debug(VALIDATION)

	if request.entity_id:
		logger.info(VALIDATED)
		return True, None
	else:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False, INPUT_PARAMETER_COUNT_ERROR 

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)
    
    if cursor["static_cursor"] == [None] or cursor["static_cursor"] is None or cursor["static_cursor"] == []:
        response = HasAnyBizIdResponse(is_present = False , status =status)
    else:
        response = HasAnyBizIdResponse(is_present = True, status= status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response
  


        