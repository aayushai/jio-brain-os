from google.protobuf.json_format import MessageToDict

def resolve_inherited_features(metadata, request):
    keyDict = []
    for i in range(len(metadata)):
        l = metadata[i].split(".")
        if(l[0] not in keyDict):
            keyDict.append( l[0] )
    
    
    dict1 = dict([(key, []) for key in keyDict])
    
    for i in range(len(metadata)):
        l = metadata[i].split(".")
        dict1[l[0]].append(l[2])
    
    request =  MessageToDict(request)
    attr_list = []
    dict_list = [val.lower() for sublist in dict1.values() for val in sublist]

    for i in request["attributeName"]:
        if("." in i):
            if(i.split(".")[1].lower() in dict_list):
                attr_list.append(i)
        elif(i.lower() in dict_list ):
            attr_list.append(i)

    request["attributeName"] = attr_list

    request["path_map"] = dict1

    return request