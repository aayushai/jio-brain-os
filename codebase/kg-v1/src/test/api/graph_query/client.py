import grpc
from test.utils.config import *
from jio.brain.proto.knowledge.api.data.graph_query_pb2 import GraphQueryRequest
from jio.brain.proto.knowledge.api.data.graph_query_pb2_grpc import GraphQueryServiceStub

channel = grpc.insecure_channel(graph_query_channel)
stub = GraphQueryServiceStub(channel)

def test(request):
    response = stub.serve(request)
    return response
    
def test_graph_query(query):
    try:
        request = GraphQueryRequest(
            query = query
        )
        
        test_response = test(request)

        return test_response
    
    except Exception as e:
        return str(e)
        

if __name__ == "__main__":
    query = 'For entity in common_person return entity'
    api_response = test_graph_query(query)
    print(api_response)    







