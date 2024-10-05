import grpc
from logs.log import get_logger
from test.utils.config import *
from jio.brain.proto.knowledge.api.schema.delete_collection_pb2 import DeleteCollectionRequest
from jio.brain.proto.knowledge.api.schema.delete_collection_pb2_grpc import DeleteCollectionServiceStub

logger = get_logger("root", "delete_collection")
channel = grpc.insecure_channel(delete_collection_channel)
stub = DeleteCollectionServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response

def test_delete_collection(is_predicate, vertical, collection_name):
    logger.debug(TEST_STARTED)
    try:
        request = DeleteCollectionRequest(
            is_predicate = is_predicate,
            vertical = vertical,
            collection_name = collection_name
        )
        
        test_response = test(request)

        logger.info(TEST_COMPLETED)
        return test_response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_delete_collection(True,"agriculture", "catalyst")
    print(api_response)
    channel.close()