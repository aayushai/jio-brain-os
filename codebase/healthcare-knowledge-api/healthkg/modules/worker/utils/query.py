query_get_symptom_given_disease = """For doc in has_symptom 
LET disease_doc = DOCUMENT(doc._from)
FILTER disease_doc.id == %s
LET symptom_doc = DOCUMENT(doc._to)
RETURN symptom_doc.id\n"""

query_get_disease_given_symptom = """For doc in has_symptom 
LET symptom_doc = DOCUMENT(doc._to)
FILTER symptom_doc.id == %s
LET disease_doc = DOCUMENT(doc._from)
RETURN disease_doc.id\n"""

query_get_highest_attribute_bucket = """LET buckets = (
FOR edge_doc in has_attribute
RETURN edge_doc.bucket
)
RETURN MAX(buckets)\n"""

query_get_attributes_of_symptom_and_disease = """FOR has_symptom_doc in has_symptom 
LET disease_doc = DOCUMENT(has_symptom_doc._from)
LET symptom_doc = DOCUMENT(has_symptom_doc._to)
FILTER disease_doc.id == %s AND symptom_doc.id == %s
FOR has_attribute_doc in has_attribute
FILTER split(has_attribute_doc._from, '/')[1] == symptom_doc.entity_type
LET attribute_doc = DOCUMENT(has_attribute_doc._to)
LET value_ids = (
    FOR has_value_doc in has_value
    FILTER split(has_value_doc._from, '/')[1] == attribute_doc.attribute_type
    LET value_doc = DOCUMENT(has_value_doc._to)
    RETURN {"id": value_doc.id}
)
RETURN { "id": attribute_doc.id, "values": value_ids }"""

query_get_age_group_id = """LET age_group_ids = (
FOR doc in applies_to
LET context_doc = DOCUMENT(doc._to)
FILTER context_doc.maximum_age >= %s and context_doc.minimum_age <= %s
RETURN context_doc.id )
RETURN UNIQUE(age_group_ids)"""