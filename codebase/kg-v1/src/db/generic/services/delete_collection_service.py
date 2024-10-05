import grpc
from retry import retry
from db.generic.utils.config import *
from protos.knowledge.req_res.delete_collection_pb2 import DeleteCollectionRequest
from protos.knowledge.api.delete_collection_pb2_grpc import DeleteCollectionServiceStub
import logging as logger

channel = grpc.insecure_channel(delete_collection_host)
stub = DeleteCollectionServiceStub(channel)

@retry((Exception), tries=3)
def delete_collection(vertical, collection_name):
	logger.debug("Entered Delete Collection Method")
	try:
		request = DeleteCollectionRequest(
			vertical = vertical,
			collection_name = collection_name
			)
		return stub.serve(request)
	
	except RetryError:
		return FATAL_ERROR

	except Exception as e:
		logger.error(e)
		return str(e)