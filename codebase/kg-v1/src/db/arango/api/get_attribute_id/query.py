query = """
FOR doc in healthcare_attribute_type
FILTER LOWER(doc.name.english.canonical) == "%s"
RETURN {"id" : doc.id}
"""