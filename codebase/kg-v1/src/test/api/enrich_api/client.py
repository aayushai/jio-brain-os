import os
import json
import grpc
from typing import Dict, List
from test.utils.config import *
from logs.log import get_logger
from google.protobuf import json_format 
from google.protobuf.struct_pb2 import Struct
from jio.brain.proto.knowledge.api.data.enrich_api_pb2 import *
from jio.brain.proto.knowledge.api.data.enrich_api_pb2_grpc import *

logger = get_logger("root", "enrich_api")

channel = grpc.insecure_channel(enrich_api_channel)
stub = EnrichServiceStub(channel)

curr_dir = os.path.dirname(os.path.realpath(__file__))

test_data_file = os.path.join(curr_dir,test_data_file_name)
def read_json_file(file:str) -> Dict:
	with open(file, encoding="utf8") as f:
		data = json.load(f)
	return data

test_data = read_json_file(test_data_file)
if("attribute" in test_data):
    attribute_req = test_data["attribute"]
else:
    attribute_req = None

if("predicate" in test_data):
    predicate_req = test_data["predicate"]
else:
    predicate_req = None

def test(request):
    response = stub.serve(request)
    return response

def test_enrich_api(attribute_req, predicate_req):
    logger.debug("entered test method")
    try:
        request = EnrichServiceRequest(
            enrich_attribute_request = attribute_req,
            enrich_predicate_request = predicate_req
        )
        test_response = test(request)
        
        logger.info("Testing completed")
        return test_response

    except Exception as e:
        logger.error(e)
        return str(e)

if __name__ == "__main__":
    api_response = test_enrich_api(attribute_req, predicate_req)
    print(api_response)