import os
import json

import grpc
from jio.brain.proto.knowledge.healthcare.req_res.get_all_symptom_pb2 import GetAllSymptomRequest
from jio.brain.proto.knowledge.healthcare.api.healthcare_kg_service_pb2_grpc import HealthcareKnowledgeApiServiceStub


from healthkg.utils.logs.logger import get_logger
from healthkg.utils.util import local_channel

logger = get_logger("root", "get_all_symptom")
stub = HealthcareKnowledgeApiServiceStub(local_channel)

def test():
    logger.debug("Entered test method")
    try:
        request = GetAllSymptomRequest() 
        response = stub.GetAllSymptom(request)
        logger.debug("Testing complete")
        return response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test()
    print(api_response)
