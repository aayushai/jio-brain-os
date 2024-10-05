import json
import logging as logger
import healthkg.utils.logs.config as logconfig
from google.protobuf import json_format 
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from healthkg.modules.worker.utils.map_keys import map_keys
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.healthcare.req_res.get_attribute_value_pb2 import GetAttributeValueResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
import copy

class GetAttributeValueWorker:

    def __init__(self):
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)

        transform_request_status = copy.deepcopy(status)
        if not request.symptom_id or not request.attribute_id or not request.value_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request_object = None
        else:
            request_object = {"from_node_id": request.symptom_id, 
                         "to_node_id": request.attribute_id, 
                         "value_id": request.value_id}

        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        response = dispatcher.get_attribute_value(request)
        response, dispatcher_status = validate_kg_response(response)
        if not response:
            return None, dispatcher_status
        return response, dispatcher_status

    def transform_response(self, response, status):
                                                   
        logger.debug(logconfig.POSTPROCESSING) 
        if not response:
            response = GetAttributeValueResponse(status = status)
        else:
            response = MessageToDict(response, preserving_proto_field_name=True)
            response = map_keys(response, 'value', 'related', 'diseases')
            response = GetAttributeValueResponse(value = response['value'], status = status)

        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

