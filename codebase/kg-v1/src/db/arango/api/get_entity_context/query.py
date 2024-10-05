query = """
FOR doc in applies_to
LET entity_doc = DOCUMENT(doc._from)
FILTER entity_doc.id == %s
LET context_doc = DOCUMENT(doc._to)
RETURN {"context_type": split(split(doc._to, "/")[0], "_")[2], "id": context_doc.id,
        "minimum": context_doc.minimum_age, "maximum": context_doc.maximum_age}
"""