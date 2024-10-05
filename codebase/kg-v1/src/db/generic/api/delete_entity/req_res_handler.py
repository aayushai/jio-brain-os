import grpc
import json
import logging as logger
from db.generic.api.delete_entity.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.delete_entity_pb2 import DeleteEntityResponse

'''
The pre_process function takes the request as input, fetches the schema and builds the
static request from the client request.
i/p: request
o/p: static_request
'''
def pre_process_function(request): #builds static and dynamic requests from the client request
    logger.debug(PREPROCESSING)
    
    static_request = build_static_request(request)

    logger.info(PREPROCESSING_COMPLETED)
    return static_request,None,brain_status


def build_static_request(request):
    logger.debug(BUILD_STATIC_REQ)
    #returning same request as static request
    logger.info(STATIC_REQ_BUILT)
    return request
    

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)
    
    response = DeleteEntityResponse(status = status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response