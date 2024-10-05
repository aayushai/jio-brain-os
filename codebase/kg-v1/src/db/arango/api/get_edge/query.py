
query = """FOR doc in %s
LET disease_doc_id = DOCUMENT(doc._from).id
LET symptom_doc_id = DOCUMENT(doc._to).id
FILTER disease_doc_id == %s and symptom_doc_id == %s
RETURN UNSET(doc, "_id", "_rev", "_key", "_from", "_to")"""
