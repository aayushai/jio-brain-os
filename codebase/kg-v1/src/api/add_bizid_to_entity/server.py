from jio.brain.proto.knowledge.api.data.add_bizid_to_entity_pb2_grpc import(
	AddBizIdToEntityServiceServicer, # Base class for generated servicer 
	add_AddBizIdToEntityServiceServicer_to_server # generated rpc handler	
)

from servings.grpc.service import serve 
from api.add_bizid_to_entity.config import (
	MAX_WORKERS,
	SERVER_PORT,
	API_NAME
)
from logs.log import get_logger
from servings.grpc.service import serve 
from db.generic.dao.query_handler import init, execute

logger = get_logger("root", API_NAME)

class Servicer(AddBizIdToEntityServiceServicer):
	def serve(self, request, context):
		logger.debug("request sent from serve method " + str(request))
		return execute(
				request = request
			)
			

if __name__ == "__main__":
	init(api_name=API_NAME)
	serve(
			rpc_handler = add_AddBizIdToEntityServiceServicer_to_server,
			servicer = Servicer,
			port = SERVER_PORT,
			max_workers = MAX_WORKERS
		)