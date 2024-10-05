import json
import logging as logger
from urllib import response
import healthkg.utils.logs.config as logconfig
from healthkg.modules.worker.utils.convert_float_to_int_dict import convert_float_to_int_dict
from google.protobuf import json_format 
from google.protobuf.json_format import MessageToDict
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from jio.brain.proto.knowledge.healthcare.req_res.get_disease_pb2 import GetDiseaseResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
import copy

class GetDiseaseWorker:

    def __init__(self):
        '''
        __init__ is the constructor for a class. 
        The self parameter refers to the instance of the object 
        '''
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING) 

        transform_request_status = copy.deepcopy(status)
        if not request.disease_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request = None

        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        response = dispatcher.get_metadata(id = request.disease_id)
        response, dispatcher_status = validate_kg_response(response)
        if not response:
            return None, dispatcher_status
        return response, dispatcher_status

    def transform_response(self, response, status):
                                          
        logger.debug(logconfig.POSTPROCESSING)

        if not response:
            response = GetDiseaseResponse(status = status)
        else:
            response_obj = MessageToDict(response.metadata, preserving_proto_field_name=True)
            if 'entity_type' not in response_obj or response_obj['entity_type'].split('_')[1] != "disease":
                transfrom_response_status = copy.deepcopy(status)
                transfrom_response_status['is_ok'] = False
                transfrom_response_status['status_message'] = "Not of proper healthcare_disease type"
                response = GetDiseaseResponse(status = transfrom_response_status)
            else:
                response_obj = convert_float_to_int_dict(response_obj)
                del response_obj['attributes']
                del response_obj['query']
                response = GetDiseaseResponse(disease = response_obj, status = status)

        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

