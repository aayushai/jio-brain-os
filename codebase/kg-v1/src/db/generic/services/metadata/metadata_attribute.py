import grpc
from retry import retry
import logging as logger
from db.generic.utils.config import *
from jio.brain.proto.knowledge.api.data.add_metadata_attribute_pb2 import AddMetadataAttributeRequest
from jio.brain.proto.knowledge.api.data.add_metadata_attribute_pb2_grpc import AddMetadataAttributeServiceStub

add_channel = grpc.insecure_channel(add_metadata_attribute_host)
add_stub = AddMetadataAttributeServiceStub(add_channel)\


@retry((Exception), tries=3)
def add_metadata_attribute(vertical,entity_type,attribute_name,quantity_type,attribute_type):        
    try:
        request = AddMetadataAttributeRequest(
            vertical = vertical,
            entity_type = entity_type,
            attribute_name = attribute_name,
            quantity_type = quantity_type,
            attribute_type = attribute_type
        )
        return add_stub.serve(request)
    except Exception as e:
        logger.error(e)
        return str(e)