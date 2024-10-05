import ast
import json
import logging as logger
import healthkg.utils.logs.config as logconfig
from google.protobuf import json_format 
from google.protobuf.json_format import MessageToDict
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.get_age_group_id import get_age_group_id
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from jio.brain.proto.knowledge.healthcare.req_res.get_valid_symptom_attribute_values_given_filter_pb2 import GetValidSymptomAttributeValuesGivenFilterResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
import copy

class GetValidSymptomAttributeValuesGivenFilterWorker:

    def __init__(self):
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)

        transform_request_status = copy.deepcopy(status)
        if not request.symptom_id or not request.attribute_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request_object = None
        else:        
            request_object = {"entity_id": request.symptom_id,
                              "entity_type": "symptom",
                              "age": request.age,
                              "gender": request.gender,
                              "attribute_id": request.attribute_id,}                  
        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        request['context_ids'] = [None]

        if request['age']:
            age_group_ids = get_age_group_id(dispatcher, [request['age']])

            if not age_group_ids:
                dispatcher_status = copy.deepcopy(status)
                dispatcher_status['is_ok'] = False
                dispatcher_status['status_message'] = "Modelling error (age group not found)"
                return None, dispatcher_status

            request["context_ids"] = age_group_ids

        if request['gender']:
            request["context_ids"] += [request['gender']]

        response = []
        for context_id in request["context_ids"]:
            dispatcher_request = {"entity_id": request["entity_id"],
                                  "entity_type": request["entity_type"],
                                  "context_id": context_id,
                                  "attribute_id": request["attribute_id"]}
            dispatcher_response = dispatcher.get_valid_entity_attribute_values_given_filter(dispatcher_request)
            dispatcher_response, dispatcher_status = validate_kg_response(dispatcher_response)
            if not dispatcher_response:
                return None, dispatcher_status
            response.append(dispatcher_response)
        return response, dispatcher_status

    def transform_response(self, response, status):
                                                   
        logger.debug(logconfig.POSTPROCESSING) 

        if not response:
            response = GetValidSymptomAttributeValuesGivenFilterResponse(status = status)
        else:
            response_obj = []
            for i in response:
                response_obj.append(set(i.value_id))
            common_response = set.intersection(*response_obj)
            response = GetValidSymptomAttributeValuesGivenFilterResponse(value_id = common_response, status = status)

        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

