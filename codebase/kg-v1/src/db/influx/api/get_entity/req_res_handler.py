import grpc
import logging as logger
from .query import query,query_
from db.influx.api.get_entity.config import *
from google.protobuf.json_format import MessageToDict
'''the preprocess function takes the request as in the input
and generates the query to fetch the list of dynamic attributes
i/p: dynamic request
o/p: query, brain_status'''

def pre_process_function(request):
    entity_id = request["entity_id"]

    entity_type = entity_id.split("/")[0].strip()
    bid = entity_id.split("/")[1].strip()

    logger.debug(PREPROCESSING)
    attributes =  request["attributes"]
    query_dict = {}
    query_dict["query_type"] = QueryType.Query
    query_dict["attributes"] = {}
    for attribute in attributes:
        measurement = entity_type+"_"+attribute

        query_start = query%(measurement)
        query_end = query_%(bid) #change to entity_id once the identity service is set up
        query_end = '"'+str(query_end)+'"'
        query_end = query_end.replace('"', "'")
        _query = query_start+query_end
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
    attributes_dict = {}
    for attribute in attributes:        
        value = cursor[attribute][0][0][attribute]
        attribute_schema = schema_store%(value)
        attributes_dict[attribute] = attribute_schema
        
    logger.info(POSTPROCESSING_COMPLETED)
    return attributes_dict,brain_status




