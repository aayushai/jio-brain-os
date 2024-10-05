import sys
import importlib
import logging as logger
from db.influx.utils.config import *
from db.influx.dao.influx_config import database
from db.influx.dao.influx_init import influx_client as client
 
def init(api_name):
    import_list_req_res = ["db", dynamic, "api", api_name, "req_res_handler"]
    init.req_res_handler = importlib.import_module(".".join(import_list_req_res))
 
'''
the process query method takes the influx query that contains the measurement
and adds it to the influxdb
i/p:query
o/p: measurements, status
'''    
def process_query(query, status):
    #TODO- 20-21 Can we remove?
    client.create_database(database)
    client.switch_database(database) 
    
    if query["query_type"] == QueryType.Write:
        for attribute in query["attributes"].keys():
            measurement = query["attributes"][attribute]
            is_added = client.write_points(measurement) 
            if not is_added:
                status["is_ok"] = is_added
                status["msg"] = MEASUREMENT_NOT_ADDED
                logger.error(MEASUREMENT_NOT_ADDED)
                return query, status
            logger.debug(status)
            logger.info(MEASUREMENT_ADDED)
 
    elif query["query_type"] == QueryType.Query: 
        results_dict = {}
        for attribute in query["attributes"].keys():
            current_query = query["attributes"][attribute]
            results = client.query(current_query)
            results = list(results)
            results_dict[attribute] = results
        return results_dict,status 

    elif query["query_type"] == QueryType.Multi:
        data_list = []
        cursor = []
        cursor.append(query["request"])
        for q in query["query"]:
            result = client.query(q)
            if(len(result)<1):
                cursor.append("Data Not Available")
            else:
                for measurement in result.get_points(measurement=q.split(" ")[3]):
                    data_list.append(str(measurement[q.split(" ")[1]]))
                cursor.append("->".join(data_list))
                data_list = []
        return cursor, status

    elif query["query_type"] == QueryType.Enrich:
        data_list = []
        cursor = []
        cursor.append(query["request"])
        for q in query["query"]:
            result = client.query(q)
            if(len(result)<1):
                cursor.append(0)
            else:
                for measurement in result.get_points(measurement=q.split(" ")[3]):
                    data_list.append(str(measurement[q.split(" ")[1]]))
                cursor.append("->".join(data_list))
                data_list = []
        return cursor, status
 
    return query,status
 
def execute(request):
    query,status = init.req_res_handler.pre_process_function(request)
    if not status["is_ok"]:
        logger.error(status)
        return None,status
    cursor,status = process_query(query,status)
    if not status["is_ok"]:
        logger.error(status)
        return None,status
    cursor,status = init.req_res_handler.post_process_function(cursor, status)
    return cursor, status 