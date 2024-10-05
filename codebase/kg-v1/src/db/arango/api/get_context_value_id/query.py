query = """FOR doc in has_value
FILTER split(doc._to, '_')[1] == "context"
LET context_doc = DOCUMENT(doc._from)
LET value_doc = DOCUMENT(doc._to)
FILTER value_doc.name.english.canonical == "%s"
RETURN {"context_id": context_doc.id, "value_id": value_doc.id}"""