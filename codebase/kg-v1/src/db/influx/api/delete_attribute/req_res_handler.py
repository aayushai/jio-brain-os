import logging as logger
from db.influx.utils.config import *
from db.influx.dao.influx_config import database
from google.protobuf.json_format import MessageToDict
from db.influx.utils.measurement import generate_measurement
from db.influx.utils.get_value import get_value
from jio.brain.proto.base.status_pb2 import BrainStatusCode
from .query import *
import collections
import json

'''the preprocess function takes the request as in the input
and generates the query to fetch the list of dynamic attributes
i/p: dynamic request
o/p: query, status'''

def pre_process_function(request):
	logger.debug(PREPROCESSING)
	parameters = {
		"msg": "no error"
	}

	brain_status_instance = {
		"status_code": BrainStatusCode.BRAIN_STATUS_CODE_OK,
		"parameters": parameters
	}

	brain_status = {
		"is_ok": True,
		"brain_status_instance": [brain_status_instance]
	}

	logger.debug(PREPROCESSING)
	query_dict = {}
	query_dict["attributes"] = {}
	query_dict["query_type"] = QueryType.Query
	entity_type = request.collection_id.split("/")[0].strip()
	entity_id = request.collection_id.split("/")[1].strip()
	attribute_name = request.attribute_name

	measurement_name = entity_type + NAMESPACE_DELIMITER + attribute_name
	_query = query%(measurement_name)
	query_dict["attributes"]["query"] = _query

	logger.info(PREPROCESSING_COMPLETED)
	return query_dict, brain_status

'''
The post processing function takes the entity_type, the metadata, the influx response and cursor as input
and returns back a dictionary of dynamic attributes(in the type, unit, value format) and status.
'''
def post_process_function(cursor, brain_status): 
	return cursor, brain_status