
query = "LET entity = DOCUMENT('%s') \
return entity.name.%s.aliases.element"

#line1: fetching entity using entity_id
#line2: iterating over entity names
#line3: filtering entity names on the basis of language and script
#line4: returning alias names of entity 