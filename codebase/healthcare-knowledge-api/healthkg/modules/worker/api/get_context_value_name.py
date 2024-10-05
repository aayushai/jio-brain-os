import json
import logging as logger
import healthkg.utils.logs.config as logconfig
from google.protobuf import json_format 
from healthkg.modules.worker.utils.config import status 
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.healthcare.req_res.get_context_value_name_pb2 import GetContextValueNameResponse
from healthkg.modules.dispatcher.kg_dispatcher import KGDispatcher
import copy

class GetContextValueNameWorker:

    def __init__(self):
        pass

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)

        transform_request_status = copy.deepcopy(status)
        if not request.context_id or not request.value_id:
            transform_request_status['is_ok'] = False
            transform_request_status['status_message'] = "Check request parameters"
            request_object = None
        else:
            request_object = {"context_id": request.context_id,
                              "value_id": request.value_id}

        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return request_object, transform_request_status

    def do(self, request, status):
        dispatcher = KGDispatcher()
        response = dispatcher.get_context_value_name(request)
        response, dispatcher_status = validate_kg_response(response)
        if not response:
            return None, dispatcher_status
        return response, dispatcher_status

    def transform_response(self, response, status):
                                                   
        logger.debug(logconfig.POSTPROCESSING)

        if not response:
            response = GetContextValueNameResponse(status = status)
        else:
            response = MessageToDict(response, preserving_proto_field_name=True)
            response = GetContextValueNameResponse(context_value_name = response['context_value_name'], status = status)

        logger.debug(logconfig.POSTPROCESSING_COMPLETED)

        return response

