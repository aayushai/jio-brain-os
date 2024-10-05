import ast
import logging as logger
import healthkg.utils.logs.config as logconfig
from google.protobuf import json_format 
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response 
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.healthcare.req_res.get_attribute_bucket_in_disease_pb2 import GetAttributeBucketInDiseaseResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
from healthkg.modules.worker.utils.query import *
import copy

class GetAttributeBucketInDiseaseWorker:

    def __init__(self):
        '''
        __init__ is the constructor for a class. 
        The self parameter refers to the instance of the object 
        '''
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)

        transform_request_status = copy.deepcopy(status)
        if not request.disease_id or not request.symptom_id or not request.attribute_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request_object = None
        else:
            request_object = { 
            "get_symptom_ids": query_get_symptom_given_disease%(request.disease_id),
            "get_attribute_bucket" : {
                "edge_collection": "has_attribute",
                "from_id": request.symptom_id, 
                "to_id": request.attribute_id 
            }
        }

        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()

        graph_query_response = dispatcher.graph_query(request["get_symptom_ids"])
        graph_query_response, dispatcher_status = validate_kg_response(graph_query_response)
        if not graph_query_response:
            return None, dispatcher_status

        symptom_ids = ast.literal_eval(graph_query_response.cursor)
        symptom_id = request["get_attribute_bucket"]['from_id']
        
        if symptom_id in symptom_ids:
            get_edge_response = dispatcher.get_edge(**request["get_attribute_bucket"])
            get_edge_response, dispatcher_status = validate_kg_response(get_edge_response)
            return get_edge_response, dispatcher_status
        else:
            dispatcher_status['is_ok'] = False
            dispatcher_status['status_message'] = "Symptom id does not exist for the given disease id"
            return None, dispatcher_status

    def transform_response(self, response, status):

        logger.debug(logconfig.POSTPROCESSING)

        if not response:
            response = GetAttributeBucketInDiseaseResponse(status = status)
        else:
            response = int(response.edge['bucket'])
            response = GetAttributeBucketInDiseaseResponse(bucket = response, status = status)
            
        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

