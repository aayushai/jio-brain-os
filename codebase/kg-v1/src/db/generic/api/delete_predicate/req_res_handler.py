import grpc
import json
import logging as logger
from db.generic.api.delete_predicate.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.delete_predicate_pb2 import DeletePredicateResponse

def pre_process_function(request): 
    logger.debug(PREPROCESSING)

    req = str(request)
    
    predicate_name = request.predicate_name

    key = "schema_entity_predicate/"+predicate_name
    try:
        metadata = get_metadata(key)
        metadata = MessageToDict(metadata)
        static_list = metadata[predicate_name]["static"]
    except Exception as e:
        brain_status["is_ok"] = False
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Check the Predicate Name."
        return None, None, brain_status

    static_request = build_static_request(request,static_list)
    
    logger.info(PREPROCESSING_COMPLETED)
    return static_request,None,brain_status


def build_static_request(request,static_list):
    return request

def post_process_function(cursor,brain_status):
    logger.debug(POSTPROCESSING)

    response = DeletePredicateResponse(status = brain_status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response