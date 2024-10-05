import ast
from healthkg.modules.worker.utils.query import *
from healthkg.modules.worker.utils.validate_kg_response import validate_kg_response

def get_age_group_id(dispatcher, ages):
    age_group_response = []    
    
    for age in ages:
        query = query_get_age_group_id % (age, age)
        graph_query_response = dispatcher.graph_query(query)
        graph_query_response, graph_query_status = validate_kg_response(graph_query_response)
        if not graph_query_response:
            return None, graph_query_status
        graph_query_response = set(ast.literal_eval(graph_query_response.cursor)[0])            
        age_group_response.append(set(graph_query_response))

    age_group_ids = list(set.intersection(*age_group_response))
    return age_group_ids