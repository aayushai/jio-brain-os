from os import stat
import grpc
import json
import logging as logger
from google.protobuf import json_format 
from db.generic.api.get_entity_id_by_name.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.get_entity_id_by_name_pb2 import GetEntityIdByNameResponse 


def pre_process_function(request):
    logger.debug(PREPROCESSING)    
    logger.info(PREPROCESSING_COMPLETED)
    return request,None,brain_status

def build_static_request(request,static_list):
    return request

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)
    if status['is_ok'] == False:
        response = GetEntityIdByNameResponse (entity_id = None, status = status)
    else:
        entity_id = cursor["static_cursor"][0]['entity_id']
        response = GetEntityIdByNameResponse (entity_id = entity_id, status = status)
    logger.debug(POSTPROCESSING_COMPLETED)
    return response