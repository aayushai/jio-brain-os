from jio.brain.proto.knowledge.healthcare.req_res.get_valid_symptom_attribute_values_given_filter_pb2 import GetValidSymptomAttributeValuesGivenFilterRequest
from jio.brain.proto.knowledge.healthcare.api.healthcare_kg_service_pb2_grpc import HealthcareKnowledgeApiServiceStub

import os
import json
import grpc
from healthkg.utils.logs.logger import get_logger

logger = get_logger("root", "get_valid_symptom_attribute_values_given_filter")

channel = grpc.insecure_channel(f"localhost:31050")

stub = HealthcareKnowledgeApiServiceStub(channel)

def test(symptom_id, attribute_id, gender, age):
    logger.debug("Entered test method")
    try:
        request = GetValidSymptomAttributeValuesGivenFilterRequest(symptom_id = symptom_id,
                                                                    attribute_id = attribute_id,
                                                                    gender = gender,
                                                                    age = age)
        response = stub.GetValidSymptomAttributeValuesGivenFilter(request)
        logger.debug("Testing complete")
        return response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test(21, 211, 311, 45)
    print(api_response)