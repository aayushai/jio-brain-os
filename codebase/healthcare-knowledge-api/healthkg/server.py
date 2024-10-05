import os
from concurrent import futures
from dotenv import load_dotenv

import grpc
import jio.brain.proto.knowledge.healthcare.api.healthcare_kg_service_pb2_grpc as healthcare_knowledge_service

from healthkg.utils.logs.logger import get_logger
from healthkg.modules.manager.service_manager import execute

logger = get_logger("root", "server")

'''
HealthcareKnowledgeApiService is a subclass of HealthcareKnowledgeApiServiceServicer
class generated in healthcare_kg_service_pb2_grpc
	i/p: API specific request
	o/p: API specific response
'''
class HealthcareKnowledgeApiService(healthcare_knowledge_service.HealthcareKnowledgeApiServiceServicer):
	'''
	i/p: None
	o/p: List of Disease ID and Name
	'''
	def GetAllDisease(self, request, context):
		logger.debug("GetAllDisease request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_ALL_DISEASE'),
			request = request
		)

	def GetDisease(self, request, context):
		logger.debug("GetDisease request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_DISEASE'),
			request = request
		)

	def GetAllSymptom(self, request, context):
		logger.debug("GetAllSymptom request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_ALL_SYMPTOM'),
			request = request
		)

	def GetSymptom(self, request, context):
		logger.debug("GetSymptom request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_SYMPTOM'),
			request = request
		)

	def GetAttribute(self, request, context):
			logger.debug("GetAttribute request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_ATTRIBUTE'),
				request = request
			)

	def GetAttributeId(self, request, context):
			logger.debug("GetAttributeId request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_ATTRIBUTE_ID'),
				request = request
			)

	def GetAttributeValueId(self, request, context):
			logger.debug("GetAttributeValueId request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_ATTRIBUTE_VALUE_ID'),
				request = request
			)


	def GetAttributeOrder(self, request, context):
			logger.debug("GetAttributeOrder request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_ATTRIBUTE_ORDER'),
				request = request
			)

	def GetAttributeName(self, request, context):
			logger.debug("GetAttributeName request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_ATTRIBUTE_NAME'),
				request = request
			)

	def GetAttributeValue(self, request, context):
			logger.debug("GetAttribute request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_ATTRIBUTE_VALUE'),
				request = request
			)

	def GetContext(self, request, context):
		logger.debug("GetContext request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_CONTEXT'),
			request = request
		)

	def GetContextValueId(self, request, context):
		logger.debug("GetContextValueId request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_CONTEXT_VALUE_ID'),
			request = request
		)

	def GetDiseaseGivenSymptom(self, request, context):
		logger.debug("GetDiseaseGivenSymptom request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_DISEASE_GIVEN_SYMPTOM'),
			request = request
		)

	def GetSymptomGivenDisease(self, request, context):
		logger.debug("GetSymptomGivenDisease request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_SYMPTOM_GIVEN_DISEASE'),
			request = request
		)

	def GetSymptomBucketInDisease(self, request, context):
		logger.debug("GetSymptomBucketInDisease request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_SYMPTOM_BUCKET_IN_DISEASE'),
			request = request
		)

	def GetHighestAttributeBucket(self, request, context):
		logger.debug("GetHighestAttributeBucket request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_HIGHEST_ATTRIBUTE_BUCKET'),
			request = request
		)

	def GetAttributeBucketInDisease(self, request, context):
		logger.debug("GetAttributeBucketInDisease request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_ATTRIBUTE_BUCKET_IN_DISEASE'),
			request = request
		)

	def GetAttributesOfSymptomAndDisease(self, request, context):
		logger.debug("GetAttributesOfSymptomAndDisease request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_ATTRIBUTES_OF_SYMPTOM_AND_DISEASE'),
			request = request
		)

	def GetSymptomId(self, request, context):
			logger.debug("GetSymptomId request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_SYMPTOM_ID'),
				request = request
			)

	def GetDiseaseId(self, request, context):
			logger.debug("GetDiseaseId request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_DISEASE_ID'),
				request = request
			)

	def GetContextId(self, request, context):
			logger.debug("GetContextId request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_CONTEXT_ID'),
				request = request
			)

	def SearchSymptoms(self, request, context):
			logger.debug("SearchSymptoms request received in servicer")
			return execute(
				api_name = os.getenv('API.SEARCH_SYMPTOMS'),
				request = request
			)

	def GetSymptomPatientState(self, request, context):
			logger.debug("GetSymptomPatientState request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_SYMPTOM_PATIENT_STATE'),
				request = request
			)

	def GetDiseasePatientState(self, request, context):
			logger.debug("GetDiseasePatientState request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_DISEASE_PATIENT_STATE'),
				request = request
			)

	def SearchDiseases(self, request, context):
			logger.debug("SearchDiseases request received in servicer")
			return execute(
				api_name = os.getenv('API.SEARCH_DISEASES'),
				request = request
			)

	def GetValidSymptomAttributeValuesGivenFilter(self, request, context):
			logger.debug("GetValidSymptomAttributeValuesGivenFilter request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_VALID_SYMPTOM_ATTRIBUTE_VALUES_GIVEN_FILTER'),
				request = request
			)

	def GetDiseaseName(self, request, context):
			logger.debug("GetDiseaseName request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_DISEASE_NAME'),
				request = request
			)

	def GetSymptomName(self, request, context):
			logger.debug("GetSymptomName request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_SYMPTOM_NAME'),
				request = request
			)

	def GetContextName(self, request, context):
			logger.debug("GetContextName request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_CONTEXT_NAME'),
				request = request
			)
	
	def GetAttributeValueName(self, request, context):
			logger.debug("GetAttributeValueName request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_ATTRIBUTE_VALUE_NAME'),
				request = request
			)

	def GetContextValueName(self, request, context):
			logger.debug("GetContextValueName request received in servicer")
			return execute(
				api_name = os.getenv('API.GET_CONTEXT_VALUE_NAME'),
				request = request
			)


def start(max_workers=5, server_port="3150"):
	'''
	Start Method starts the Healthcare Knowledge API Server
	'''
	load_dotenv()
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
	healthcare_knowledge_service.add_HealthcareKnowledgeApiServiceServicer_to_server(HealthcareKnowledgeApiService(), server)
	server.add_insecure_port('[::]:{}'.format(server_port))
	server.start()
	# TODO: Use logger
	print('Starting server. Listening on port {} with {} workers'.format(server_port, max_workers))
	server.wait_for_termination()

if __name__ == "__main__":
	load_dotenv()
	max_workers = int(os.getenv('MAX_WORKERS'))
	server_port = str(os.getenv('SERVER_PORT'))
	start(max_workers=max_workers, server_port=server_port)
