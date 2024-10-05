query = """
FOR doc in %s
FILTER LOWER(doc.name.english.canonical)=="%s"
RETURN {"entity_id":doc.id}
"""