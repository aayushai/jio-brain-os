import grpc
import json
import logging as logger
from db.generic.api.get_entities_with_canonical_name.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.get_entities_with_canonical_name_pb2 import GetEntitiesWithCanonicalNameResponse

def pre_process_function(request): 
    logger.debug(PREPROCESSING)

    static_request = request
    
    logger.info(PREPROCESSING_COMPLETED)
    return static_request, None, brain_status
    
def post_process_function(cursor,status): 
    logger.debug(POSTPROCESSING)

    if(cursor["static_cursor"] is None):
        brain_status["is_ok"] = False
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Data Not Available! Check the Language/Entity ID/Canonical Name."
    response = GetEntitiesWithCanonicalNameResponse(entity_ids = cursor["static_cursor"], status = brain_status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response