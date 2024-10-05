import grpc
import json
import logging as logger
from db.generic.api.get_entities_with_alias_name.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.get_entities_with_alias_name_pb2 import GetEntitiesWithAliasNameResponse
'''
The pre_process function takes the request as input, fetches the schema and builds the
static request from the client request.
i/p: request
o/p: static_request
'''
def pre_process_function(request): 
    logger.debug(PREPROCESSING)
    
    static_request = request

    logger.info(PREPROCESSING_COMPLETED)
    return static_request,None,brain_status

def post_process_function(cursor,brain_status): 
    logger.debug(POSTPROCESSING)
    
    response = GetEntitiesWithAliasNameResponse(entity_ids = cursor["static_cursor"], status = brain_status) 
 
    logger.debug(POSTPROCESSING_COMPLETED)
    return response