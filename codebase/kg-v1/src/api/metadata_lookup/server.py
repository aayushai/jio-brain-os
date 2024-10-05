from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2_grpc import(
	MetadataLookupServiceServicer, # Base class for generated servicer 
	add_MetadataLookupServiceServicer_to_server # generated rpc handler	
)

from api.metadata_lookup.config import (
	MAX_WORKERS,
	SERVER_PORT,
	API_NAME
)

from servings.grpc.service import serve
from db.generic.dao.query_handler import init, execute
from logs.log import get_logger

logger = get_logger("root", API_NAME)

class Servicer(MetadataLookupServiceServicer):

	def serve(self, request, context):
		logger.debug("request sent from serve method " + str(request))
		#request is sent to the generic query handler
		return execute(
			request = request
		)

if __name__ == "__main__":
	init(api_name=API_NAME)
	serve(
			rpc_handler = add_MetadataLookupServiceServicer_to_server,
			servicer = Servicer,
			port = SERVER_PORT,
			max_workers = MAX_WORKERS
		)