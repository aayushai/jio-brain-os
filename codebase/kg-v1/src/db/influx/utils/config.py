
from jio.brain.proto.base.status_pb2 import BrainStatusCode

#Namespace Delimiter
NAMESPACE_DELIMITER = "_" 

# brain_status 
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

# DB
dynamic = "influx"

# General Log Messages
PREPROCESSING_COMPLETED = "Preprocessing completed.Measurement generated from preprocessing"
PREPROCESSING = "Preprocessing method of InfluxDb entered"
POSTPROCESSING = "Postprocessing method of InfluxDb entered"
POSTPROCESSING_COMPLETED = "Postprocessing related InfluxDB completed"
VALIDATE = "Validate method reached to validate influx input parameters"
VALIDATED = "All influxdb input parameters are valid"
MEASUREMENT_NOT_GENERATED = "Measurement not added to InfluxDb-Check the data type-enter a number"
ADD_MEASUREMENT = "add_measurement() method reached in influx dao"
ADD_MEASUREMENT_COMPLETED = "add_measurement method executed sucessfully in influx dao and measurement added to influx"
NO_DYNAMIC_ATTRIBUTE = "Request is empty. No dynamic attributes present."
BUILD_MEASUREMENT = "build_measurement() entered"
MEASUREMENT_BUILT = "measurement built to be added to influx"
INVALID_INPUT_PARAMETER = "Invalid Input parameter entered- Data type must be numeric"
MEASUREMENT_NOT_ADDED = "Measurement not added to Influx"
MEASUREMENT_ADDED = "Measurement added to influx"

# Execution Strings
EXECUTE = "Influx Execute method reached"
EXECUTED = "Query Executed. Post processing completed"

# Enum
import enum
class QueryType(enum.Enum):
   Query = 1 # Get and Delete 
   Write = 2 # Write
   Multi = 3
   Enrich = 4