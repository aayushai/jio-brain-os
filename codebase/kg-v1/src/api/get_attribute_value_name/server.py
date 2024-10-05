from jio.brain.proto.knowledge.api.data.get_attribute_value_name_pb2_grpc import(
	GetAttributeValueNameServiceServicer, # Base class for generated servicer 
	add_GetAttributeValueNameServiceServicer_to_server # generated rpc handler	
)

from servings.grpc.service import serve
from db.generic.dao.query_handler import init, execute
from api.get_attribute_value_name.config import *
from logs.log import get_logger

logger = get_logger("root", API_NAME)
'''
Client request lands here
serve method sends the request to the generic query handler
i/p: request
o/p: GetAttributeValueNameAPI response
'''

class Servicer(GetAttributeValueNameServiceServicer):

	def serve(self, request, context):
		logger.debug("request sent from serve method " + str(request))
		#request is sent to the generic query handler

		return execute(
			request = request,
		)

if __name__ == "__main__":
	'''
	server method starts the get_attribute_value_name server
	'''
	init(api_name=API_NAME)
	serve(
			rpc_handler = add_GetAttributeValueNameServiceServicer_to_server,
			servicer = Servicer,
			port = SERVER_PORT,
			max_workers = MAX_WORKERS
		)