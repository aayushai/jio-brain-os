from db.generic.api.metadata_lookup.config import *
from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2 import MetadataLookupResponse
import logging as logger
from google.protobuf.struct_pb2 import Struct
from db.arango.utils.config import *
from db.generic.api.metadata_lookup.config import *
from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2 import MetadataLookupResponse
from jio.brain.proto.base.status_pb2 import BrainStatus, BrainStatusInstance, BrainStatusCode


def pre_process_function(request):
    logger.debug(PREPROCESSING)
    static_request = request
    dynamic_request = None
    return static_request, dynamic_request, brain_status

def post_process_function(cursor, status):
    logger.debug(POSTPROCESSING)
    s = Struct()

    if status['is_ok']:
        s.update(cursor["static_cursor"][0])

    response = MetadataLookupResponse(metadata=s, status=status)
    logger.debug(POSTPROCESSING_COMPLETED)
    return response