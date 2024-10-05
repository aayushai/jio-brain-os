from jio.brain.proto.base.status_pb2 import BrainStatusCode

#Namespace Delimiter
NAMESPACE_DELIMITER = "_" 

parameters = {
    "NO_ERROR": "no error"
}

brain_status_instance = {
	"status_code": BrainStatusCode.BRAIN_STATUS_CODE_OK,
	"parameters": parameters
}

# brain_status 
brain_status = {
    "is_ok": True,
	"brain_status_instance": [brain_status_instance]
}

# Cursor Object
cursor = {
    "static_cursor":None,
    "dynamic_cursor":None
}

# DB
static = "arango"
dynamic = "influx"

# Execution Log Strings
EXECUTE = "Main execute method entered"
EXECUTED = "Main execution completed"

# List of Hosts
metadata_lookup_host = "10.161.209.143:31003"
delete_entity_host = "10.161.209.143:31004"
identity_service_host = "10.161.209.14:9101"
schema_service_host = "10.161.209.14:9300"
delete_collection_host = "10.161.209.143:31005"


# General Log Messages
PREPROCESSING = "Main preprocessing method entered"
PREPROCESSING_COMPLETED = "Main Preprocessing completed"
PREPROCESSING_INCOMPLETE = "Invalid request hence main preprocessing incomplete"
POSTPROCESSING = "Main postprocessing method entered"
POSTPROCESSING_COMPLETED = "Main postprocessing completed"
VALIDATED = "Validation Completed"
VALIDATION = "Validation method reached"
BUILD_DYNAMIC_REQ = "build_dynamic_request() reached"
DYNAMIC_REQ_BUILT = "Dynamic request built"
BUILD_STATIC_REQ = "build_static_request() reached"
STATIC_REQ_BUILT = "static request built"
INPUT_PARAMETER_COUNT_ERROR = "INPUT_PARAMETER_COUNT_ERROR: The number of input parameters entered are invalid"
GET_METADATA = "get_metadata() reached"
METADATA_FETCHED = "fetched metadata"
METADATA_NOT_FETCHED = "could not fetch metadata."
ENTITY_FETCHED = "fetched entity"
ENTITY_NOT_FETCHED = "could not fetch entity."

# metadata hosts
add_metadata_vertical_host = "10.161.209.143:31006"
add_metadata_attribute_host = "10.161.209.143:31007"
add_metadata_entity_predicate_host = "10.161.209.143:31008"

# Fatal_error
FATAL_ERROR = "Fatal Error Occurred. Please try again!"
