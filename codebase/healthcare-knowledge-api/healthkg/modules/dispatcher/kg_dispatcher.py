import grpc
from jio.brain.proto.knowledge.api.data.get_all_children_pb2 import GetAllChildrenRequest
from jio.brain.proto.knowledge.api.data.get_all_children_pb2_grpc import GetAllChildrenServiceStub
from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2 import MetadataLookupRequest
from jio.brain.proto.knowledge.api.data.metadata_lookup_pb2_grpc import MetadataLookupServiceStub
from jio.brain.proto.knowledge.api.data.get_attribute_pb2 import GetAttributeRequest
from jio.brain.proto.knowledge.api.data.get_attribute_pb2_grpc import GetAttributeServiceStub
from jio.brain.proto.knowledge.api.data.graph_query_pb2 import GraphQueryRequest
from jio.brain.proto.knowledge.api.data.graph_query_pb2_grpc import GraphQueryServiceStub
from jio.brain.proto.knowledge.api.data.get_edge_pb2 import GetEdgeRequest
from jio.brain.proto.knowledge.api.data.get_edge_pb2_grpc import GetEdgeServiceStub
from jio.brain.proto.knowledge.api.data.get_attribute_value_pb2 import GetAttributeValueRequest
from jio.brain.proto.knowledge.api.data.get_attribute_value_pb2_grpc import GetAttributeValueServiceStub
from jio.brain.proto.knowledge.api.data.get_attribute_id_pb2_grpc import GetAttributeIdServiceStub
from jio.brain.proto.knowledge.api.data.get_attribute_id_pb2 import GetAttributeIdRequest
from jio.brain.proto.knowledge.api.data.get_attribute_value_id_pb2_grpc import GetAttributeValueIdServiceStub
from jio.brain.proto.knowledge.api.data.get_attribute_value_id_pb2 import GetAttributeValueIdRequest
from jio.brain.proto.knowledge.api.data.get_entity_id_by_name_pb2_grpc import GetEntityIdByNameServiceStub
from jio.brain.proto.knowledge.api.data.get_entity_id_by_name_pb2 import GetEntityIdByNameRequest
from jio.brain.proto.knowledge.api.data.get_context_pb2 import GetContextRequest
from jio.brain.proto.knowledge.api.data.get_context_pb2_grpc import GetContextServiceStub
from jio.brain.proto.knowledge.api.data.get_context_value_id_pb2 import GetContextValueIdRequest
from jio.brain.proto.knowledge.api.data.get_context_value_id_pb2_grpc import GetContextValueIdServiceStub
from jio.brain.proto.knowledge.api.data.search_entity_by_context_pb2 import SearchEntityByContextRequest
from jio.brain.proto.knowledge.api.data.search_entity_by_context_pb2_grpc import SearchEntityByContextServiceStub
from jio.brain.proto.knowledge.api.data.get_entity_context_pb2 import GetEntityContextRequest
from jio.brain.proto.knowledge.api.data.get_entity_context_pb2_grpc import GetEntityContextServiceStub
from jio.brain.proto.knowledge.api.data.get_valid_entity_attribute_values_given_filter_pb2 import GetValidEntityAttributeValuesGivenFilterRequest
from jio.brain.proto.knowledge.api.data.get_valid_entity_attribute_values_given_filter_pb2_grpc import GetValidEntityAttributeValuesGivenFilterServiceStub
from jio.brain.proto.knowledge.api.data.get_entity_name_by_id_pb2 import GetEntityNameByIdRequest
from jio.brain.proto.knowledge.api.data.get_entity_name_by_id_pb2_grpc import GetEntityNameByIdServiceStub
from jio.brain.proto.knowledge.api.data.get_attribute_value_name_pb2 import GetAttributeValueNameRequest
from jio.brain.proto.knowledge.api.data.get_attribute_value_name_pb2_grpc import GetAttributeValueNameServiceStub
from jio.brain.proto.knowledge.api.data.get_context_value_name_pb2 import GetContextValueNameRequest
from jio.brain.proto.knowledge.api.data.get_context_value_name_pb2_grpc import GetContextValueNameServiceStub

