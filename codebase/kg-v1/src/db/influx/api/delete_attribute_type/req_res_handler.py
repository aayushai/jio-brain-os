from db.influx.utils.config import *

def pre_process_function(request):

    return request, brain_status


def post_process_function(cursor,status):

    return cursor,status