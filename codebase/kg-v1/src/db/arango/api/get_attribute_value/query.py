query = """FOR doc in has_attribute
LET to_doc = DOCUMENT(doc._to)
LET from_doc = DOCUMENT(doc._from)
FILTER from_doc.id == %s AND to_doc.id == %s

FOR y in has_value
FILTER split(y._from, "/")[1] == to_doc.attribute_type
LET value_doc = UNSET(DOCUMENT(y._to), "_id", "_key", "_rev", "type")
FILTER value_doc.id == %s

LET equivalent_entity_type = (
FOR has_property_doc in has_property
FILTER split(has_property_doc._to, "/")[1] == value_doc.value_type
RETURN has_property_doc._from ) [0]

LET disease_ids = (
FOR has_symptom_doc in has_symptom
FILTER has_symptom_doc._to == equivalent_entity_type
LET disease_doc = DOCUMENT(has_symptom_doc._from)
RETURN disease_doc.id )

RETURN MERGE(value_doc, 
        { "name": value_doc.name.english.canonical, 
          "query": value_doc.query.english.primary_query,
          "related" : disease_ids})"""