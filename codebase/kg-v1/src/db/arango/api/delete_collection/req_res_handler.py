import logging as logger
from db.arango.api.delete_collection.config import *

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

    collection_name = request["collection_name"]

    query_dict = {}
    query_dict["query_type"] = QueryType.DeleteType
    query_dict["collection_name"] = collection_name
    query_dict["request"] = request

    logger.info(PREPROCESSING_COMPLETED)
    return query_dict, brain_status


def post_process_function(cursor,status):
    logger.debug(POSTPROCESSING)

    if status["is_ok"]:
        status["brain_status_instance"][0]["status_code"] = BrainStatusCode.KNOWLEDGE_GRAPH_COLLECTION_DELETED

    return cursor,status