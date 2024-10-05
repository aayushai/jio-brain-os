import grpc
from retry import retry
import logging as logger
from db.generic.utils.config import *
from jio.brain.proto.knowledge.api.data.add_metadata_vertical_pb2 import AddMetadataVerticalRequest
from jio.brain.proto.knowledge.api.data.add_metadata_vertical_pb2_grpc import AddMetadataVerticalServiceStub

add_channel = grpc.insecure_channel(add_metadata_vertical_host)
add_stub = AddMetadataVerticalServiceStub(add_channel)


@retry((Exception), tries=3)
def add_metadata_vertical(vertical,entity_type,is_predicate):   
    try:
        request = AddMetadataVerticalRequest(
            vertical = vertical,
            entity_type = entity_type,
            is_predicate = is_predicate
        )
        return add_stub.serve(request)
    except Exception as e:
        logger.error(e)
        return str(e)