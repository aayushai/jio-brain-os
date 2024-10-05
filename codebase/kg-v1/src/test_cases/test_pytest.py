import os
import json
import pytest
import importlib
from google.protobuf import json_format 
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.base.entity_pb2 import Entity
from jio.brain.proto.knowledge.api.schema.add_collection_type_pb2 import AddCollectionTypeRequest
from jio.brain.proto.knowledge.api.data.add_entity_pb2 import AddEntityRequest
from jio.brain.proto.knowledge.api.data.enrich_api_pb2 import EnrichServiceRequest

from google.protobuf.struct_pb2 import Struct


curr_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(curr_dir,"api")

api_list = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
# print(api_list)

# creating dict of input and output json files
input_files_dict = {}
output_files_dict = {}
input_files = []
output_files = []
for api in api_list:
    input_dir = os.path.join(curr_dir,f"api/{api}/Input")
    input_files.append([os.path.join(input_dir, x) for x in os.listdir(input_dir) if ".json" in x])
    input_files_dict["%s"%api] = input_files
    (input_files_dict["%s"%api][0]).sort()
    input_files = []

    output_dir = os.path.join(curr_dir,f"api/{api}/Output")
    output_files.append([os.path.join(output_dir, x) for x in os.listdir(output_dir) if ".json" in x])
    output_files_dict["%s"%api] = output_files
    (output_files_dict["%s"%api][0]).sort()
    output_files = []

#(input_files_dict["has_entity"][0]).sort()
#(output_files_dict["has_entity"][0]).sort()


# for api_input in input_files:
#     print(api_input)
def add_collection_run(input):

    from api.add_collection_type.server import Servicer
    try:
        request = AddCollectionTypeRequest(
            vertical = input["vertical"], #common
            collection_name = input["collection_name"],#person
            is_predicate = input["is_predicate"], #True/False
            schema = get_struct(input["attribute_schema"])
            )
        context = "abc"
        self = ""
        #test_response = test(request)
        test_response = Servicer.serve(self, request, context)
    
        return test_response

    except Exception as e:
    
        return str(e)

def add_entity_run(input):
    from api.add_entity.server import Servicer
    try:
        entity = json_format.Parse(json.dumps(input), Entity())
        request = AddEntityRequest(
            entity = entity
            )
        context = "abc"
        self = ""
        #test_response = test(request)
        test_response = Servicer.serve(self, request, context)
    
        return test_response

    except Exception as e:
    
        return str(e)

def enrich_api_run(input):
    from api.enrich_api.server import Servicer

    if("attribute" in input):
        attribute_req = input["attribute"]
    else:
        attribute_req = None

    if("predicate" in input):
        predicate_req = input["predicate"]
    else:
        predicate_req = None

    try:
        request = EnrichServiceRequest(
            enrich_attribute_request = attribute_req,
            enrich_predicate_request = predicate_req
        )
        context = "abc"
        self = ""
        #test_response = test(request)
        test_response = Servicer.serve(self, request, context)
    
        return test_response

    except Exception as e:
    
        return str(e)

def get_struct(schema_dict):
    s = Struct()
    s.update(schema_dict)
    return s

client_dict = {}
for api in api_list:
    api_client_list = ['test', 'api', api, 'client']
    print(api_client_list)
    client_dict["%s"%api] = importlib.import_module(".".join(api_client_list))
#print(client_dict)

# lines 1 to 38 is generic code

# lines 44 to 59 are has_entity API specific

io_list_has_entity = []
for i in range(len(input_files_dict["has_entity"][0])):
    io_list_has_entity.append([input_files_dict["has_entity"][0][i],output_files_dict["has_entity"][0][i],"has_entity"])


io_list_add_predicate = []
for i in range(len(input_files_dict["add_predicate"][0])):
    io_list_add_predicate.append([input_files_dict["add_predicate"][0][i],output_files_dict["add_predicate"][0][i],"add_predicate"])


io_list_get_predicate = []
for i in range(len(input_files_dict["get_predicate"][0])):
    io_list_get_predicate.append([input_files_dict["get_predicate"][0][i],output_files_dict["get_predicate"][0][i],"get_predicate"])

io_list_delete_entity = []
for i in range(len(input_files_dict["delete_entity"][0])):
    io_list_delete_entity.append([input_files_dict["delete_entity"][0][i],output_files_dict["delete_entity"][0][i],"delete_entity"])

