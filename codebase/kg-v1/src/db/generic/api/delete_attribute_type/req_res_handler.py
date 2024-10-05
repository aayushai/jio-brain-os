import logging as logger
from db.arango.dao.db_init import arango
from kgschemalib import SchemaClient
from db.generic.api.delete_attribute_type.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *
from jio.brain.proto.knowledge.api.schema.delete_attribute_type_pb2 import DeleteAttributeTypeResponse

def pre_process_function(request): #builds static and dynamic requests
    logger.debug(PREPROCESSING)
    is_valid, msg = validate(request)
    if not is_valid:
        brain_status["is_ok"] = is_valid
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
        logger.debug(PREPROCESSING_INCOMPLETE)
        return None, None,brain_status
    static_request = request
    dynamic_request = None

    logger.info(PREPROCESSING_COMPLETED)
    return static_request,dynamic_request,brain_status


def validate(request):
    logger.debug(VALIDATION)
    if request.collection_type is not None and request.attribute_name is not None:
        logger.info(VALIDATED)
        return True,None
    else:
        logger.error(INPUT_PARAMETER_COUNT_ERROR)
        return False,INPUT_PARAMETER_COUNT_ERROR


'''
The post_process_function takes the status and converts it into
the API response signifying if the DB is deleted or not.
'''
def post_process_function(cursor,status):
    logger.debug(POSTPROCESSING)

    if status['is_ok']:
        try:
            cursor = cursor["static_cursor"][0]
            update_schema(cursor)
        except Exception as e:
            brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Schema Update Error!"

    response  = DeleteAttributeTypeResponse(status=status)

    logger.info(POSTPROCESSING_COMPLETED)
    return response



def update_schema(cursor):
    collection_name = cursor.collection_type
    vertical = collection_name.split("_")[0]
    entity_type = collection_name.split("_")[1]
    attribute_name = cursor.attribute_name

    key = "schema_entity_predicate/"+collection_name
    try:
        metadata = get_metadata(key)
        metadata = MessageToDict(metadata)
    except Exception as e:
        logger.error(e)
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
        return None, None,brain_status

    schema = metadata
    schema_entity_predicate = {}
    schema_entity_predicate["static_attributes"] = schema[collection_name]['static']
    schema_entity_predicate["dynamic_attributes"] = schema[collection_name]['dynamic']

    if attribute_name in schema_entity_predicate["static_attributes"]:
        attribute_type = "static"

    else:
        attribute_type = "dynamic"
    
    attribute_param = {"vertical":vertical,"entity_type":entity_type,"attribute_name":attribute_name}
    entity_predicate_param = {"vertical":vertical,"entity_type":entity_type,"attribute_type": attribute_type,"attribute_name":attribute_name}
    client = SchemaClient(arango.host,arango.db_name,arango.username,arango.password)
    client.delete_attribute_type(attribute_param,entity_predicate_param)