import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.add_entity.query import query

'''
The pre_process_function takes in the static request and generates the arango query
i/p: static reqest
o/p: arango_query and status
'''
def pre_process_function(request):
    logger.debug(PREPROCESSING)
    query_dict = {}
    query_dict["query_type"] = QueryType.Query
    entity_type = request["entity"]["entityType"]
    entity = request["entity"]
    entity_str = iterdict(entity)
    val = entity_str["_key"]
    entity_str["_key"] = str(val)

    brain_status["is_ok"] = True
    brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"

    _query = query%(entity_str, entity_type)
    print(_query)
    query_dict["query"] = _query
    logger.info(PREPROCESSING_COMPLETED)
    return query_dict,brain_status 

'''
Iterdict function here will losslessly convert the str to int keeping the values intact
'''
def iterdict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            iterdict(v)
        else:
            if type(v) == str and (k=="u64" or k=="u32"):
                try:
                    v = int(v)
                except ValueError:
                    pass
            d.update({k: v})
    return d

'''
the post_process_function checks the response from arango 
and returns a response along with a status(if all went okay or some error occured)
i/p: response from arango -> list containing entity_id of added entity OR the error message
o/p: entity_id of entity and status OR Error Message with status
'''		

def post_process_function(cursor, status):
    logger.debug(POSTPROCESSING)

    return cursor, status
