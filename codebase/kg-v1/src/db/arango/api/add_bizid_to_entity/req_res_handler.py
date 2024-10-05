from jio.brain.proto.knowledge.api.data import has_biz_id_pb2_grpc
from jio.brain.proto.knowledge.api.data.add_bizid_to_entity_pb2 import AddBizIdToEntityResponse
from google.protobuf.json_format import MessageToDict
from db.arango.utils.config import QueryType
import json
import grpc
from .config import *
import logging as logger
from db.arango.api.add_bizid_to_entity.query import query
from db.generic.services.brain.schema_service import getEntitySchema
'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	req =  str(request)
	is_valid, msg = validate(req)
	
	if not is_valid:
		brain_status["is_ok"] = is_valid
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = BrainStatusCode.BRAIN_STATUS_CODE_INVALID_DATA
		logger.debug(PREPROCESSING_INCOMPLETE)
		return None, brain_status

	biz_id = request.biz_id
	entity_type = request.entity_id.split("/")[0].strip()	#entity_type is the collection_name
	biz_id_,status = prepare_bizId(biz_id,request.entity_id,entity_type)
	if biz_id_ is None:
		return None, status
	else:
		_query = query%(request.entity_id,biz_id_, entity_type)

		query_dict["query"] = _query
		brain_status["is_ok"] = True
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"
		logger.info(PREPROCESSING_COMPLETED)
		return query_dict,brain_status 

'''
Validate method checks if all the required inputs are present
it returns an Input parameter count error if not
i/p: string(request)
o/p:flag,error message
'''
def validate(req):
	logger.debug(VALIDATION)

	if "entity_id" in req and "biz_id" in req:
		logger.info(VALIDATED)
		return True, None
	else:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False, INPUT_PARAMETER_COUNT_ERROR

def prepare_bizId(biz_id, entity_id,entity_type):
	biz_id_type = biz_id.type
	biz_id_value = biz_id.value
	schema_id, primary_key = getEntitySchema(entity_type) 
	primary_key_ = primary_key.split("/")[-1]
	biz_id_ = biz_id.type.split("/")[-1]
	if biz_id_ == primary_key_:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Primary ID can be not be added like this"
		return None ,brain_status
	else:
		response = has_entity(entity_id,biz_id_type)
		if  response.is_present :
			brain_status["is_ok"] = False
			brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Update of BizID value is not recommended, please delete the bizID and add again"
			return None ,brain_status
		else:
			biz_id_dict = {
				"type": biz_id_type,
      			"value": biz_id_value
			}
			biz_id_str = json.dumps(biz_id_dict)#converting dictionary to string
			biz_id_=  biz_id_str
			return biz_id_ ,brain_status
	

'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)
	try:		
		logger.info(POSTPROCESSING_COMPLETED)
		return cursor,status
	except Exception as e:
		logger.error(e)
		status["is_ok"] = False
		status["brain_status_instance"][0]["parameters"]["msg"] = BrainStatusCode.KNOWLEDGE_GRAPH_BIZ_ID_ALREADY_EXIST
		return cursor ,status

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
	


