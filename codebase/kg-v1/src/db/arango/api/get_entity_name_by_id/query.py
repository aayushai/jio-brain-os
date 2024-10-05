query = """
FOR doc in %s
FILTER doc.id ==%s
RETURN {"entity_name":doc.name.english.canonical}
"""