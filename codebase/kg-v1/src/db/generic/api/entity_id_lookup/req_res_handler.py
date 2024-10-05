import grpc
import json
import logging as logger
from google.protobuf import json_format 
from db.generic.api.entity_id_lookup.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.entity_id_lookup_pb2 import EntityIdLookupResponse

def pre_process_function(request):
    logger.debug(PREPROCESSING)

    return request,None,brain_status

'''
the post_process_function takes the responses from both the static and dynamic
data stores and combines them into one response, i.e, the entity has both
static and dynamic attributes present.
i/p: static response, dynamic response, status
o/p: API response(entity)
'''
def post_process_function(cursor,status):

    response = EntityIdLookupResponse(entity_type = cursor["static_cursor"][0]["_key"])
    logger.info(POSTPROCESSING_COMPLETED)
    return response
