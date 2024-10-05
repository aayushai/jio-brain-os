import grpc
import json
import logging as logger
from google.protobuf import json_format 
from db.generic.api.get_attribute_value_id.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.get_attribute_value_id_pb2 import GetAttributeValueIdResponse 


def pre_process_function(request):
    logger.debug(PREPROCESSING)    
    logger.info(PREPROCESSING_COMPLETED)
    return request,None,brain_status

def build_static_request(request,static_list):
    return request

def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)

    if status['is_ok'] == False:
        response = GetAttributeValueIdResponse (parent_node_id = None, 
                                                value_id = None,
                                                attribute_id = None,
                                                status = status)
    else:
        response = GetAttributeValueIdResponse (parent_node_id = cursor["static_cursor"][0]["symptom_id"],
                                            value_id = cursor["static_cursor"][0]["value_id"],
                                            attribute_id = cursor["static_cursor"][0]["attribute_id"],
                                            status = status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response