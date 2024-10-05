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
static = "arango"

# Query
dynamic_query = "SELECT 'value' FROM 'measurement' WHERE 'condition'"

# General Log Messages 
ERROR_MESSAGE = "Entity is not added to collection"
PREPROCESSING = "Preprocessing method reached"
PREPROCESSING_INCOMPLETE = "Preprocessing Incomplete - Invalid Parameters"
PREPROCESSING_COMPLETED = "Preprocessing completed"
POSTPROCESSING = "Postprocessing method reached"
POSTPROCESSING_COMPLETED = "Postprocessing completed"
VALIDATION = "Validation method reached"
VALIDATED = "Validation Completed"
GET_TIMESERIES_ATTRIBUTES = "get_timeseries_attributes() reached"
TIMESERIES_ATTRUBUTES_FETCHED = "fetched all timeseries attributes"
FILL_TEMPLATE = "fill_template() reached"
TEMPLATE_QUERY_ADDED = "template query added to value of attribute"
INPUT_PARAMETER_COUNT_ERROR = "INPUT_PARAMETER_COUNT_ERROR: The number of input parameters entered are invalid"
PREDICATE_DELETED = "Predicate Deleted"

# Query Handler Messages
EXECUTE = "Execute method reached"
NOT_EXECUTED = "Query not executed "
EXCEPTION = "DB error "
EXECUTED = "Query executed"

# add_entity API
ENTITY_ADDED = "Entity is added to collection"
NOT_CREATED = "Entity_id not created"

# delete_entity API 
ENTITY_DELETED = "Entity Deleted"
ENTITY_DOES_NOT_EXIST = "Entity Does Not Exists."

# Enum
import enum
class QueryType(enum.Enum):
   Query = 1 
   AddType = 2
   DeleteType = 3
   AddAttributeType = 4
   Multi = 5
   DeleteAttributeType = 6
   Enrich = 7
