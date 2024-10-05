from jio.brain.proto.knowledge.healthcare.req_res.get_symptom_given_disease_pb2 import GetSymptomGivenDiseaseRequest
from jio.brain.proto.knowledge.healthcare.api.healthcare_kg_service_pb2_grpc import HealthcareKnowledgeApiServiceStub

import os
import json
import grpc
from healthkg.utils.logs.logger import get_logger

logger = get_logger("root", "get_symptom_given_disease")

channel = grpc.insecure_channel(f"localhost:31050")

stub = HealthcareKnowledgeApiServiceStub(channel)

def test(disease_id):
    logger.debug("Entered test method")
    try:
        request = GetSymptomGivenDiseaseRequest(
            disease_id = disease_id
        ) 
        response = stub.GetSymptomGivenDisease(request)
        logger.debug("Testing complete")
        return response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test([14, 11])
    print(api_response)