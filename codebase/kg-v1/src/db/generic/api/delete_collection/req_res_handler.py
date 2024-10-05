import logging as logger
from db.arango.dao.db_init import arango
from kgschemalib import SchemaClient
from db.generic.api.delete_collection.config import *
from google.protobuf.json_format import MessageToDict
from db.generic.services.metadata_dispatcher import *
from db.generic.services.brain_dispatcher import *
from jio.brain.proto.knowledge.api.schema.delete_collection_pb2 import DeleteCollectionResponse

def pre_process_function(request): #builds static and dynamic requests
    logger.debug(PREPROCESSING)
    is_valid, msg = validate(request)
    if not is_valid:
        brain_status["is_ok"] = is_valid
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
        logger.debug(PREPROCESSING_INCOMPLETE)
        return None, None,brain_status

    vertical = request.vertical
    collection_name = request.collection_name
    is_predicate = request.is_predicate
    entity_type = vertical + NAMESPACE_DELIMITER + collection_name

    # if "vertical" in str(request):
    #     vertical = request["vertical"]
    #     entity_type = vertical + NAMESPACE_DELIMITER + collection_name
    # else:
    #     entity_type = collection_name

    static_request = build_static_request(entity_type, is_predicate)
    dynamic_request = None

    logger.info(PREPROCESSING_COMPLETED)
    return static_request,dynamic_request,brain_status


def validate(request):
    logger.debug(VALIDATION)
    req = str(request)
    if "vertical" in req and "collection_name" in req:
        logger.info(VALIDATED)
        return True,None
    else:
        logger.error(INPUT_PARAMETER_COUNT_ERROR)
        return False,INPUT_PARAMETER_COUNT_ERROR

'''
the build_static request takes the entity_type as input and 
returns it as a static request
i/p: entity_type
o/p: a dictionary containing the entity type
'''
def build_static_request(entity_type, is_predicate):
    logger.debug(STATIC_REQ_BUILT)
    static_request = {}
    static_request["collection_name"] = entity_type
    static_request["is_predicate"] = is_predicate
    logger.info(BUILD_STATIC_REQ)
    return static_request


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

    response  = DeleteCollectionResponse(status=status)

    logger.info(POSTPROCESSING_COMPLETED)
    return response



def update_schema(cursor):
    entity_id = cursor["collection_name"]
    collection_name = entity_id.split("/")[0]
    vertical = collection_name.split("_")[0]
    entity_type = collection_name.split("_")[1]
    print("HERE")
    print(cursor)
    is_predicate = cursor["is_predicate"]
    print("HERE")

    key = "schema_entity_predicate/"+collection_name

    try:
        metadata = get_metadata(key)
        metadata = MessageToDict(metadata)
    except Exception as e:
        logger.error(e)
        brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)

    schema = metadata
    schema_entity_predicate = {}
    schema_entity_predicate["static_attributes"] = schema[collection_name]['static']
    schema_entity_predicate["dynamic_attributes"] = schema[collection_name]['dynamic']

    schema_attribute = []
    for static_attribute in schema_entity_predicate["static_attributes"]:
        schema_attribute.append(static_attribute)

    for dynamic_attribute in schema_entity_predicate["dynamic_attributes"]:
        schema_attribute.append(dynamic_attribute)
    
    vertical_param = {"is_predicate":is_predicate,"vertical":vertical,"entity_type":entity_type}
    attribute_param = {"vertical":vertical,"entity_type":entity_type,"attribute_name":schema_attribute}
    entity_predicate_param = {"vertical":vertical,"entity_type":entity_type}

    client = SchemaClient(arango.host,arango.db_name,arango.username,arango.password)
    client.delete_collection_type(vertical_param,attribute_param,entity_predicate_param)
