import ast
import json
import logging as logger
import re
import healthkg.utils.logs.config as logconfig
from healthkg.modules.worker.utils.get_common_response_objs import get_common_response_objs
from google.protobuf import json_format 
from google.protobuf.json_format import MessageToDict
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from jio.brain.proto.knowledge.healthcare.req_res.search_diseases_pb2 import SearchDiseasesResponse
from healthkg.modules.worker.utils.get_age_group_id import get_age_group_id
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
import copy

class SearchDiseasesWorker:

    def __init__(self):
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)

        transform_request_status = copy.deepcopy(status)
        if not request.keyword:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request_object = None
        else:        
            request_object = {"entity_type": "disease",
                              "keyword": request.keyword,
                              "age": list(request.age),
                              "context_ids": list(request.gender)} 
            if request_object['context_ids'] == []:
                request_object['context_ids'] = [None]
        
        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()

        if request['age']:
            age_group_ids = get_age_group_id(dispatcher, request['age'])

            if not age_group_ids:
                dispatcher_status = copy.deepcopy(status)
                dispatcher_status['is_ok'] = False
                dispatcher_status['status_message'] = "Modelling error (age group not found)"
                return None, dispatcher_status

            request["context_ids"] += age_group_ids
        
        search_response = []
        for context_id in request["context_ids"]:            
            dispatcher_request = {"entity_type": request["entity_type"],
                                  "keyword": request["keyword"],
                                  "context_id": context_id}
            dispatcher_response = dispatcher.search_entity_by_context(dispatcher_request)
            dispatcher_response, dispatcher_status = validate_kg_response(dispatcher_response)
            if not dispatcher_response:
                return None, dispatcher_status
            search_response.append(dispatcher_response)
        
        return search_response, dispatcher_status

    def transform_response(self, response, status):
                                                   
        logger.debug(logconfig.POSTPROCESSING) 

        if not response:
            response = SearchDiseasesResponse(status = status)
        else:
            response_obj = get_common_response_objs(response, "search_response")
            response = SearchDiseasesResponse(search_response = response_obj, status = status)
        
        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

