import importlib
import logging as logger
from healthkg.utils.logs import config as logconfig

from healthkg.modules.worker.api.get_all_disease import GetAllDiseaseWorker
from healthkg.modules.worker.api.get_disease import GetDiseaseWorker
from healthkg.modules.worker.api.get_all_symptom import GetAllSymptomWorker
from healthkg.modules.worker.api.get_symptom import GetSymptomWorker
from healthkg.modules.worker.api.get_context import GetContextWorker
from healthkg.modules.worker.api.get_attribute import GetAttributeWorker
from healthkg.modules.worker.api.get_attribute_value import GetAttributeValueWorker
from healthkg.modules.worker.api.get_disease_given_symptom import GetDiseaseGivenSymptomWorker
from healthkg.modules.worker.api.get_symptom_given_disease import GetSymptomGivenDiseaseWorker
from healthkg.modules.worker.api.get_attribute_order import GetAttributeOrderWorker
from healthkg.modules.worker.api.get_attribute_id import GetAttributeIdWorker
from healthkg.modules.worker.api.get_attribute_value_id import GetAttributeValueIdWorker
from healthkg.modules.worker.api.get_attribute_name import GetAttributeNameWorker
from healthkg.modules.worker.api.get_symptom_bucket_in_disease import GetSymptomBucketInDiseaseWorker
from healthkg.modules.worker.api.get_highest_attribute_bucket import GetHighestAttributeBucketWorker
from healthkg.modules.worker.api.get_attribute_bucket_in_disease import GetAttributeBucketInDiseaseWorker
from healthkg.modules.worker.api.get_attributes_of_symptom_and_disease import GetAttributesOfSymptomAndDiseaseWorker
from healthkg.modules.worker.api.get_symptom_id import GetSymptomIdWorker
from healthkg.modules.worker.api.get_disease_id import GetDiseaseIdWorker
from healthkg.modules.worker.api.get_context_value_id import GetContextValueIdWorker
from healthkg.modules.worker.api.get_context_id import GetContextIdWorker
from healthkg.modules.worker.api.search_symptoms import SearchSymptomsWorker
from healthkg.modules.worker.api.get_symptom_patient_state import GetSymptomPatientStateWorker
from healthkg.modules.worker.api.get_disease_patient_state import GetDiseasePatientStateWorker
from healthkg.modules.worker.api.search_diseases import SearchDiseasesWorker
from healthkg.modules.worker.api.get_valid_symptom_attribute_values_given_filter import GetValidSymptomAttributeValuesGivenFilterWorker
from healthkg.modules.worker.api.get_symptom_name import GetSymptomNameWorker
from healthkg.modules.worker.api.get_disease_name import GetDiseaseNameWorker
from healthkg.modules.worker.api.get_context_name import GetContextNameWorker
from healthkg.modules.worker.api.get_attribute_value_name import GetAttributeValueNameWorker
from healthkg.modules.worker.api.get_context_value_name import GetContextValueNameWorker


def worker_factory(api_name):
    '''
    Factory Methods for Knowledge Graph Service Workers
    '''
    workers = {
        "GetAllDisease": GetAllDiseaseWorker,
        "GetDisease": GetDiseaseWorker,
        "GetAllSymptom": GetAllSymptomWorker,
        "GetSymptom": GetSymptomWorker,
        "GetAttribute": GetAttributeWorker,
        "GetAttributeValue": GetAttributeValueWorker,
        "GetDiseaseGivenSymptom": GetDiseaseGivenSymptomWorker,
        "GetSymptomGivenDisease": GetSymptomGivenDiseaseWorker,
        "GetAttributeOrder": GetAttributeOrderWorker,
        "GetAttributeName": GetAttributeNameWorker,
        "GetSymptomBucketInDisease" : GetSymptomBucketInDiseaseWorker,
        "GetAttributeId" : GetAttributeIdWorker,
        "GetAttributeValueId" : GetAttributeValueIdWorker,
        "GetHighestAttributeBucket" : GetHighestAttributeBucketWorker,
        "GetAttributeBucketInDisease" : GetAttributeBucketInDiseaseWorker,
        "GetAttributesOfSymptomAndDisease" : GetAttributesOfSymptomAndDiseaseWorker,
        "GetSymptomId" : GetSymptomIdWorker,
        "GetDiseaseId" : GetDiseaseIdWorker,
        "GetContext": GetContextWorker,
        "GetContextValueId": GetContextValueIdWorker,
        "GetContextId": GetContextIdWorker,
        "SearchSymptoms": SearchSymptomsWorker,
        "GetSymptomPatientState": GetSymptomPatientStateWorker,
        "GetDiseasePatientState": GetDiseasePatientStateWorker,
        "SearchDiseases": SearchDiseasesWorker,
        "GetValidSymptomAttributeValuesGivenFilter": GetValidSymptomAttributeValuesGivenFilterWorker,
        "GetSymptomName" : GetSymptomNameWorker,
        "GetDiseaseName" : GetDiseaseNameWorker,
        "GetContextName": GetContextNameWorker,
       # "GetSymptomsID": SearchSymptomsWorker,
        "GetAttributeValueName": GetAttributeValueNameWorker,
        "GetContextValueName": GetContextValueNameWorker
    }

    return workers[api_name]()

def execute(request, api_name):
    logger.debug(logconfig.EXECUTE)
    knowledge_service_response = None
    worker = worker_factory(api_name)

    knowledge_service_request, status = worker.transform_request(request)

    if status['is_ok'] == False:
        logger.error(status)
        knowledge_service_response = None
        return worker.transform_response(
            knowledge_service_response,
            status
        )

    knowledge_service_response, status = worker.do(knowledge_service_request, status)

    if status['is_ok'] == False:
        logger.error(status)
        knowledge_service_response = None
        return worker.transform_response(
            knowledge_service_response,
            status
        )

    logger.debug(logconfig.EXECUTED)

    return worker.transform_response(
        knowledge_service_response,
        status
    )
