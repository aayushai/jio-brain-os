import grpc
import json
import logging as logger
from db.generic.api.add_predicate.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.add_predicate_pb2 import AddPredicateResponse

def pre_process_function(request): 
    logger.debug(PREPROCESSING)

    req = str(request)
    
    predicate = request.predicate
    predicate_name = predicate.predicate_name

    key = "schema_entity_predicate/"+predicate_name
    metadata = get_metadata(key)
    metadata = MessageToDict(metadata)
    
    static_list = metadata[predicate_name]["static"]

    static_request = build_static_request(request,static_list)
    
    logger.info(PREPROCESSING_COMPLETED)
    return static_request,None,brain_status


def build_static_request(request,static_list):
    return request

def post_process_function(cursor,brain_status):
    logger.debug(POSTPROCESSING)
    if(cursor != []):
        response = AddPredicateResponse(predicate_id = cursor["static_cursor"][0], status = brain_status)
    else:
        response = AddPredicateResponse(predicate_id = '-1', status = brain_status)
    

    logger.debug(POSTPROCESSING_COMPLETED)
    return response