import grpc
from db.generic.utils.config import *
from jio.brain.proto.identity.api.identity_service_pb2 import IdentityRequest #Import for getBrainIdForEntityId stub
from jio.brain.proto.identity.api.identity_service_pb2_grpc import EntityIdServiceStub

def getBrainIdForEntityId(schema_id, primary_key):
    brain_id_channel = grpc.insecure_channel(identity_service_host)
    stub = EntityIdServiceStub(brain_id_channel)
    try:
        request = IdentityRequest(
                entity_type_id = schema_id,
                unique_key = [primary_key]
            )
        response = stub.getBrainIdForEntity(request)
        return response.brain_id[0].u64
    except Exception as e:
        print(str(e))


# if __name__ == "__main__":
#     print(getBrainIdForEntityId(5000004,"PAN-1234"))