ENTITY_ADDED = "Entity added"
ENTITY_NOT_ADDED = "Entity not added"
PREPROCESSING = "Main preprocessing method entered"
PREPROCESSING_COMPLETED = "Main Preprocessing completed"
POSTPROCESSING = "Main postprocessing method entered"
POSTPROCESSING_COMPLETED = "Main postprocessing completed"
VALIDATED = "Validation Completed"
VALIDATION = "Validation method reached"
PREPROCESSING_INCOMPLETE = "Invalid request hence main preprocessing incomplete"

GET_METADATA = "get_metadata() reached"
METADATA_FETCHED = "fetched metadata"
METADATA_NOT_FETCHED = "could not fetch metadata. "
DELIMITER = "_"
status = {
    "ok":True,
    "msg":"No Error"
}

static = "arango"
dynamic = "influx"

host = 'localhost:50078'

EXECUTE = "Main execute method entered"
EXECUTED = "Main execution completed"

BUILD_DYNAMIC_REQ = "build_dynamic_request() reached"
DYNAMIC_REQ_BUILT = "Dynamic request built"
BUILD_STATIC_REQ = "build_static_request() reached"
STATIC_REQ_BUILT = "static request built"
INPUT_PARAMETER_COUNT_ERROR = "INPUT_PARAMETER_COUNT_ERROR: The number of input parameters entered are invalid"