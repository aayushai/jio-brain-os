from jio.brain.proto.knowledge.api.data.delete_canonical_name_pb2_grpc import(
	DeleteCanonicalNameServiceServicer, # Base class for generated servicer 
	add_DeleteCanonicalNameServiceServicer_to_server # generated rpc handler	
)

from api.delete_canonical_name.config import (
	MAX_WORKERS,
	SERVER_PORT,
	API_NAME
)

from servings.grpc.service import serve
from db.generic.dao.query_handler import init, execute
from logs.log import get_logger
logger = get_logger("root", API_NAME)

class Servicer(DeleteCanonicalNameServiceServicer):
	def serve( self, request, context):
		logger.debug("request sent from serve method " + str(request))
		return execute(
				request = request
			)

if __name__ == "__main__":
	init(api_name=API_NAME)
	serve(
			rpc_handler = add_DeleteCanonicalNameServiceServicer_to_server,
			servicer = Servicer,
			port = SERVER_PORT,
			max_workers = MAX_WORKERS
		)