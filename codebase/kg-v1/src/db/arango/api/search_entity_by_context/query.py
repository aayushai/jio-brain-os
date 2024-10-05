query_with_context = """LET results = (
FOR doc in applies_to
FILTER SPLIT(doc._from, '_')[3] == "%s" AND LIKE(doc._from, "%s")
LET context_doc = DOCUMENT(doc._to)
FILTER context_doc.id == %s
LET symptom_doc = DOCUMENT(doc._from)
RETURN {"id": symptom_doc.id, "display_name": symptom_doc.name.english.display_name} )
RETURN UNIQUE(results)
"""

query_without_context = """LET results = (
FOR doc in applies_to
FILTER SPLIT(doc._from, '_')[3] == "%s" AND LIKE(doc._from, "%s")
LET symptom_doc = DOCUMENT(doc._from)
RETURN {"id": symptom_doc.id, "display_name": symptom_doc.name.english.display_name} )
RETURN UNIQUE(results)
"""