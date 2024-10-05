query_with_context = """
LET result = (
FOR doc in applies_to
LET entity_type = split(doc._from, '_')[3]
LET context_doc = DOCUMENT(doc._to)
LET entity_doc = DOCUMENT(doc._from)
FILTER entity_doc.id == %s and context_doc.id == %s and entity_type == "%s" 
LET values = (
    FOR has_value_doc in has_value
    LET attribute_doc = DOCUMENT(has_value_doc._from)
    LET value_doc = DOCUMENT(has_value_doc._to)
    FILTER attribute_doc.id == %s
    RETURN value_doc.id
)
RETURN values )
RETURN UNIQUE(result)
"""

query_without_context = """
LET result = (
FOR doc in applies_to
LET entity_type = split(doc._from, '_')[3]
LET entity_doc = DOCUMENT(doc._from)
FILTER entity_doc.id == %s and entity_type == "%s" 
LET values = (
    FOR has_value_doc in has_value
    LET attribute_doc = DOCUMENT(has_value_doc._from)
    LET value_doc = DOCUMENT(has_value_doc._to)
    FILTER attribute_doc.id == %s
    RETURN value_doc.id
)
RETURN values )
RETURN UNIQUE(result)
"""