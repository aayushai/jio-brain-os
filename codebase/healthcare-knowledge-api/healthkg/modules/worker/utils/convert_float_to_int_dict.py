def convert_float_to_int_dict(dict_obj):
    for key in dict_obj:
        value = dict_obj[key]
        if type(value) == list:            
            for idx in range(len(value)):
                sub_value = dict_obj[key][idx]
                if type(sub_value) == list:
                    dict_obj[key][idx] = [int(x) for x in sub_value]
                elif type(sub_value) == dict:
                    dict_obj[key][idx] = convert_float_to_int_dict(sub_value)
                elif type(sub_value) == float:
                    dict_obj[key][idx] = int(sub_value)
        elif type(value) == float:
            dict_obj[key] = int(value)
    return dict_obj

