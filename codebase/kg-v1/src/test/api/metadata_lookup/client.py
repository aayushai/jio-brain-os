import grpc
from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2 import MetadataLookupRequest
from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2_grpc import MetadataLookupServiceStub

from test.api.metadata_lookup.config import TEST,TESTED,channel

from logs.log import get_logger
logger = get_logger("root", "metadata_lookup")

channel = grpc.insecure_channel(channel)
stub = MetadataLookupServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response

# This is the test service of KG that can be added to JioFabric
def test_metadata_lookup(id):
	logger.debug(TEST)
	try:
		request = MetadataLookupRequest(
			id = id
        )
		test_response = test(request)
		logger.info(TESTED)
		return test_response
	except Exception as e:
		logger.error(e)
		return str(e)

if __name__ == "__main__":
	api_response = test_metadata_lookup(21)
	print(api_response)