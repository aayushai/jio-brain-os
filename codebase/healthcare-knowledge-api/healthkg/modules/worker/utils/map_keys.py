def map_keys(response, main_key, old_sub_key, new_sub_key):
    if main_key not in response:
        pass
    else:
        key_object = response[main_key]
        if type(key_object) == dict:
            if old_sub_key not in response[main_key]:
                return response
            else:
                response[main_key][new_sub_key] = response[main_key][old_sub_key]
                del response[main_key][old_sub_key]
        elif type(key_object) == list:
            for idx in range(len(response[main_key])):
                if old_sub_key not in response[main_key][idx]:
                    continue
                else:
                    response[main_key][idx][new_sub_key] = response[main_key][idx][old_sub_key]
                    del response[main_key][idx][old_sub_key]
    return response