io_list_delete_predicate = []
for i in range(len(input_files_dict["delete_predicate"][0])):
    io_list_delete_predicate.append([input_files_dict["delete_predicate"][0][i],output_files_dict["delete_predicate"][0][i],"delete_predicate"])

io_list_delete_bizid = []
for i in range(len(input_files_dict["delete_bizid"][0])):
    io_list_delete_bizid.append([input_files_dict["delete_bizid"][0][i],output_files_dict["delete_bizid"][0][i],"delete_bizid"])

io_list_delete_canonical_name = []
for i in range(len(input_files_dict["delete_canonical_name"][0])):
    io_list_delete_canonical_name.append([input_files_dict["delete_canonical_name"][0][i],output_files_dict["delete_canonical_name"][0][i],"delete_canonical_name"])

io_list_add_bizid_to_entity = []
for i in range(len(input_files_dict["add_bizid_to_entity"][0])):
    io_list_add_bizid_to_entity.append([input_files_dict["add_bizid_to_entity"][0][i],output_files_dict["add_bizid_to_entity"][0][i],"add_bizid_to_entity"])

io_list_add_entity = []
for i in range(len(input_files_dict["add_entity"][0])):
    io_list_add_entity.append([input_files_dict["add_entity"][0][i],output_files_dict["add_entity"][0][i],"add_entity"])

io_list_add_attribute = []
for i in range(len(input_files_dict["add_attribute"][0])):
    io_list_add_attribute.append([input_files_dict["add_attribute"][0][i],output_files_dict["add_attribute"][0][i],"add_attribute"])

io_list_add_attribute_type = []
for i in range(len(input_files_dict["add_attribute_type"][0])):
    io_list_add_attribute_type.append([input_files_dict["add_attribute_type"][0][i],output_files_dict["add_attribute_type"][0][i],"add_attribute_type"])

io_list_add_collection_type = []
for i in range(len(input_files_dict["add_collection_type"][0])):
    io_list_add_collection_type.append([input_files_dict["add_collection_type"][0][i],output_files_dict["add_collection_type"][0][i],"add_collection_type"])

io_list_delete_attribute = []
for i in range(len(input_files_dict["delete_attribute"][0])):
    io_list_delete_attribute.append([input_files_dict["delete_attribute"][0][i],output_files_dict["delete_attribute"][0][i],"delete_attribute"])

io_list_delete_attribute_type = []
for i in range(len(input_files_dict["delete_attribute_type"][0])):
    io_list_delete_attribute_type.append([input_files_dict["delete_attribute_type"][0][i],output_files_dict["delete_attribute_type"][0][i],"delete_attribute_type"])

io_list_delete_collection = []
for i in range(len(input_files_dict["delete_collection"][0])):
    io_list_delete_collection.append([input_files_dict["delete_collection"][0][i],output_files_dict["delete_collection"][0][i],"delete_collection"])

io_list_enrich_api = []
for i in range(len(input_files_dict["enrich_api"][0])):
    io_list_enrich_api.append([input_files_dict["enrich_api"][0][i],output_files_dict["enrich_api"][0][i],"enrich_api"])



@pytest.mark.has_entity
@pytest.mark.parametrize("io_list",io_list_has_entity)
def test_has_entity_api(io_list):
    api_name = io_list_has_entity[2]
    client_has_entity = client_dict["has_entity"]
    client = client_has_entity
    f_i = open(io_list[0])
    input = json.load(f_i)
    output = client.test_has_entity(input["entity_id"])
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output

@pytest.mark.add_predicate
@pytest.mark.parametrize("io_list",io_list_add_predicate)
def test_add_predicate_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    #client = client_add_predicate
    api_name = io_list[2]
    client_add_predicate = client_dict[api_name]
    client = client_add_predicate
    output = client.test_add_predicate(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output.status) == expected_output["status"]

@pytest.mark.get_predicate
@pytest.mark.parametrize("io_list",io_list_get_predicate)
def test_get_predicate_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    #client = client_add_predicate
    api_name = io_list[2]
    client_get_predicate = client_dict[api_name]
    client = client_get_predicate
    output = client.test_get_predicate(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output.status) == expected_output["status"]

