from db.generic.api.delete_entity_alias.config import *
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.api.data.delete_entity_alias_pb2 import DeleteEntityAliasResponse
import logging as logger
from google.protobuf.json_format import Parse
import grpc

'''
The pre_process function takes the request as input, fetches the schema and builds the
static request from the client request.
i/p: request
o/p: static_request
'''
def pre_process_function(request): #builds static and dynamic requests from the client request
    logger.debug(PREPROCESSING)
    
    logger.info(PREPROCESSING_COMPLETED)
    return request, None, brain_status

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)
    if(status["is_ok"] == True):
        status["brain_status_instance"][0]["parameters"]["msg"] = "Alias Deleted."
    response = DeleteEntityAliasResponse(status = status) 

    logger.debug(POSTPROCESSING_COMPLETED)
    return response