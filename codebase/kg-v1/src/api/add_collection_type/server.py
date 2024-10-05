from jio.brain.proto.knowledge.api.schema.add_collection_type_pb2_grpc import(
	AddCollectionTypeServiceServicer, # Base class for generated servicer 
	add_AddCollectionTypeServiceServicer_to_server # generated rpc handler	
)

from api.add_collection_type.config import (
	MAX_WORKERS,
	SERVER_PORT,
	API_NAME
)

from logs.log import get_logger
from servings.grpc.service import serve 
from db.generic.dao.query_handler import init, execute

init(api_name=API_NAME)

logger = get_logger("root", API_NAME)

class Servicer(AddCollectionTypeServiceServicer):
	def serve(self, request, context):
		logger.debug("request sent from serve method " + str(request))
		return execute(
				request = request
			)
			

if __name__ == "__main__":
	init(api_name=API_NAME)
	serve(
			rpc_handler = add_AddCollectionTypeServiceServicer_to_server,
			servicer = Servicer,
			port = SERVER_PORT,
			max_workers = MAX_WORKERS
		)