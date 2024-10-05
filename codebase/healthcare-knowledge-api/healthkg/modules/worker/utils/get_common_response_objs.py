from google.protobuf.json_format import MessageToDict
import ast

def get_common_response_objs(response, key):
    object_ids = []
    key_objects = {}

    for response_row in response:
        response_row = MessageToDict(response_row, preserving_proto_field_name=True)
        object_id_row = []
        if key in response_row:
            try:
                response_row_item = ast.literal_eval(response_row[key])
            except ValueError:
                response_row_item = response_row[key]
            for obj in response_row_item:
                object_id_row.append(obj["id"])
                key_objects[obj["id"]] = obj
        object_ids.append(set(object_id_row))

    common_object_ids = set.intersection(*object_ids)
    
    if len(common_object_ids) > 0: 
        common_response_objects = []
        for i in common_object_ids:
            common_response_objects.append(key_objects[i])
    else:
        common_response_objects = None

    return common_response_objects