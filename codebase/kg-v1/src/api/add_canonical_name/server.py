from jio.brain.proto.knowledge.api.data.add_canonical_name_pb2_grpc import(
	AddCanonicalNameServiceServicer, # Base class for generated servicer 
	add_AddCanonicalNameServiceServicer_to_server # generated rpc handler	
)

from servings.grpc.service import serve 
from api.add_canonical_name.config import (
	MAX_WORKERS,
	SERVER_PORT,
	API_NAME
)
from logs.log import get_logger
from servings.grpc.service import serve 
from db.generic.dao.query_handler import init, execute

logger = get_logger("root", API_NAME)

class Servicer(AddCanonicalNameServiceServicer):
	def serve(self, request, context):
		logger.debug("request sent from serve method " + str(request))
		return execute(
				request = request
			)
			

if __name__ == "__main__":
	init(api_name=API_NAME)
	serve(
			rpc_handler = add_AddCanonicalNameServiceServicer_to_server,
			servicer = Servicer,
			port = SERVER_PORT,
			max_workers = MAX_WORKERS
		)