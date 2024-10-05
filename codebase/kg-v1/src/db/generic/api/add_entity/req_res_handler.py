import logging as logger
from db.generic.api.add_entity.config import *
from db.generic.services.brain_dispatcher import *
from db.generic.services.delete_entity_service import delete_entity
from db.generic.services.metadata_dispatcher import *
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.api.data.add_entity_pb2 import AddEntityResponse


def pre_process_function(request):
    logger.debug(PREPROCESSING)
    is_valid, msg = validate(request)

    if not is_valid:
        brain_status["is_ok"] = is_valid
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Invalid Request"
        logger.debug(PREPROCESSING_INCOMPLETE)
        return None, None,brain_status

    entity_type = request.entity.entity_type
    
    key = "schema_entity_predicate/"+entity_type #metadata_entity_predicate/HumanResource_employee_emp_details

    try:
        metadata = get_metadata(key)
        metadata = MessageToDict(metadata)
        static_list = metadata[entity_type]["static"]
        dynamic_list = metadata[entity_type]["dynamic"]
    except Exception as e:
        logger.error(e)
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
        return None, None,brain_status

    static_request = build_static_request(request,static_list)
    dynamic_request = build_dynamic_request(request,dynamic_list)
    print(static_request)
    print(brain_status)
    if(static_request or dynamic_request):
        brain_id = getBrainId(static_request, entity_type)
        if static_request is not None:
            static_request['entity']['_key'] = str(brain_id)
        
        if dynamic_request is not None:
            dynamic_request['entity']['_key'] = str(brain_id)
    else:
        brain_status_instance["parameters"]= {'msg':"Invalid Request"}
        brain_status["is_ok"] = False

    logger.info(PREPROCESSING_COMPLETED)
    return static_request,dynamic_request,brain_status

def validate(request):
    logger.debug(VALIDATION)
    req = MessageToDict(request)
    print(req)
    if (req == {"entity": {}}):
        print("Here")
        logger.error(INPUT_PARAMETER_COUNT_ERROR)
        return False,INPUT_PARAMETER_COUNT_ERROR
    else:
        logger.info(VALIDATED)
        return True,None 

def build_static_request(request,static_list):
    logger.debug(BUILD_STATIC_REQ)
    
    request =  MessageToDict(request)
    attributes = request["entity"]["attributes"]
    attributes_list = list(attributes.keys())

    for key in attributes_list:
        if key not in static_list:
            del attributes[key]

    if attributes == {}:
        return None
    else:
        logger.info(STATIC_REQ_BUILT)
        request["entity"]["attributes"] = attributes
        return request

def build_dynamic_request(request,dynamic_list):
    logger.debug(BUILD_DYNAMIC_REQ)
    request =  MessageToDict(request) 

    attributes = request["entity"]["attributes"]
    attributes_list = list(attributes.keys())

    for key in attributes_list:
        if key not in dynamic_list:
            del attributes[key] 

    if attributes == {}:
        return None

    else:
        logger.info(DYNAMIC_REQ_BUILT)
        request["entity"]["attributes"] = attributes
        return request

def post_process_function(cursor,status):
    logger.debug(POSTPROCESSING)
    print(status)
    if not status["is_ok"]:
        entity_id = ""
        if(status["brain_status_instance"][0]["parameters"]["msg"] == MEASUREMENT_NOT_ADDED):
            status["brain_status_instance"][0]["parameters"]["msg"] = "Measurement could not be Added to Influx, Hence removing the corresponding Entity from Arango!"
            delete_entity(cursor["static_cursor"][0])
            
    else:
        entity_id = cursor["static_cursor"][0]
        status["brain_status_instance"][0]["status_code"] = BrainStatusCode.KNOWLEDGE_GRAPH_ENTITY_ADDED
        status["brain_status_instance"][0]["parameters"]["msg"] = ENTITY_ADDED

    response = AddEntityResponse(entity_id = entity_id,status=status)

    logger.debug(POSTPROCESSING_COMPLETED)
    return response