query = """
FOR attribute_edge_doc in has_attribute
LET symptom_doc = DOCUMENT(attribute_edge_doc._from)
LET attribute_doc = DOCUMENT(attribute_edge_doc._to)
FOR value_edge_doc in has_value
FILTER split(value_edge_doc._from, '/')[1] == attribute_doc.attribute_type
LET value_doc = DOCUMENT(value_edge_doc._to)
FILTER value_doc.name.english.canonical == "%s"
RETURN {"symptom_id": symptom_doc.id ,"attribute_id": attribute_doc.id, "value_id": value_doc.id}
"""