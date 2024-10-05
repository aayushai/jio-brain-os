import grpc
import json
import logging as logger
from db.generic.api.graph_query.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.graph_query_pb2 import GraphQueryResponse

'''
The pre_process function takes the request as input, fetches the schema and builds the
static request from the client request.
i/p: request
o/p: static_request
'''
def pre_process_function(request): # Builds static and dynamic requests from the client request
    logger.debug(PREPROCESSING)    
    static_request = request    
    logger.info(PREPROCESSING_COMPLETED)    
    return static_request, None, brain_status
    

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)    
    response = GraphQueryResponse(cursor = cursor["static_cursor"], status = status)
    logger.debug(POSTPROCESSING_COMPLETED)
    return response