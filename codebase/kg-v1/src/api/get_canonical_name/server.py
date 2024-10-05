from jio.brain.proto.knowledge.api.data.get_canonical_name_pb2_grpc import(
	GetCanonicalNameServiceServicer, # Base class for generated servicer 
	add_GetCanonicalNameServiceServicer_to_server # generated rpc handler	
)

from servings.grpc.service import serve
from db.generic.dao.query_handler import init, execute
from api.get_canonical_name.config import *
from logs.log import get_logger

logger = get_logger("root", API_NAME)

class Servicer(GetCanonicalNameServiceServicer):

	def serve(self, request, context):
		logger.debug("request sent from serve method " + str(request))
		#request is sent to the generic query handler

		return execute(
			request = request,
		)

if __name__ == "__main__":
	'''
	server method starts the get_entity server
	'''
	init(api_name=API_NAME)
	serve(
			rpc_handler = add_GetCanonicalNameServiceServicer_to_server,
			servicer = Servicer,
			port = SERVER_PORT,
			max_workers = MAX_WORKERS
		)