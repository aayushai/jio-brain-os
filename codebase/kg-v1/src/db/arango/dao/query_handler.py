import importlib
from .config import *
from .db_init import db
import logging as logger
from collections import Iterable
from db.arango.utils.config import *

def init(api_name):
	api_name = api_name
	import_list_req_res = ["db", static, "api", api_name, "req_res_handler"]
	init.req_res_handler = importlib.import_module(".".join(import_list_req_res))

def process_query(query,status):
	logger.debug(EXECUTE)
	cursor = []
	try:
		if query["query_type"] == QueryType.Query:
			cursor = db.aql.execute(query["query"])
			cursor = list(cursor)

		elif query["query_type"] == QueryType.AddType:
			cursor.append(query["request"])
			if db.has_collection(query["collection_name"]):
				status["is_ok"] = False
				status["brain_status_instance"][0]["status_code"]=BrainStatusCode.KNOWLEDGE_GRAPH__COLLECTION_ALREADY_EXISTS
				status["brain_status_instance"][0]["parameters"]["msg"]="Collection already exists"
			else:
				db.create_collection(name = query["collection_name"], schema = query["schema"], edge = query["edge_variable"])
		
		elif query["query_type"] == QueryType.DeleteType:
			cursor.append(query["request"])
			if db.has_collection(query["collection_name"]):
				db.delete_collection(query["collection_name"])
			else:
				status["is_ok"] = False
				#TODO: add status code for collection does not exist
				status["brain_status_instance"][0]["parameters"]["msg"] = COLLECTION_DOES_NOT_EXIST
		
		elif query["query_type"] == QueryType.AddAttributeType:
			cursor.append(query["request"])
			collection_type = query["collection_type"]
			if(list(query["attribute_schema"].keys())[0].lower() == "static"):
				if db.has_collection(collection_type):
					attribute_name = query["attribute_name"]
					attribute_schema = query["attribute_schema"]
					collection = db.collection(collection_type)
					schema = collection.properties()["schema"]
					schema[rule][properties][attributes][properties][attribute_name] = attribute_schema
					if query["attribute_required"] == True:
						schema[rule][properties][attributes][required].append(attribute_name)
					collection.configure(schema = schema)
				else:
					status["is_ok"] = False
					#TODO: add status code for collection does not exist
					status["brain_status_instance"][0]["parameters"]["msg"] = COLLECTION_DOES_NOT_EXIST
					logger.error(COLLECTION_DOES_NOT_EXIST)
			else:
				return cursor, status

		elif query["query_type"] == QueryType.DeleteAttributeType:
			cursor.append(query["request"])
			collection_type = query["collection_type"]
			if db.has_collection(collection_type):
				attribute_name = query["attribute_name"]
				collection = db.collection(collection_type)
				schema = collection.properties()["schema"]
				schema[rule][properties][attributes][properties].pop(attribute_name)
				print(schema)
				collection.configure(schema = schema)
			else:
				status["is_ok"] = False
				#TODO: add status code for collection does not exist
				status["brain_status_instance"][0]["parameters"]["msg"] = COLLECTION_DOES_NOT_EXIST
				logger.error(COLLECTION_DOES_NOT_EXIST)

		elif query["query_type"] == QueryType.Multi:
			cursor.append(query["request"])
			for q in query["query"]:
				result = db.aql.execute(q)
				if(result.empty()):
					cursor.append("Data Not Available")
				else:
					cursor.append(list(result))

		elif query["query_type"] == QueryType.Enrich:
			cursor = {"attribute":[], "predicate":[]}
			cursor["query"] = query["request"]
			if(query["query_attribute"] is not None):
				for q in query["query_attribute"]:
					result = db.aql.execute(q)
					if(result.empty()):
						cursor["attribute"].append("Data Not Available")
					else:
						cursor["attribute"].append(list(result))
			if(query["query_predicate"] is not None):
				for q in query["query_predicate"]:
					result = db.aql.execute(q)
					res = list(result)
					if(res == []):
						cursor["predicate"].append("Data Not Available")
					else:
						cursor["predicate"].append(res)
			print(cursor["predicate"])

	except Exception as e:
		logger.error(e)
		exception = str(e)
		status["is_ok"] = False
		status["brain_status_instance"][0]["parameters"]["msg"] = (EXCEPTION + exception)
	logger.info(EXECUTED)
	return cursor,status

def execute(request):
	logger.debug(EXECUTE)
	query,status = init.req_res_handler.pre_process_function(request)
	if not status["is_ok"]:
		logger.error(status)
		return None,status
	cursor,status = process_query(query,status)
	if not status["is_ok"]:
		logger.error(status)
		return None,status
	cursor,status = init.req_res_handler.post_process_function(cursor, status)
	logger.info(EXECUTED)
	return cursor,status