import sys
from .service import compile_protos

if __name__ == "__main__":

	service_name = sys.argv[1]
	compile_protos(service_name)
	print("Protos Compiled succesfully")

#python -m grpc_tools.protoc --proto_path=K:\Desktop\reliance\knowledge_updated\knowledge --python_out=K:\Desktop\reliance\knowledge_updated\knowledge\src\python K:\Desktop\reliance\knowledge_updated\knowledge\protos\knowledge\generic\comparision.proto