import logging as logger
from db.arango.api.delete_attribute_type.config import *

def pre_process_function(request):
    logger.debug(PREPROCESSING)

    brain_status = {
        "is_ok": True,
        "brain_status_instance": [{
            "status_code": BrainStatusCode.BRAIN_STATUS_CODE_OK,
            "parameters": {
                "msg": "no error"
            }
        }]
    }

    collection_type = request.collection_type
    attribute_name = request.attribute_name
    query_dict = {}
    query_dict["query_type"] = QueryType.DeleteAttributeType
    query_dict["collection_type"] = collection_type
    query_dict["attribute_name"] = attribute_name
    query_dict["request"] = request

    logger.info(PREPROCESSING_COMPLETED)
    return query_dict, brain_status


def post_process_function(cursor,status):
    logger.debug(POSTPROCESSING)

    return cursor,status