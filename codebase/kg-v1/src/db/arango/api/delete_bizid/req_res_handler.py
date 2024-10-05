import json
import grpc
import logging as logger
from db.arango.api.add_collection_type.config import *
from .query import query
from .config import *
from db.generic.services.brain.schema_service import getEntitySchema

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
	entity_type = entity_id.split("/")[0].strip()	#entity_type is collection_name
	biz_id = request.biz_id
	biz_id_type = biz_id.type
	biz_id_value = biz_id.value
	
	schema_id, primary_key = getEntitySchema(entity_type) 
	primary_key_ = primary_key.split("/")[-1]
	biz_id_ = biz_id.type.split("/")[-1]
	
	if biz_id_ == primary_key_:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Primary ID cannot be deleted"
		return None ,brain_status
	else:
		response = has_entity(entity_id,biz_id_type)
		if not response.is_present :
			brain_status["is_ok"] = False
			brain_status["brain_status_instance"][0]["parameters"]["msg"] = "BizId does not exist"
			return None ,brain_status
		else :
			biz_id_dict = {
				"type": biz_id_type,
      			"value": biz_id_value
			}
			biz_id_str = json.dumps(biz_id_dict)#converting dictionary to string
			biz_id_=  biz_id_str
			query_ = query%(entity_id,biz_id_str,entity_type)
			query_dict["query"] = query_
			print(query_)
			logger.info(PREPROCESSING_COMPLETED)
			return query_dict,brain_status
	


def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)
	
	try:
		if status["is_ok"]:
			status["brain_status_instance"][0]["parameters"]["msg"] = "BizId deleted"
			logger.info(POSTPROCESSING_COMPLETED)
			return cursor,status
		else:
			return cursor,status
		
	except Exception as e:
		logger.error(e)
		return cursor, str(e)



def has_entity(entity_id, biz_id_type):
	from jio.brain.proto.knowledge.api.data.has_biz_id_pb2 import HasBizIdRequest
	from jio.brain.proto.knowledge.api.data.has_biz_id_pb2_grpc import HasBizIdServiceStub
	channel = grpc.insecure_channel('10.161.209.143:31012')
	stub = HasBizIdServiceStub(channel)
	def test(request):
		response = stub.serve(request)
		return response
	try:
		request = HasBizIdRequest(
			entity_id = entity_id,
      		biz_id = biz_id_type
		)
		test_response = test(request)
		
		logger.info("Testing completed")
		
		return test_response
		
	except Exception as e:
		logger.error(e)
		return str(e)
	