import grpc
import json
import logging as logger
from db.generic.api.get_schema.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *
from google.protobuf.struct_pb2 import Struct

from jio.brain.proto.knowledge.api.schema.get_type_schema_pb2 import GetTypeSchemaResponse

'''
The pre_process function takes the request as input, fetches the schema and builds the
static request from the client request.
i/p: request
o/p: static_request
'''
def pre_process_function(request): #builds static and dynamic requests from the client request
    logger.debug(PREPROCESSING)
    
    static_request = request

    logger.info(PREPROCESSING_COMPLETED)
    return static_request,None,brain_status    

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)
    cursor_final = cursor["static_cursor"][0][0]
    s = Struct()
    for k, v in cursor_final.items():
        s.update({k:v})
    response = GetTypeSchemaResponse(schema = s,status = status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response