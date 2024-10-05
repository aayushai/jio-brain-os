import logging as logger
from db.influx.utils.config import *
from google.protobuf.json_format import MessageToDict
from db.influx.utils.measurement import generate_measurement
from jio.brain.proto.base.status_pb2 import BrainStatusCode
import collections

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
'''
the pre_processing_function takes the dynamic request as input
and generates the influxdb query.
i/p: request
o/p: query,status
'''
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
	measurement_dict = {}
	measurement_dict["query_type"] = QueryType.Write
	measurement_dict["attributes"] = {}
	collection_id = request.entity_id
	entity_type = collection_id.split("/")[0].strip()
	entity_id = collection_id.split("/")[1].strip()
	attribute_name = request.attribute_name
	attribute_val = request.attribute_value
	attribute_type_timeseries = flatten(MessageToDict(attribute_val))
	attribute_type_timeseries_numeric_value = list(attribute_type_timeseries.values())[0]
	
	measurement_name = entity_type + NAMESPACE_DELIMITER + attribute_name
	try:
		measurement = generate_measurement(measurement_name,attribute_name,entity_id,attribute_type_timeseries_numeric_value)
	except Exception as e:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		logger.error(str(e))
		return None,brain_status

	measurement_dict["attributes"][attribute_name] = measurement
	logger.info(PREPROCESSING_COMPLETED)
	return measurement_dict, brain_status

'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:Response
'''
def post_process_function(cursor, brain_status): 
	return cursor, brain_status