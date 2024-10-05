from healthkg.modules.worker.utils.config import status 
from google.protobuf.json_format import MessageToDict
import copy

def validate_kg_response(kg_response):
    is_ok = kg_response.status.is_ok
    message = MessageToDict(kg_response.status, preserving_proto_field_name=True)
    status_message = message['brain_status_instance'][0]['parameters']['msg']
    validator_status = copy.deepcopy(status) 
    if  is_ok != True:
        validator_status['is_ok'] = False
        validator_status['status_message'] = status_message
        return None, validator_status
    return kg_response, validator_status