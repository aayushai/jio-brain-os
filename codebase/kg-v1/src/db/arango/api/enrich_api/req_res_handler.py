import logging as logger
from db.arango.utils.config import *
from db.arango.api.enrich_api.query import *

def pre_process_function(request):
	logger.debug(PREPROCESSING)

	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"

	enrich_list_attribute = request["attributeName"]
	enrich_list_predicate = request["predicateName"]
	queries = []
	query_ = {}
	query_["request"] = request
	query_["query_type"] = QueryType.Enrich
	
	if(enrich_list_attribute is None):
		query_["query_attribute"] = None
	else:
		for i in range(len(enrich_list_attribute)):
			doc = enrich_list_attribute[i].split(".")[0]
			attribute = enrich_list_attribute[i].split(".")[1]
			_query = query_attribute%(doc, attribute)
			queries.append(_query)
		query_["query_attribute"] = queries
		queries = []

	if(enrich_list_predicate is None):
		query_["query_predicate"] = None
	else:
		for i in range(len(enrich_list_predicate)):
			entity_id = enrich_list_predicate[i].split(".")[0]
			predicate = enrich_list_predicate[i].split(".")[1]
			entity_type = entity_id.split("/")[0]
			entity_key = entity_id.split("/")[0]
			_query = query_predicate%(predicate, entity_id)
			queries.append(_query)

		query_["query_predicate"] = queries

	logger.info(PREPROCESSING_COMPLETED)
	return query_,brain_status

from collections import Iterable
def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

def build_attribute_map(cursor, cursor_list, cursor_attributes):
	if(cursor_attributes is None):
		return None
	else:
		flat_cursor_attribute = flatten(cursor["attribute"])
		val = 0
		cursor_map = {}
		cursor_max_map = {}
		for i in range(len(cursor_list)):
			cursor_mini_map = {}
			cursor_minimi_map = {}
			cursor_map[cursor_list[i]["type"]] = {}
			mapping_attributes = cursor_list[i]["attributes"]
			mapping_attributes_new = []
			for m in mapping_attributes:
				if(m in cursor_attributes):
					mapping_attributes_new.append(m)
			entity_list = cursor_list[i]["entityIds"]
			for k in range(len(entity_list)):
				cursor_minimi_map ={}
				cursor_outer_map_mini = {}
				cursor_outer_map = {}
				for j in mapping_attributes_new:
					cursor_minimi_map[j] = flat_cursor_attribute[val]
					val+=1
					cursor_outer_map_mini["attributeValue"] = cursor_minimi_map
					cursor_mini_map[entity_list[k]] = cursor_outer_map_mini
					cursor_outer_map["attributeValue"] = cursor_mini_map
			cursor_map[cursor_list[i]["type"]] = cursor_outer_map
		return cursor_map

def build_predicate_map(cursor, cursor_list, cursor_predicates):
	if(cursor_predicates is None):
		return None
	else:
		flat_cursor_predicate = flatten(cursor["predicate"])
		if('Data Not Available' in flat_cursor_predicate):
			return None
		val = 0
		cursor_map = {}
		cursor_max_map = {}
		for i in range(len(cursor_list)):
			cursor_mini_map = {}
			cursor_minimi_map = {}
			cursor_outermax_map = {}
			cursor_map[cursor_list[i]["type"]] = {}
			mapping_predicates = cursor_list[i]["predicates"]
			entity_list = cursor_list[i]["entityIds"]
			for k in range(len(entity_list)):
				cursor_minimi_map ={}
				cursor_outer_map_mini = {}
				cursor_outer_map = {}
				for j in mapping_predicates:
					fcp_val = flat_cursor_predicate[val]
					fcp_val.pop("_key")
					fcp_val.pop("_id")
					fcp_val.pop("_rev")
					cursor_minimi_map["entity"] = fcp_val
					val+=1
					cursor_outer_map_mini[j] = cursor_minimi_map
					cursor_outermax_map["predicate_value"] = cursor_outer_map_mini
					cursor_mini_map[entity_list[k]] = cursor_outermax_map
					cursor_outer_map["entity_id_predicate"] = cursor_mini_map
			cursor_map[cursor_list[i]["type"]] = cursor_outer_map

		cursor_max_map["subject_predicate"] = cursor_map
		return cursor_map

def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	cursor_list_predicates = []
	cursor_list_attributes = []
	if("enrichPredicateRequest" in cursor["query"]):
		cursor_list_predicates = cursor["query"]["enrichPredicateRequest"]
	if("enrichAttributeRequest" in cursor["query"]):
		cursor_list_attributes = cursor["query"]["enrichAttributeRequest"]

	cursor_attributes = cursor["query"]["attributeName"]
	if(cursor_attributes is not None):
		for i in range(len(cursor_attributes)):
			cursor_attributes[i] = cursor_attributes[i].split(".")[1]
	cursor_predicates = cursor["query"]["predicateName"]
	if(cursor_predicates is not None):
		for i in range(len(cursor_predicates)):
			cursor_predicates[i] = cursor_predicates[i].split(".")[1]

	
	cursor.pop("query")
	static_cursor = {}
	static_cursor_attribute = build_attribute_map(cursor, cursor_list_attributes, cursor_attributes)
	static_cursor_predicate = build_predicate_map(cursor, cursor_list_predicates, cursor_predicates)

	static_cursor["static_cursor_attribute"] = static_cursor_attribute
	static_cursor["static_cursor_predicate"] = static_cursor_predicate
	return static_cursor, brain_status
