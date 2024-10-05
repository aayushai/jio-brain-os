import logging as logger
import grpc
from db.generic.utils.config import *
from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2 import MetadataLookupRequest
from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2_grpc import MetadataLookupServiceStub

def get_metadata(key): 
    logger.debug(GET_METADATA)

    channel = grpc.insecure_channel(metadata_lookup_host)
    stub = MetadataLookupServiceStub(channel)

    try:
        request = MetadataLookupRequest(
            key = key
        )
        metadata_response = stub.serve(request)

        metadata = metadata_response.metadata
        
        logger.info(METADATA_FETCHED)

        return metadata
    
    except Exception as e:
        logger.error(METADATA_NOT_FETCHED+str(e))
        return str(e)
        