query = """FOR doc in healthcare_context_type
FILTER doc.id == %s
LET values = (
        FOR y in has_value
        FILTER split(y._from, "/")[1] == doc.context_type
        LET value_doc = UNSET(DOCUMENT(y._to), "_id", "_key", "_rev", "type")
        RETURN MERGE(value_doc, 
            { "name": value_doc.name.english.canonical, 
            "query": value_doc.query.english.primary_query })
    )
RETURN MERGE(UNSET(doc, "_id", "_rev", "_key", "type"), 
            {"name": doc.name.english.canonical,
             "query": doc.query.english.primary_query,
             "values": values})"""