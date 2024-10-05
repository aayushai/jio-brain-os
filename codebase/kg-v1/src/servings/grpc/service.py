import grpc
from concurrent import futures
from logs.log import get_logger

# rpc_handler = RPC STUB generated from proto
# service = implementation of the service
def serve(rpc_handler, servicer, port, max_workers):
	print("server reached")
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
	
	rpc_handler(servicer(), server)
	
	server.add_insecure_port('[::]:' + str(port))
	server.start()
	print('Starting server. Listening on port %s.'%str(port))
	server.wait_for_termination()
	
	