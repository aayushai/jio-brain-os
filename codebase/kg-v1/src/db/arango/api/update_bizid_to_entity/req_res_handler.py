from db.arango.api.update_bizid_to_entity.query import query
import json
from db.arango.api.update_bizid_to_entity.config import *
import logging as logger
'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	brain_status = {
		"is_ok": True,
		"brain_status_instance": [{
			"status_code": BrainStatusCode.BRAIN_STATUS_CODE_OK,
			"parameters": {
				"msg": "no error"
			}
		}]
	}

	query_dict = {}
	query_dict["query_type"] = QueryType.Query

	entity_id = request.entity_id
	entity_type = entity_id.split("/")[0].strip()

	old_biz_id = request.old_biz_id
	new_biz_id = request.new_biz_id

	old_bizid_type = old_biz_id.type
	old_bizid_value = old_biz_id.value

	new_bizid_type = new_biz_id.type
	new_bizid_value = new_biz_id.value

	new_biz_id_dict = {
		"type": new_bizid_type,
      	"value": new_bizid_value
	}

	new_biz_id_str = json.dumps(new_biz_id_dict)	

	try:
		_query = query%(entity_id,old_bizid_type,old_bizid_value,new_biz_id_str,entity_type)

	except Exception as e:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Check for the BizID Parameters"
		logger.error(e)
		return None,brain_status
	
	query_dict["query"] = _query

	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status 

'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	print(cursor)

	return cursor, brain_status

