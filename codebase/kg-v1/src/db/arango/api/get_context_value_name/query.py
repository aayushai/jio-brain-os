query = """
FOR doc in has_value
FILTER split(doc._to, '_')[1] == "context"
LET context_doc = DOCUMENT(doc._from)
LET value_doc = DOCUMENT(doc._to)
FILTER context_doc.id == %s
FILTER value_doc.id == %s
RETURN value_doc.name.english.canonical 
"""