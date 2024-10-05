
import grpc

hosted_channel = grpc.insecure_channel(f"10.161.209.143:31050")
local_channel = grpc.insecure_channel(f"localhost:31050")
