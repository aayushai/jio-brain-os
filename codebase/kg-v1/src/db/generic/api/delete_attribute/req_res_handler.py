import grpc
import json
import logging as logger
from db.generic.api.delete_attribute.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.delete_attribute_pb2 import DeleteAttributeResponse
'''
the pre_process function takes the request as input
looks up the metadata store for the entity type and
generates static and dynamic requests.
i/p: request
o/p: static_request,dynamic_request,status
'''
def pre_process_function(request): #builds static and dynamic requests
    logger.debug(PREPROCESSING)
    entity_type = request.collection_id.split("/")[0]
    entity_id = request.collection_id.split("/")[1]
    brain_status["is_ok"] = True
    brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error."

    key = "schema_entity_predicate/"+entity_type 

    try:
        metadata = get_metadata(key)
        metadata = MessageToDict(metadata)
        static_list = metadata[entity_type]["static"]
        dynamic_list = metadata[entity_type]["dynamic"]
    except Exception as e:
        logger.error(e)
        brain_status["is_ok"] = False
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Check the Collection ID/Entity Type"
        return None, None, brain_status

    if request.attribute_name in dynamic_list:
        dynamic_request = request
        static_request = None
        return None,dynamic_request,brain_status
    elif request.attribute_name in static_list:
        static_request = request
        dynamic_request = None
        return static_request,None,brain_status
    else:
        brain_status["is_ok"] = False
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Attribute Name does not exist. Please Check and Try Again."
        return None, None, brain_status     


def post_process_function(cursor, brain_status):
    logger.debug(POSTPROCESSING)
    if not brain_status["is_ok"]:
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = ATTRIBUTE_NOT_DELETED +". "+ brain_status["brain_status_instance"][0]["parameters"]["msg"]
    else:
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = ATTRIBUTE_DELETED

    response = DeleteAttributeResponse(status=brain_status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response
    