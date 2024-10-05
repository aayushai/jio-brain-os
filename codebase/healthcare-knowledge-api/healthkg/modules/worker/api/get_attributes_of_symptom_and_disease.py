import ast
import logging as logger
import healthkg.utils.logs.config as logconfig
from google.protobuf import json_format 
from google.protobuf.json_format import MessageToDict
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from healthkg.modules.worker.utils.get_common_response_objs import get_common_response_objs
from jio.brain.proto.knowledge.healthcare.req_res.get_attributes_of_symptom_and_disease_pb2 import GetAttributesOfSymptomAndDiseaseResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
from healthkg.modules.worker.utils.query import *
import copy

class GetAttributesOfSymptomAndDiseaseWorker:

    def __init__(self):
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)

        transform_request_status = copy.deepcopy(status)
        if not request.symptom_id or not request.disease_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request_object = None
        else:
            queries = []
            symptom_id = request.symptom_id
            for i in request.disease_id:
                queries.append(query_get_attributes_of_symptom_and_disease%(i, symptom_id))
        
            request_object = queries

        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        response = []
        for query in request:
            graph_query_response = dispatcher.graph_query(query)
            graph_query_response, dispatcher_status = validate_kg_response(graph_query_response)
            if not graph_query_response:
                return None, dispatcher_status
            response.append(graph_query_response)
        return response, dispatcher_status

    def transform_response(self, response, status):

        logger.debug(logconfig.POSTPROCESSING)

        if not response:
            response = GetAttributesOfSymptomAndDiseaseResponse(status = status)
        else:
            response_obj = get_common_response_objs(response, "cursor")
            response = GetAttributesOfSymptomAndDiseaseResponse(attributes = response_obj, status = status)
        
        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

