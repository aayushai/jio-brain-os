
query = """FOR edge IN %s
FILTER SPLIT(edge._to, '/')[1] == "%s"
LET from_node = DOCUMENT(edge._from)
Return {'id':from_node.id, 
        'entity_type':from_node._key, 
        'name':from_node.name.english.canonical, 
        'display_name':from_node.name.english.display_name}"""