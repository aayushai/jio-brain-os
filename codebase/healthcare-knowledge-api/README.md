# Healthcare-Knowledge-Api
Healthcare knowledge service is an api service that is based on Domain Centric Knowledge Graph(Healthcare). It is product specific api based on grpc calls using protobuf request, the service is powered by Domain Agnostic Knowledge Graph.

Eg. of api-service 
The get_all_symptom service fetches the symptoms present in knowledge graph.
```
make client_get_all_symptom
```
```
symptom {
  id: 21
  entity_type: "healthcare_symptom_cough"
  name: "Cough"
  display_name: "Cough"
}
symptom {
  id: 23
  entity_type: "healthcare_symptom_fatigue"
  name: "Fatigue"
  display_name: "Fatigue"
}
symptom {
  id: 22
  entity_type: "healthcare_symptom_headache"
  name: "Headache"
  display_name: "Headache"
}
symptom {
  id: 24
  entity_type: "healthcare_symptom_bodypain"
  name: "Body Pain"
  display_name: "Body Pain"
}
...
status {
  is_ok: true
  status_message: "no error"
}
```

-----
# Installing Service
Create a virtual environment
```
virtualenv healthcare
source healthcare/bin/activate
```

Clone the repository
```
git clone https://github.com/Shivansh2407/healthcare-knowledge-api.git
cd healthcare-knowledge-api/
```
Install dependencies
```
pip install dependencies/kgschemalib-1.0.tar.gz 
pip install dependencies/jiohkgprotos-1.0.tar.gz 
pip install dependencies/brainproto-1.0.3.tar.gz
pip install -r requirements.txt
```
-----
# Running the Hosted Service

```
make client_<api_name>
```
---
# Running the Service on local
## Server Side
```
make server_healthcare_knowledge_api
```
## Client Side
Change the channel to local_channel
```
make client_<api_name>
```
-----
# API Mappings

This mapping shows the dependency of Healthcare api's on specific EKG api service.

Healthcare Knowledge APIs | KG APIs  
-----|-----
GetAllDisease | get_all_children
GetAllSymptom | get_all_children
GetDisease | metadata_lookup
GetSymptom | metadata_lookup
GetAttribute | get_attribute 
GetAttributeOrder | get_attribute
GetAttributeName | get_attribute
GetAttributeID | get_attribute_id
GetAttributeValue | get_attribute_value
GetAttributeValueID | get_attribute_value_id
GetDiseaseGivenSymptom | graph_query 
GetSymptomGivenDisease | graph_query
GetHighestAttributeBucket | graph_query
GetAttributesOfSymptomAndDisease | graph_query
GetSymptomBucketInDisease | get_edge
GetAttributeBucketInDisease | graph_query and get_edge
GetSymptomId | get_entity_id_by_name
GetDiseaseId | get_entity_id_by_name
GetContextId | get_entity_id_by_name
GetContext | get_context
GetContextValueId | get_context_value_id 
SearchSymptoms | graph_query and search_entity_by_context
SearchDiseases | graph_query and search_entity_by_context
GetDiseasePatientState | get_entity_context
GetSymptomPatientState | get_entity_context
GetValidSymptomAttributeValuesGivenFilter | graph_query and get_valid_entity_attribute_values_given_filter
GetDiseaseName | get_entity_name_by_id
GetSymptomName | get_entity_name_by_id
GetContextName | get_entity_name_by_id
GetAttributeValueName | get_attribute_value_name
GetContextValueName | get_context_value_name


# Status of Healthcare Service
Healthcare Knowledge APIs | API Name | Status
-----|-----|-----
GetAllDisease | get_all_disease | Complete
GetAllSymptom | get_all_symptom | Complete
GetDisease | get_disease | Complete
GetSymptom | get_symptom | Complete
GetAttribute | get_attribute | Complete
GetAttributeOrder | get_attribute_order | Complete
GetAttributeName | get_attribute_name | Complete
GetAttributeID | get_attribute_id | Complete
GetAttributeValue | get_attribute_value | Complete
GetAttributeValueId | get_attribute_value_id | Complete
GetDiseaseGivenSymptom | get_disease_given_symptom | Complete
GetSymptomGivenDisease | get_symptom_given_disease | Complete
GetSymptomBucketInDisease | get_symptom_bucket_in_disease | Complete
GetHighestAttributeBucket | get_highest_attribute_bucket | Complete
GetAttributeBucketInDisease | get_attribute_bucket_in_disease | Complete
GetAttributesOfSymptomAndDisease | get_attributes_of_symptom_and_disease | Complete
GetSymptomId | get_symptom_id | Complete
GetDiseaseId | get_disease_id | Complete
GetContext | get_context | Complete
GetContextId | get_context_id | Complete
GetContextValueId | get_context_value_id | Complete
SearchSymptoms | search_symptoms | Complete
SearchDiseases | search_diseases | Complete
GetDiseasePatientState | get_disease_patient_state | Complete
GetSymptomPatientState | get_symptom_patient_state | Complete
GetValidSymptomAttributeValuesGivenFilter | get_valid_symptom_attribute_values_given_filter | Complete
GetDiseaseName | get_disease_name | Complete
GetSymptomName | get_symptom_name | Complete
GetContextName | get_context_name | Complete
GetAttributeValueName | get_attribute_value_name | Complete
GetContextValueName | get_context_value_name | Complete
