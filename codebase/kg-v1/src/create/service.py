import os, sys
from shutil import copyfile
cur_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.abspath(os.path.join(cur_dir, "../../../"))
req_res_proto_dir = os.path.abspath(os.path.join(project_dir, "protos/knowledge/req_res"))
api_proto_dir = os.path.abspath(os.path.join(project_dir, "protos/knowledge/api"))

src_python_dir = os.path.abspath(os.path.join(project_dir, "src/python"))
src_python_api_dir = os.path.abspath(os.path.join(src_python_dir, "api"))

db_dir = os.path.abspath(os.path.join(src_python_dir, "db"))
arango_dir = os.path.abspath(os.path.join(db_dir, "arango"))
arango_api_dir = os.path.abspath(os.path.join(arango_dir, "api"))

template_req_res_proto_file = os.path.abspath(os.path.join(req_res_proto_dir, "template.proto"))
template_api_proto_file = os.path.abspath(os.path.join(api_proto_dir, "template.proto"))
template_src_python_api_dir = os.path.abspath(os.path.join(src_python_api_dir, "template"))
template_arango_api_dir = os.path.abspath(os.path.join(arango_api_dir, "template"))

template_service = "template"
template_prefix = "Template"
req_res_proto_compile_command = "python -m grpc_tools.protoc --proto_path="+project_dir+" --python_out="+src_python_dir+" %s"
api_proto_compile_command = "python -m grpc_tools.protoc --proto_path="+project_dir+" --grpc_python_out="+src_python_dir+" %s"

#to_do:
#1.server.py: return execute(request)
#2.db.generic.api -> api_name-> query_handler,query_handler_config,req_res_handler,config,utils
#3.db.influx.api -> api_name

def copy_file(src, dst, service_name = None):
	if not ".pyc" in src:
		with open(src, "r") as read_file:
			file_text = read_file.read()
			if service_name:
				service_name_prefix = "".join([x.strip().capitalize() for x in service_name.split("_")])
				file_text = file_text.replace(template_service, service_name)
				file_text = file_text.replace(template_prefix, service_name_prefix)
			with open(dst, "w") as write_file:
				write_file.write(file_text)

def compile_protos(service_name):
	service_req_res_proto_file = os.path.abspath(os.path.join(req_res_proto_dir, service_name + ".proto"))
	req_res_compile_command = req_res_proto_compile_command%service_req_res_proto_file
	#print(req_res_compile_command)
	os.system(req_res_compile_command)

	service_api_proto_file = os.path.abspath(os.path.join(api_proto_dir, service_name + ".proto"))
	api_compile_command = api_proto_compile_command%service_api_proto_file
	os.system(api_compile_command)


def generate_and_comiple_proto_files(service_name):
	service_req_res_proto_file = os.path.abspath(os.path.join(req_res_proto_dir, service_name + ".proto"))
	copy_file(
		src = template_req_res_proto_file,
		dst = service_req_res_proto_file,
		service_name = service_name
	)

	service_api_proto_file = os.path.abspath(os.path.join(api_proto_dir, service_name + ".proto"))
	copy_file(
		src = template_api_proto_file,
		dst = service_api_proto_file,
		service_name = service_name
	)

	compile_protos(service_name)
	


def copy_dir(src_dir, dst_dir, service_name):
	src_files = os.listdir(src_dir)
	src_files.remove("__pycache__")
	
	if not os.path.isdir(dst_dir):
		os.makedirs(dst_dir)

	for file_ in src_files :
		src_file = os.path.join(src_dir, file_)
		dst_file = os.path.join(dst_dir, file_)
		copy_file(
			src = src_file,
			dst = dst_file,
			service_name = service_name
		)


def generate_service(service_name):
	generate_and_comiple_proto_files(service_name)
	
	servicce_src_python_api_dir = os.path.join(src_python_api_dir, service_name)
	copy_dir(
		src_dir = template_src_python_api_dir,
		dst_dir = servicce_src_python_api_dir,
		service_name = service_name
	)

	service_arango_api_dir = os.path.join(arango_api_dir, service_name)
	copy_dir(
		src_dir = template_arango_api_dir,
		dst_dir = service_arango_api_dir,
		service_name = service_name
	)

	print("New template service is generated successfully named as: " + service_name)



if __name__ == "__main__":
	service_name = sys.argv[1]
	generate_service(service_name)








