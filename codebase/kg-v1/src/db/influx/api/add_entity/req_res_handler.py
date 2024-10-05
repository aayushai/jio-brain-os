import logging as logger
from db.influx.utils.config import *
from db.influx.dao.influx_config import database
from google.protobuf.json_format import MessageToDict
from db.influx.utils.measurement import generate_measurement
from db.influx.utils.get_value import get_value
from jio.brain.proto.base.status_pb2 import BrainStatusCode

'''
the preprocessing function takes the dynamic request as input and returns the dictionary 
containing all the measurements to be added to influx
i/p:request
o/p: dictionary of measurements, status
'''
def pre_process_function(request):
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
	dynamic_attributes_list = list(request["entity"]["attributes"].keys())
	for dynamic_attribute in dynamic_attributes_list:
		value = get_value(request,dynamic_attribute)  
		if value == None:
			brain_status["is_ok"] = False
			brain_status["brain_status_instance"][0]["parameters"]["msg"] = MEASUREMENT_NOT_GENERATED
			return None,brain_status
		
		measurement, brain_status = build_measurement(request,dynamic_attribute,value)
		if measurement is None:
			return None,brain_status
		measurement_dict["attributes"][dynamic_attribute] = measurement
	logger.debug(brain_status)
	logger.info(PREPROCESSING_COMPLETED)
	return measurement_dict, brain_status

'''
the build measurement method fetches all required parameters from request and 
generates the measurement structure to be added to influxdb
i/p:request,value,dynamic_attribute,status
o/p:measurement,status
'''
def build_measurement(request,dynamic_attribute,value):
	logger.debug(BUILD_MEASUREMENT)
	try:
		entity_type = request["entity"]["entityType"]
	
		measurement_name = entity_type + NAMESPACE_DELIMITER + dynamic_attribute 

		brain_id = request["entity"]["_key"] 
		measurement = generate_measurement(measurement_name,dynamic_attribute,brain_id,value) #formats data as influx measurement
		
	except Exception as e:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		logger.error(str(e))
		return None,brain_status
	logger.info(MEASUREMENT_BUILT)
	return measurement,brain_status

def post_process_function(cursor,status): 
	logger.debug(POSTPROCESSING)
	if status["is_ok"]:
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = MEASUREMENT_ADDED

	logger.info(POSTPROCESSING_COMPLETED)
	return cursor,status