import importlib
import logging as logger
from db.generic.utils.config import *

def init(api_name):
    api_name = api_name
        
    import_list_req_res = ["db", "generic", "api", api_name, "req_res_handler"]
    init.req_res_handler = importlib.import_module(".".join(import_list_req_res))

    import_static_query_handler = ["db", static, "dao", "query_handler"]
    init.static_query_handler = importlib.import_module(".".join(import_static_query_handler))

    init.static_query_handler.init(api_name=api_name)

    import_dynamic_query_handler = ["db", dynamic, "dao", "query_handler"]
    init.dynamic_query_handler = importlib.import_module(".".join(import_dynamic_query_handler))

    init.dynamic_query_handler.init(api_name=api_name)

def execute(request):
    logger.debug(EXECUTE)
    cursor = {'static_cursor': None, 'dynamic_cursor': None}
    
    static_request,dynamic_request,brain_status = init.req_res_handler.pre_process_function(request)
    if brain_status['is_ok'] == False:
        logger.error(brain_status)
        cursor["static_cursor"] = None
        cursor["dynamic_cursor"] = None
        return init.req_res_handler.post_process_function(
            cursor,
            brain_status
        )

    if static_request is not None:
        static_cursor, brain_status = init.static_query_handler.execute(static_request)
        cursor["static_cursor"] = static_cursor   

    if(brain_status['is_ok'] == False):
        logger.error(brain_status)
        cursor["static_cursor"] = None
        cursor["dynamic_cursor"] = None
        return init.req_res_handler.post_process_function(
            cursor,
            brain_status
        )

    if dynamic_request is not None:
        dynamic_cursor, brain_status = init.dynamic_query_handler.execute(dynamic_request)
        cursor["dynamic_cursor"] = dynamic_cursor   

    if brain_status['is_ok'] == False:
        logger.error(brain_status)
        cursor["static_cursor"] = None
        cursor["dynamic_cursor"] = None
        return init.req_res_handler.post_process_function(
            cursor,
            brain_status
        )

    # if(static_request is not None and dynamic_request is not None):
    #     static_cursor_map = dict(zip(static_request["attributeName"], cursor["static_cursor"]))
    #     dynamic_cursor_map = dict(zip(dynamic_request["attributeName"], cursor["dynamic_cursor"]))
    #     cursor_map = {**static_cursor_map, **dynamic_cursor_map}
    #     print("Cursor Map")
    #     print(cursor_map)
    #     logger.info(EXECUTED)
    #     return init.req_res_handler.post_process_function(
    #         cursor_map,
    #         brain_status
    #     )

    logger.info(EXECUTED)
    return init.req_res_handler.post_process_function(
        cursor,
        brain_status
    )