import json
import logging as logger
import healthkg.utils.logs.config as logconfig
from healthkg.modules.worker.utils.convert_float_to_int_dict import convert_float_to_int_dict
from google.protobuf import json_format 
from google.protobuf.json_format import MessageToDict
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from jio.brain.proto.knowledge.healthcare.req_res.get_symptom_pb2 import GetSymptomResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
import copy

class GetSymptomWorker:

    def __init__(self):
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)   

        transform_request_status = copy.deepcopy(status)
        if not request.symptom_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request = None

        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        response = dispatcher.get_metadata(id = request.symptom_id)
        response, dispatcher_status = validate_kg_response(response)
        if not response:
            return None, dispatcher_status
        return response, dispatcher_status

    def transform_response(self, response, status):
                                                   
        logger.debug(logconfig.POSTPROCESSING)

        if not response:
            response = GetSymptomResponse(status = status)
        else:
            response_obj = MessageToDict(response.metadata, preserving_proto_field_name=True)
            if 'entity_type' not in response_obj or response_obj['entity_type'].split('_')[1] != "symptom":
                transfrom_response_status = copy.deepcopy(status)
                transfrom_response_status['is_ok'] = False
                transfrom_response_status['status_message'] = "Not of proper healthcare_symptom type"
                response = GetSymptomResponse(status = transfrom_response_status)
            else:
                response_obj = convert_float_to_int_dict(response_obj)
                response = GetSymptomResponse(symptom = response_obj, status = status)

        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