@pytest.mark.delete_entity
@pytest.mark.parametrize("io_list",io_list_delete_entity)
def test_api(io_list):
    api_name = io_list[2]
    client_delete_entity = client_dict[api_name]
    client = client_delete_entity
    f_i = open(io_list[0])
    input = json.load(f_i)
    output = client.test_delete_entity(input["entity_id"])
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output

@pytest.mark.delete_predicate
@pytest.mark.parametrize("io_list",io_list_delete_predicate)
def test_api(io_list):
    api_name = io_list[2]
    client_delete_entity = client_dict[api_name]
    client = client_delete_entity
    f_i = open(io_list[0])
    input = json.load(f_i)
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output

@pytest.mark.delete_bizid
@pytest.mark.parametrize("io_list",io_list_delete_bizid)
def test_api(io_list):
    api_name = io_list[2]
    client_delete_bizid = client_dict[api_name]
    client = client_delete_bizid
    f_i = open(io_list[0])
    input = json.load(f_i)
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output

@pytest.mark.delete_canonical_name
@pytest.mark.parametrize("io_list",io_list_delete_canonical_name)
def test_api(io_list):
    api_name = io_list[2]
    client_delete_bizid = client_dict[api_name]
    client = client_delete_bizid
    f_i = open(io_list[0])
    input = json.load(f_i)
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output

@pytest.mark.add_bizid_to_entity
@pytest.mark.parametrize("io_list",io_list_add_bizid_to_entity)
def test_api(io_list):
    api_name = io_list[2]
    client_add_bizid_to_entity = client_dict[api_name]
    client = client_add_bizid_to_entity
    f_i = open(io_list[0])
    input = json.load(f_i)
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output

@pytest.mark.add_entity
@pytest.mark.parametrize("io_list",io_list_add_entity)
def test_add_entity_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    api_name = io_list[2]
    client_add_entity = client_dict[api_name]

    output = add_entity_run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    print(output)

@pytest.mark.enrich_api
@pytest.mark.parametrize("io_list",io_list_enrich_api)
def test_enrich_api_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    api_name = io_list[2]
    client_enrich_api = client_dict[api_name]

    output = enrich_api_run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output.status) == expected_output["status"]

@pytest.mark.add_collection_type
@pytest.mark.parametrize("io_list",io_list_add_collection_type)
def test_add_collection_type_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    api_name = io_list[2]
    client_collection_type = client_dict[api_name]
    #client = client_collection_type
    
    output = add_collection_run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output.status) == expected_output["status"]

@pytest.mark.add_attribute_type
@pytest.mark.parametrize("io_list",io_list_add_attribute_type)
def test_add_attribute_type_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    api_name = io_list[2]
    client_attribute_type = client_dict[api_name]
    client = client_attribute_type
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output["status"]

@pytest.mark.add_attribute
@pytest.mark.parametrize("io_list",io_list_add_attribute)
def test_add_attribute_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    api_name = io_list[2]
    client_attribute = client_dict[api_name]
    client = client_attribute
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output["status"]

@pytest.mark.delete_attribute
@pytest.mark.parametrize("io_list",io_list_delete_attribute)
def test_delete_attribute_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    api_name = io_list[2]
    client_delete_attribute = client_dict[api_name]
    client = client_delete_attribute
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output["status"]

@pytest.mark.delete_attribute_type
@pytest.mark.parametrize("io_list",io_list_delete_attribute_type)
def test_delete_attribute_type_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    api_name = io_list[2]
    client_delete_attribute_type = client_dict[api_name]
    client = client_delete_attribute_type
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output) == expected_output["status"]

@pytest.mark.delete_collection
@pytest.mark.parametrize("io_list",io_list_delete_collection)
def test_delete_coolection_api(io_list):
    f_i = open(io_list[0])
    input = json.load(f_i)
    api_name = io_list[2]
    client_delete_collection = client_dict[api_name]
    client = client_delete_collection
    output = client.run(input)
    f_o = open(io_list[1])
    expected_output = json.load(f_o)
    assert MessageToDict(output.status) == expected_output["status"]

def create_io_list(api_name):
    io_list = []
    for i in range(len(input_files_dict["%s"%api_name][0])):
        io_list.append([input_files_dict["%s"%api_name][0][i],output_files_dict["%s"%api_name][0][i]],api_name)
    return io_list



# if __name__ == "__main__":
#     # io_list = create_io_list("has_entity")
#     test_api(create_io_list("has_entity"))