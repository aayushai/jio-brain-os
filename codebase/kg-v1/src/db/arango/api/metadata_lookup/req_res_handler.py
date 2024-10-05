from db.arango.api.metadata_lookup.query import query
from db.arango.api.metadata_lookup.config import *
import logging as logger

'''
The pre_process_function takes in the static request and generates the arango query
i/p: static request
o/p: arrange_query and status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	id = request.id
	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"
	try:
		query_dict["query"] = query%(id)	
	except Exception as e:	
		brain_status["is_ok"] = False
		## TODO : move this to BrainStatusInstance Object
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		logger.error(e)
		return None,brain_status
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status

'''
the post_process_function checks the response from arango 
and returns a response along with a status(if all went okay or some error occured)
i/p: response from arango -> list containing entity_id of added entity OR the error message
o/p: entity_id of entity and status OR Error Message with status
'''
def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)


	if cursor is None or None in cursor:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Given id does not exist"
		print(brain_status)
		return cursor,brain_status

	try:
		if brain_status["is_ok"]:
			if cursor == []:
				brain_status["is_ok"] = False
				brain_status["brain_status_instance"][0]["parameters"]["msg"] = ERROR_MESSAGE
				logger.debug(ERROR_MESSAGE)
		logger.info(POSTPROCESSING_COMPLETED)
		return cursor, brain_status

	except Exception as e:
		logger.error(e)
		brain_status["is_ok"]  = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"]= str(e)
		return cursor,brain_status