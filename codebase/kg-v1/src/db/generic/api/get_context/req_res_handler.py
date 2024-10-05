import grpc
import json
import logging as logger
from google.protobuf import json_format 
from db.generic.api.get_context.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.get_context_pb2 import GetContextResponse


def pre_process_function(request):
    logger.debug(PREPROCESSING)    
    logger.info(PREPROCESSING_COMPLETED)
    return request,None,brain_status

def build_static_request(request,static_list):
    return request

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)
    
    if status['is_ok'] == False:
        response = GetContextResponse(context = None, status = status)
    else:
        response = GetContextResponse(context = cursor["static_cursor"][0], status = status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response