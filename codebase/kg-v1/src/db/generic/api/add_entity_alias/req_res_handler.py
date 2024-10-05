from os import stat
from google.protobuf.json_format import MessageToDict
from db.generic.api.add_entity_alias.config import DELIMITER,POSTPROCESSING_COMPLETED,POSTPROCESSING,PREPROCESSING_COMPLETED,PREPROCESSING,VALIDATED,VALIDATION,PREPROCESSING_INCOMPLETE,status,DYNAMIC_REQ_BUILT,BUILD_DYNAMIC_REQ,INPUT_PARAMETER_COUNT_ERROR, GET_METADATA,METADATA_FETCHED,METADATA_NOT_FETCHED,BUILD_STATIC_REQ,STATIC_REQ_BUILT
from jio.brain.proto.knowledge.api.data.add_entity_alias_pb2 import AddEntityAliasResponse
import logging as logger
import grpc
from db.generic.api.add_entity.config import *
'''
The pre_process function takes the request as input, fetches the schema and builds the
static request from the client request.
i/p: request
o/p: static_request
'''
def pre_process_function(request): #builds static and dynamic requests from the client request
    logger.debug(PREPROCESSING)
    is_valid, msg = validate(request)

    if not is_valid:
        brain_status["is_ok"] = is_valid
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = BrainStatusCode.BRAIN_STATUS_CODE_INVALID_DATA
        logger.debug(PREPROCESSING_INCOMPLETE)
        return None, None,brain_status

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
    req = request.entity_id
    if req is None:
        logger.error(INPUT_PARAMETER_COUNT_ERROR)
        return False,INPUT_PARAMETER_COUNT_ERROR
    else:
        logger.info(VALIDATED)
        return True,None   

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)
    
    response = AddEntityAliasResponse(status = status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response