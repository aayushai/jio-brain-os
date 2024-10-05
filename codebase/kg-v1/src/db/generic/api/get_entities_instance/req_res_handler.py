import grpc
import json
import logging as logger
from google.protobuf import json_format 
from db.generic.api.get_entities_instance.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.get_entities_instance_pb2 import GetEntitiesInstanceResponse

def pre_process_function(request):
    logger.debug(PREPROCESSING)

    entity_type = request.entity_type

    key = "schema_entity_predicate/" + entity_type
    try:
        metadata = get_metadata(key)
        metadata = MessageToDict(metadata)
    except Exception as e:
        logger.error(e)
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
        return None, None,brain_status

    if(metadata[entity_type]["dynamic"] == []):
        dynamic_request = None
    else:
        dynamic_request = build_dynamic_request(request, metadata[entity_type]["dynamic"], entity_type)
    static_request = build_static_request(request)
    return static_request,dynamic_request,brain_status

def build_static_request(request):
    logger.debug(STATIC_REQ_BUILT)
    logger.info(BUILD_STATIC_REQ)
    return request

'''
the build_dynamic_request method takes in the request, the list of
dynamic attributes and the entity type as the input and 
builds a metada dictionary that contains the type of the attribute
ex. "common_city_temperature: {"common_cityC_temperature": "timeseries"}
it then builds a dynamic request that contains the entity_id, the list of
dynamic attributes and the metadata dictionary created.
i/p: request, dynamic_attributes list, entity_type
o/p: dynamic request
'''
def build_dynamic_request(request,dynamic_list,entity_type):
    logger.debug(BUILD_DYNAMIC_REQ)

    dynamic_request = {}
    dynamic_request["attributes"] = dynamic_list
    dynamic_request["entity_type"] = entity_type

    logger.info(DYNAMIC_REQ_BUILT)
    return dynamic_request

def build_cursor_response(static_cursor, dynamic_cursor):
    for doc in static_cursor:
        key = doc['_key']
        dynamic_val = dynamic_cursor[key]
        for i in dynamic_val.keys():
            doc['attributes'][i] = json.loads(dynamic_val[i])
    
    return static_cursor
    
'''
the post_process_function takes the responses from both the static and dynamic
data stores and combines them into one response, i.e, the entity has both
static and dynamic attributes present.
i/p: static response, dynamic response, status
o/p: API response(entity)
'''
def post_process_function(cursor,status):
    logger.debug(POSTPROCESSING)

    if(cursor["dynamic_cursor"] != None):
        cursor_new = build_cursor_response(cursor["static_cursor"], cursor["dynamic_cursor"])
        status["msg"] = ENTITY_FETCHED
    else:
        cursor_new = cursor["static_cursor"]
        
    entity = cursor_new
    for i in entity:
        del i['_key']
        del i['_id']
        del i['_rev']

    response_dict = {'entity':entity, 'brain_status':status, 'next_page_token':"2"}
    response_dict.pop("brain_status")
    response = json_format.Parse(json.dumps(response_dict), GetEntitiesInstanceResponse())
    logger.info(POSTPROCESSING_COMPLETED)
    return response
