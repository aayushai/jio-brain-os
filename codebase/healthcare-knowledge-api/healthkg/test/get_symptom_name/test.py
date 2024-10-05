from jio.brain.proto.knowledge.healthcare.req_res.get_symptom_name_pb2 import GetSymptomNameRequest
from jio.brain.proto.knowledge.healthcare.api.healthcare_kg_service_pb2_grpc import HealthcareKnowledgeApiServiceStub

import os
import json
import grpc
from healthkg.utils.logs.logger import get_logger

logger = get_logger("root", "get_symptom_name")

channel = grpc.insecure_channel(f"localhost:31050")

stub = HealthcareKnowledgeApiServiceStub(channel)

def test():
    logger.debug("Entered test method")
    try:
        request = GetSymptomNameRequest(symptom_id=21)
        response = stub.GetSymptomName(request)
        logger.debug("Testing complete")
        return response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test()
    print(api_response)