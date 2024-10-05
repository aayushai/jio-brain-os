import grpc
from db.generic.utils.config import *
from jio.brain.proto.schema.api.schema_service_pb2 import EntitySchemaRequest
from jio.brain.proto.schema.api.schema_service_pb2_grpc import EntitySchemaServiceStub

def getEntitySchema(entity_type): 
    entity_channel = grpc.insecure_channel(schema_service_host)
    #TODO: Vertical should be in camel case hence we are using .capitalize() has hack, we need this via ignore case
    stub = EntitySchemaServiceStub(entity_channel)
    # import pdb; pdb.set_trace()
    try:
        entity_list = entity_type.split("_")
        if(len(entity_list) == 2): #Vertical_Name 
            vertical = entity_list[0]
            domain = ""
            name = entity_list[1]
        if(len(entity_list)>=3): #Vertical_Domain_Name 
            vertical = entity_list[0]
            domain = entity_list[1]
            name = "_".join(entity_list[2:])

        request = EntitySchemaRequest(
            vertical = vertical,
            name = name
            )
        response = stub.getSchemaForEntity(request)
        primary_key = "/bizid/"+entity_type+"/"+response.primary_biz_id.biz_id.name.path[0]
        return response.token.id32, primary_key
    except Exception as e:
        print(str(e))

# if __name__ == "__main__":
#     print(getEntitySchema("common_person"))

