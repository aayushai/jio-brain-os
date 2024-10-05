import grpc
from logs.log import get_logger
from test.utils.config import *
from jio.brain.proto.knowledge.api.schema.delete_attribute_type_pb2 import DeleteAttributeTypeRequest
from jio.brain.proto.knowledge.api.schema.delete_attribute_type_pb2_grpc import DeleteAttributeTypeServiceStub

logger = get_logger("root", "delete_attribute_type")
channel = grpc.insecure_channel(delete_attribute_type_channel)
stub = DeleteAttributeTypeServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response

def test_delete_attribute_type(collection_type, attribute_name):
    logger.debug(TEST_STARTED)
    try:
        request = DeleteAttributeTypeRequest(
            collection_type = collection_type,
            attribute_name = attribute_name
        )

        test_response = test(request)

        logger.info(TEST_COMPLETED)
        return test_response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_delete_attribute_type("agriculture_catalyst1234", "ownership_date")
    print(api_response)
    channel.close()