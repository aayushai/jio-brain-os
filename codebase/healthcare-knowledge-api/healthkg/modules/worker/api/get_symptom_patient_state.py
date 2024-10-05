import json
import logging as logger
import healthkg.utils.logs.config as logconfig
from google.protobuf import json_format 
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.healthcare.req_res.get_symptom_patient_state_pb2 import GetSymptomPatientStateResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
import copy

class GetSymptomPatientStateWorker:

    def __init__(self):
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)

        transform_request_status = copy.deepcopy(status)
        if not request.symptom_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request_object = None
        else:
            request_object={"entity_id": request.symptom_id}

        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        response = dispatcher.get_entity_context(request)
        response, dispatcher_status = validate_kg_response(response)
        if not response:
            return None, dispatcher_status
        return response, dispatcher_status

    def transform_response(self, response, status):
                                                   
        logger.debug(logconfig.POSTPROCESSING) 

        if not response:
            response = GetSymptomPatientStateResponse(status = status)
        else:
            gender = []
            minimum_age = []
            maximum_age = []

            for i in response.entity_context:
                if i.context_type == 'gender':
                    gender.append(i.id)
                elif i.context_type == 'age':
                    minimum_age.append(i.minimum)
                    maximum_age.append(i.maximum)

            if not gender or not maximum_age or not minimum_age:
                transform_response_status = copy.deepcopy(status)
                transform_response_status['is_ok'] = False
                transform_response_status['status_message'] = "Modelling error (gender or age not present)"
                response = GetSymptomPatientStateResponse(status = transform_response_status)
            else:
                response = GetSymptomPatientStateResponse(gender = gender,
                                                          minimum_age = min(minimum_age), maximum_age = max(maximum_age), 
                                                          status = status)

        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

