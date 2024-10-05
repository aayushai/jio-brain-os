import ast
import logging as logger
import healthkg.utils.logs.config as logconfig
from google.protobuf import json_format 
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.healthcare.req_res.get_symptom_given_disease_pb2 import GetSymptomGivenDiseaseResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
from healthkg.modules.worker.utils.query import *
import copy

class GetSymptomGivenDiseaseWorker:

    def __init__(self):
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)

        transform_request_status = copy.deepcopy(status)

        if not request.disease_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request_object = None
        else:
            queries = []
            for i in request.disease_id:
                queries.append(query_get_symptom_given_disease%(i))
            request_object = queries

        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        response = []
        for i in request:
            dispatcher_response = dispatcher.graph_query(i)
            dispatcher_response, dispatcher_status = validate_kg_response(dispatcher_response)
            if not dispatcher_response:
                return None, dispatcher_status
            response.append(dispatcher_response)
        return response, dispatcher_status

    def transform_response(self, response, status):

        logger.debug(logconfig.POSTPROCESSING)

        if not response:
            response = GetSymptomGivenDiseaseResponse(status = status)
        else:
            response_obj = []
            for i in response:
                response_obj.append(set(ast.literal_eval(i.cursor)))
            response_obj = set.union(*response_obj)
            response = GetSymptomGivenDiseaseResponse(symptom_id = response_obj, status = status)
        
        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

