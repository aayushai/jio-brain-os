query = """FOR doc in has_attribute
LET to_doc = DOCUMENT(doc._to)
LET from_doc = DOCUMENT(doc._from)
FILTER from_doc.id == %s AND to_doc.id == %s
LET attribute_doc = UNSET(to_doc, "_key", "_rev", "type")
LET values = (
        FOR y in has_value
        FILTER split(y._from, "/")[1] == attribute_doc.attribute_type
        LET value_doc = UNSET(DOCUMENT(y._to), "_id", "_key", "_rev", "type")
        
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
              "related" : disease_ids})
    )
    
    LET depends_on = (
    
        FOR has_attribute_doc in has_attribute
        FILTER has_attribute_doc._to == attribute_doc._id
        
        LET attribute_value_doc_id = (
        FOR has_property_doc in has_property
        FILTER has_property_doc._from == has_attribute_doc._from
        LET attribute_value_doc = DOCUMENT(has_property_doc._to)
        RETURN attribute_value_doc.id
        )[0]
        
        FILTER attribute_value_doc_id != null

        LET symptom_doc_id = (
        FOR is_a_doc in is_a
        FILTER is_a_doc._from == has_attribute_doc._from
        LET symptom_doc = DOCUMENT(is_a_doc._from)
        RETURN symptom_doc.id
        )[0]
        
        LET attribute_doc_id = (
        FOR has_value_doc in has_value
        FILTER DOCUMENT(has_value_doc._to).id == attribute_value_doc_id
        RETURN DOCUMENT(has_value_doc._from).id
        ) [0]
        
        RETURN {"entity_type_id" : symptom_doc_id, "attribute_id": attribute_doc_id, "attribute_value_id": attribute_value_doc_id}
        
    )
RETURN MERGE(UNSET(attribute_doc, "_id"), {"values": values, 
            "name": attribute_doc.name.english.canonical, 
            "query": attribute_doc.query.english.primary_query,
            "depends_on": depends_on})"""