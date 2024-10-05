from db.generic.services.brain.identity_service import getBrainIdForEntityId
from db.generic.services.brain.schema_service import getEntitySchema
import logging as logger
from db.generic.utils.config import *

def getBrainId(request, entity_type):
    print("here")
    schema_id, primary_key = getEntitySchema(entity_type) 
        # Biz Id Proto can be optimized (TODO)
    biz_id_map = list(zip(*map(dict.values, request['entity']['bizId'])))

    print(biz_id_map)

    if(primary_key in biz_id_map[0]):
        primary_data = biz_id_map[1][biz_id_map[0].index(primary_key)]
    else:
        primary_data = None
    print(primary_data)
    try:
        brain_id = getBrainIdForEntityId(schema_id, primary_data)
        return brain_id
    except Exception as e:
        logger.error(e)
        brain_status["msg"] = str(e)
        return None


