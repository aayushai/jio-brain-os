import grpc
import json
import logging as logger
from google.protobuf import json_format 
from db.generic.api.get_predicate.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.get_predicate_pb2 import GetPredicateResponse

def pre_process_function(request):
    logger.debug(PREPROCESSING)

    logger.info(PREPROCESSING_COMPLETED)

    return request,None,brain_status

def post_process_function(cursor,brain_status): 
    logger.debug(POSTPROCESSING)

    try:
        response_dict = {'predicate':cursor["static_cursor"][0], 'status':brain_status}
    except Exception as e:
        brain_status["is_ok"] = False
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Check the From and To Nodes, and try Again!"
        response_dict = {'status':brain_status}
        
    response = json_format.Parse(json.dumps(response_dict), GetPredicateResponse())

    logger.debug(POSTPROCESSING_COMPLETED)

    return response
