import grpc
import logging as logger
from db.generic.utils.config import *

def call_rpc(request, host_port, stub_name):
	logger.debug("Entered"+ stub_name +"Method")
	
	import_list_pb2 = ["protos", "knowledge", "req_res", api_name + "_pb2"]
    import_req_res_pb2 = importlib.import_module(".".join(import_list_pb2))

	import_list_pb2_grpc = ["protos", "knowledge", "api", api_name + "_pb2_grpc"]
    api_pb2_grpc = importlib.import_module(".".join(import_list_pb2_grpc))

	channel = grpc.insecure_channel(host_port)
	stub = api_pb2_grpc.stub_name(channel)
	try:
		return stub.serve(request)

	except Exception as e:
		logger.error(e)
		return str(e)