import grpc
import json
import re
import logging as logger
from db.generic.api.enrich_api.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *
from google.protobuf import json_format
from jio.brain.proto.knowledge.api.data.enrich_api_pb2 import *

'''
the pre_process_function takes the request and generates a static request
i/p: request
o/p: static_request,brain_status
'''
def pre_process_function(request): 
    logger.debug(PREPROCESSING)
    brain_status["is_ok"] = True
    brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"

    entity_id_list = []
    static_attributes_list = []
    dynamic_attributes_list = []
    predicate_list = []
    request = MessageToDict(request)
    static_request = request
    dynamic_request = request.copy()

    if("enrichAttributeRequest" not in request):
       static_request["attributeName"] = None
       dynamic_request["attributeName"] = None
    else:
        for i in range (len(request["enrichAttributeRequest"])):

            cursor["static_cursor"] = None
            cursor["dynamic_cursor"] = None
            entity_id_type = request["enrichAttributeRequest"][i]["type"]
            entity_id = request["enrichAttributeRequest"][i]["entityIds"]
            attribute_name = request["enrichAttributeRequest"][i]["attributes"]
            try:
                key = "schema_entity_predicate/"+entity_id_type

                metadata = get_metadata(key)    
                metadata = MessageToDict(metadata)
                static_list = metadata[entity_id_type]["static"]
                dynamic_list = metadata[entity_id_type]["dynamic"]

            except Exception as e:
                brain_status["is_ok"] = False
                brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Check for the Entity Type."
                return None, None, brain_status

            for j in entity_id:
                for k in attribute_name:
                    if(k in static_list):
                        static_attributes_list.append(entity_id_type+"/"+j+"."+k)
                    else:
                        dynamic_attributes_list.append(entity_id_type+"/"+j+"."+k)

        static_request["attributeName"] = static_attributes_list
        dynamic_request["attributeName"] = dynamic_attributes_list

    if("enrichPredicateRequest" not in request):
        static_request["predicateName"] = None
    else:
        for i in range (len(request["enrichPredicateRequest"])):

            entity_id_type = request["enrichPredicateRequest"][i]["type"]
            entity_id = request["enrichPredicateRequest"][i]["entityIds"]
            predicate_name = request["enrichPredicateRequest"][i]["predicates"]

            for j in entity_id:
                for k in predicate_name:
                    predicate_list.append(entity_id_type+"/"+j+"."+k)

        static_request["predicateName"] = predicate_list

    if(dynamic_attributes_list == []):
        dynamic_request = None
    if(static_attributes_list == [] and predicate_list == []):
        static_request = None

    logger.info(PREPROCESSING_COMPLETED)

    return static_request,dynamic_request,brain_status
    
def merge(a, b, path=None):
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass 
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a

def build_attribute_response(cursor):
    cur = {}
    cur_fin = {}
    
    if(cursor["dynamic_cursor"] is None):
        cur = cursor["static_cursor"]["static_cursor_attribute"]
        cur_fin["entityIdAttribute"] = cur
    elif(cursor["static_cursor"] is None):
        cur = cursor["dynamic_cursor"]["dynamic_cursor_attribute"]
        cur_fin["entityIdAttribute"] = cur
    else:
        cursor_type_list = list(cursor["static_cursor"]["static_cursor_attribute"].keys())
        for key in cursor["static_cursor"]["static_cursor_attribute"]:
            if(key in cursor["dynamic_cursor"]["dynamic_cursor_attribute"]):
                cur.update(merge(cursor["static_cursor"]["static_cursor_attribute"][key],cursor["dynamic_cursor"]["dynamic_cursor_attribute"][key]))
        
        cur_fin["entityIdAttribute"] = cursor["static_cursor"]["static_cursor_attribute"]

    cursor_fin = (json_format.Parse(json.dumps(cur_fin), EnrichAttributeResponse()))
    return cursor_fin

def build_predicate_response(cursor):
    cur_fin = {}
    cur_fin["subject_predicate"] = cursor["static_cursor"]["static_cursor_predicate"]
    cursor_fin = (json_format.Parse(json.dumps(cur_fin), EnrichPredicateResponse()))
    return cursor_fin

def post_process_function(cursor,brain_status): 
    logger.debug(POSTPROCESSING)    

    if(cursor == {'static_cursor': None, 'dynamic_cursor': None}):
        return EnrichServiceResponse(status = brain_status)

    if brain_status["is_ok"] == False:
        response = EnrichServiceResponse(status = brain_status)
        return response

    attribute_cursor = build_attribute_response(cursor)    
    predicate_cursor = build_predicate_response(cursor)
    response = EnrichServiceResponse(status = brain_status, enrich_attribute_response = attribute_cursor, enrich_predicate_response= predicate_cursor)    
    
    logger.debug(POSTPROCESSING_COMPLETED)
    return response
