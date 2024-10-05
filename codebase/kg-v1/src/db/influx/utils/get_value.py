import logging as logger
from db.influx.utils.config import *

'''
the get_value method checks if the value is an integer or not and returns the value 
if it is an integer
i/p:request,dynamic_attribute
o/p:value
'''
# TODO - Support all Types of Attributes
def get_value(request,dynamic_attribute):
    logger.debug(VALIDATED)
    try:
        key = list(request["entity"]["attributes"][dynamic_attribute]["atomic"]["numeric"]["value"].keys())[0]
        value = int(request["entity"]["attributes"][dynamic_attribute]["atomic"]["numeric"]["value"][key])
    except Exception as e:
        logger.error(INVALID_INPUT_PARAMETER+str(e))
        return None
    return value