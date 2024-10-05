import grpc
from retry import retry
import logging as logger
from db.generic.utils.config import *
from jio.brain.proto.knowledge.api.data.add_metadata_entity_predicate_pb2 import AddMetadataEntityPredicateRequest
from jio.brain.proto.knowledge.api.data.add_metadata_entity_predicate_pb2_grpc import AddMetadataEntityPredicateServiceStub

add_channel = grpc.insecure_channel(add_metadata_entity_predicate_host)
add_stub = AddMetadataEntityPredicateServiceStub(add_channel)

@retry((Exception), tries=3)
def add_metadata_entity_predicate(collection_name,attribute_name,attribute_type):
    try:
        request = AddMetadataEntityPredicateRequest(
            collection_name = collection_name,
            attribute_name = attribute_name,
            attribute_type = attribute_type
        )
        return add_stub.serve(request)
    except Exception as e:
        logger.error(e)
        return str(e)
    