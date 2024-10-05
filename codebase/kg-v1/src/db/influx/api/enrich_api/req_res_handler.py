import grpc
import sys
import struct
import logging as logger
from .query import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *
from ...dao.influx_init import influx_client
from ...dao.influx_config import database
from db.influx.api.enrich_api.config import *

def pre_process_function(request):

    enrich_list = request["attributeName"]
    brain_status["is_ok"] = True
    brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"
    queries = []
    for i in range(len(enrich_list)):
        entity_type = enrich_list[i].split(".")[0].split("/")[0]
        bid = enrich_list[i].split(".")[0].split("/")[1]
        attribute = enrich_list[i].split(".")[1]

        measurement_name = entity_type+"_"+attribute
        query_start = query%(attribute, measurement_name)
        query_end = query_new%(bid)
        query_end = '"'+str(query_end)+'"'
        query_end = query_end.replace('"', "'")
        _query = query_start+query_end
        queries.append(_query)

    query_ = {}
    query_["request"] = request
    query_["query_type"] = QueryType.Enrich
    query_["query"] = queries

    logger.info(PREPROCESSING_COMPLETED)
    return query_, brain_status

def build_cursor_schema(cursor_attributes, cursor, entity_id_list):
    cursor_schema_list = []
    cursor_schema = {}
    for i in range(len(cursor_attributes)):
        schema =  {"quantity_type": {"numeric": {"value": {"u32": "value" } } } }
        attribute_val = cursor[i]
        attribute = cursor_attributes[i]
        key = "schema_attribute/"+entity_id_list[i]
        metadata = get_metadata(key)    
        metadata = MessageToDict(metadata)
        if(metadata == {}):
            return None
        quantity_type = metadata["quantity_type"]

        schema[quantity_type] = schema.pop("quantity_type")
        schema[quantity_type]["numeric"]["value"]["u32"] = attribute_val

        cursor_schema_list.append(schema)
    return cursor_schema_list


def build_attribute_map(cursor, cursor_list, cursor_attributes):
    if(cursor==None):
        return [None]
    val = 0
    cursor_map = {}
    cursor_max_map = {}
    for i in range(len(cursor_list)):
        cursor_mini_map = {}
        cursor_minimi_map = {}
        cursor_map[cursor_list[i]["type"]] = {}
        mapping_attributes = cursor_list[i]["attributes"]
        mapping_attributes_new = []
        for m in mapping_attributes:
            if(m in cursor_attributes):
                mapping_attributes_new.append(m)
        entity_list = cursor_list[i]["entityIds"]
        for k in range(len(entity_list)):
            cursor_minimi_map ={}
            cursor_outer_map_mini = {}
            cursor_outer_map = {}
            for j in mapping_attributes_new:
                cursor_minimi_map[j] = cursor[val]
                val+=1
                cursor_outer_map_mini["attributeValue"] = cursor_minimi_map
                cursor_mini_map[entity_list[k]] = cursor_outer_map_mini
                cursor_outer_map["attributeValue"] = cursor_mini_map
        cursor_map[cursor_list[i]["type"]] = cursor_outer_map
    return cursor_map

def post_process_function(res, brain_status):
    logger.debug(POSTPROCESSING)
    cursor = res

    schema_attribute_key_list = []
    cursor_list_attributes = cursor[0]["enrichAttributeRequest"]
    cursor_attributes = cursor[0]["attributeName"]

    for i in range(len(cursor_attributes)):
        attribute = cursor_attributes[i].split(".")[1]
        schema_attribute_key = cursor_attributes[i].split(".")[0].split("/")[0] + "_" + cursor_attributes[i].split(".")[1]
        schema_attribute_key_list.append(schema_attribute_key)
        cursor_attributes[i] = attribute
    
    cursor.remove(cursor[0])
    dynamic_cursor = {}
    cursor = build_cursor_schema(cursor_attributes, cursor, schema_attribute_key_list)
    dynamic_cursor_attribute = build_attribute_map(cursor, cursor_list_attributes, cursor_attributes)

    dynamic_cursor["dynamic_cursor_attribute"] = dynamic_cursor_attribute
    return dynamic_cursor, brain_status