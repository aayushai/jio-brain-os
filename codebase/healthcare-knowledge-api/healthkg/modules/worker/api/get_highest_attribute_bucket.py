import ast
import logging as logger
import healthkg.utils.logs.config as logconfig
from google.protobuf import json_format 
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.healthcare.req_res.get_highest_attribute_bucket_pb2 import GetHighestAttributeBucketResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
from healthkg.modules.worker.utils.query import *
import copy

class GetHighestAttributeBucketWorker:

    def __init__(self):
        '''
        __init__ is the constructor for a class. 
        The self parameter refers to the instance of the object 
        '''
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)        
        request_object = query_get_highest_attribute_bucket
        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        response = dispatcher.graph_query(request)
        response, dispatcher_status = validate_kg_response(response)
        if not response:
            return None, dispatcher_status
        return response, dispatcher_status

    def transform_response(self, response, status):

        logger.debug(logconfig.POSTPROCESSING)

        if not response:
            response = GetHighestAttributeBucketResponse(status = status)
        else:
            response_obj = ast.literal_eval(response.cursor)[0]
            response = GetHighestAttributeBucketResponse(bucket = response_obj, status = status)
        
        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

