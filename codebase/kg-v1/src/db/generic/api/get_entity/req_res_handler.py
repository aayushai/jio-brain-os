import grpc
import json
import logging as logger
from google.protobuf import json_format 
from db.generic.api.get_entity.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *

from jio.brain.proto.knowledge.api.data.get_entity_pb2 import GetEntityResponse

def pre_process_function(request):
    logger.debug(PREPROCESSING)

    entity_id = request.entity_id

    entity_type = entity_id.split("/")[0].strip() 
    key = "schema_entity_predicate/" + entity_type
    try:
        metadata = get_metadata(key)
        metadata = MessageToDict(metadata)
    except Exception as e:
        logger.error(e)
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
        return None, None,brain_status

    dynamic_list = metadata[entity_type]["dynamic"]

    static_request = build_static_request(request)
    dynamic_request = build_dynamic_request(request,dynamic_list,entity_type)
    if dynamic_request == False:
        brain_status["is_ok"] = is_valid
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = METADATA_NOT_FETCHED
    
    logger.info(PREPROCESSING_COMPLETED)
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
    dynamic_request["entity_id"] = request.entity_id

    dynamic_request["attributes"] = dynamic_list

    metadata_dict = {}
    for attribute in dynamic_list:
        key = entity_type + NAMESPACE_DELIMITER + attribute
        try:
            metadata = get_metadata(key)
            metadata = MessageToDict(metadata)
        except Exception as e:
            logger.error(e)
            brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
            return None, None,brain_status

        if brain_status["is_ok"] == False:
            return False
        metadata_dict[attribute] = metadata
    dynamic_request["metadata"] = metadata_dict

    logger.info(DYNAMIC_REQ_BUILT)
    return dynamic_request


'''
the post_process_function takes the responses from both the static and dynamic
data stores and combines them into one response, i.e, the entity has both
static and dynamic attributes present.
i/p: static response, dynamic response, status
o/p: API response(entity)
'''
def post_process_function(cursor,status):
    logger.debug(POSTPROCESSING)
    entity = cursor["static_cursor"][0]
    dynamic_attributes = cursor["dynamic_cursor"].keys()
    for attribute in dynamic_attributes:
        string = cursor["dynamic_cursor"][attribute]
        attribute_dict =  json.loads(string)
        
        entity["attributes"][attribute] = attribute_dict
    status["msg"] = ENTITY_FETCHED
        
    response_dict = {'entity':entity, 'brain_status':status}
    print(response_dict)
    response_dict.pop("brain_status")
    print(response_dict)
    response = json_format.Parse(json.dumps(response_dict), GetEntityResponse())
    logger.info(POSTPROCESSING_COMPLETED)
    return response
