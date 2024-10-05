import grpc
import logging as logger
from .query import query
from db.influx.api.get_entities_instance.config import *
from google.protobuf.json_format import MessageToDict
'''the preprocess function takes the request as in the input
and generates the query to fetch the list of dynamic attributes
i/p: dynamic request
o/p: query, brain_status'''

def pre_process_function(request):
    print(request)
    entity_type = request["entity_type"]
    query_dict = {}
    query_dict["query_type"] = QueryType.Query
    attributes =  request["attributes"]
    query_dict["attributes"] = {}
    for attribute in attributes:
        measurement = entity_type+"_"+attribute
        query_start = query%(measurement)
        _query = query_start
        query_dict["attributes"][attribute] = _query

    logger.info(PREPROCESSING_COMPLETED)
    return query_dict, brain_status

'''
The post processing function takes the entity_type, the metadata, the influx response and cursor as input
and returns back a dictionary of dynamic attributes(in the type, unit, value format) and brain_status.
'''
def post_process_function(cursor,brain_status):
    from .schema_store import schema_store,value_types
    logger.debug(POSTPROCESSING)
    attributes = cursor.keys()
    attributes_dict_max = {}
    attributes_dict = {}
    for attribute in attributes:
        for i in range(len(cursor[attribute][0])):     
            uid = cursor[attribute][0][i]["unified_id"]
    for attribute in attributes:
        for i in range(len(cursor[attribute][0])):     
            uid = cursor[attribute][0][i]["unified_id"]
            value = cursor[attribute][0][i][attribute]
            attribute_schema = schema_store%(value)
            attributes_dict[attribute] = attribute_schema
            attributes_dict_max[uid]=attributes_dict

    logger.info(POSTPROCESSING_COMPLETED)
    return attributes_dict_max,brain_status




