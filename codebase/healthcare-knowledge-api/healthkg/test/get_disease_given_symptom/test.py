from jio.brain.proto.knowledge.healthcare.req_res.get_disease_given_symptom_pb2 import GetDiseaseGivenSymptomRequest
from jio.brain.proto.knowledge.healthcare.api.healthcare_kg_service_pb2_grpc import HealthcareKnowledgeApiServiceStub

import os
import json
import grpc
from healthkg.utils.logs.logger import get_logger

logger = get_logger("root", "get_disease_given_symptom")

channel = grpc.insecure_channel(f"localhost:31050")

stub = HealthcareKnowledgeApiServiceStub(channel)

def test(symptom_id):
    logger.debug("Entered test method")
    try:
        request = GetDiseaseGivenSymptomRequest(
            symptom_id = symptom_id
        ) 
        response = stub.GetDiseaseGivenSymptom(request)
        logger.debug("Testing complete")
        return response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test([21, 22])
    print(api_response)