class KGDispatcher:
    '''
    TODO
    '''
    def __init__(self):
        self.host = "localhost"

    def get_all_children(self,request):
        channel = grpc.insecure_channel(f"{self.host}:31038")
        stub = GetAllChildrenServiceStub(channel)
        try:
            request = GetAllChildrenRequest(
                predicate_name = request["predicate_name"],
                from_node = request["from_node"]
            )
            response = stub.serve(request)
            return response
        except Exception as e:
            return str(e)

    def get_metadata(self,id):
        channel = grpc.insecure_channel(f"{self.host}:31056")
        stub = MetadataLookupServiceStub(channel)
        try:
            request = MetadataLookupRequest(
                id = id
            )
            metadata_response = stub.serve(request)
            return metadata_response
        except Exception as e:
            return str(e)

    def get_attribute(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31055")
        stub = GetAttributeServiceStub(channel)
        try:
            request = GetAttributeRequest(
                from_node_id = request["from_node_id"],
                to_node_id = request["to_node_id"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_attribute_id(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31046")
        stub = GetAttributeIdServiceStub(channel)
        try:
            request = GetAttributeIdRequest(
                attribute_name = request["attribute_name"],
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_attribute_value_id(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31052")
        stub = GetAttributeValueIdServiceStub(channel)
        try:
            request = GetAttributeValueIdRequest(
                attribute_value_name = request["attribute_value_name"],
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_attribute_value(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31045")
        stub = GetAttributeValueServiceStub(channel)
        try:
            request = GetAttributeValueRequest(
                from_node_id = request["from_node_id"],
                to_node_id = request["to_node_id"],
                value_id = request["value_id"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def graph_query(self, query):
        channel = grpc.insecure_channel(f"{self.host}:31016")
        stub = GraphQueryServiceStub(channel)
        try:
            request = GraphQueryRequest(
                query = query
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_edge(self, edge_collection, from_id, to_id):
        channel = grpc.insecure_channel(f"{self.host}:31044")
        stub = GetEdgeServiceStub(channel)
        try:
            request = GetEdgeRequest(
                edge_collection = edge_collection,
                from_id = from_id,
                to_id = to_id
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_entity_id_by_name(self, request, type, collection_name):
        channel = grpc.insecure_channel(f"{self.host}:31048")
        stub = GetEntityIdByNameServiceStub(channel)
        try:
            request = GetEntityIdByNameRequest(
                collection_name = f"{collection_name}",
                entity_name = request[f"{type}_name"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_context(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31051")
        stub = GetContextServiceStub(channel)
        try:
            request = GetContextRequest(
                context_id = request["context_id"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_context_value_id(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31047")
        stub = GetContextValueIdServiceStub(channel)
        try:
            request = GetContextValueIdRequest(
                context_value_name = request["context_value_name"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def search_entity_by_context(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31053")
        stub = SearchEntityByContextServiceStub(channel)
        try:
            request = SearchEntityByContextRequest(
                entity_type = request["entity_type"],
                keyword = request["keyword"],
                context_id = request["context_id"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_entity_context(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31054")
        stub = GetEntityContextServiceStub(channel)
        try:
            request = GetEntityContextRequest(
                entity_id = request["entity_id"],
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_valid_entity_attribute_values_given_filter(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31057")
        stub = GetValidEntityAttributeValuesGivenFilterServiceStub(channel)
        try:
            request = GetValidEntityAttributeValuesGivenFilterRequest(
                entity_id = request["entity_id"],
                entity_type = request["entity_type"],
                context_id = request["context_id"],
                attribute_id = request["attribute_id"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_entity_name_by_id(self, request, type, collection_name):
        channel = grpc.insecure_channel(f"{self.host}:31058")
        stub = GetEntityNameByIdServiceStub(channel)
        try:
            request = GetEntityNameByIdRequest(
                collection_name = f"{collection_name}",
                entity_id = request[f"{type}_id"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_attribute_value_name(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31059")
        stub = GetAttributeValueNameServiceStub(channel)
        try:
            request = GetAttributeValueNameRequest(
                parent_node_id  = request["parent_node_id"],
                attribute_id = request["attribute_id"],
                value_id = request["value_id"]
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

    def get_context_value_name(self, request):
        channel = grpc.insecure_channel(f"{self.host}:31060")
        stub = GetContextValueNameServiceStub(channel)
        try:
            request = GetContextValueNameRequest(
                context_id   = request["context_id"],
                value_id  = request["value_id"],
            )
            response = stub.serve(request)
            return response

        except Exception as e:
            return str(e)

