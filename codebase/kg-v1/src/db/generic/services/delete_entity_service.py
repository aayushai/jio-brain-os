import grpc
from retry import retry
import logging as logger
from db.generic.utils.config import *
from jio.brain.proto.knowledge.api.data.delete_entity_pb2 import DeleteEntityRequest
from jio.brain.proto.knowledge.api.data.delete_entity_pb2_grpc import DeleteEntityServiceStub

channel = grpc.insecure_channel(delete_entity_host)
stub = DeleteEntityServiceStub(channel)

@retry((Exception), tries=3)
def delete_entity(entity_id):
	logger.debug("Entered Delete Entity Method")
	try:
		request = DeleteEntityRequest(
			entity_id = entity_id
		)
		return stub.serve(request)

	except RetryError:
		return FATAL_ERROR

	except Exception as e:
		logger.error(e)
		return str(e)
	