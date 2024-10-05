query = "FOR entity IN %s \
FILTER entity.name.%s.aliases.element == {'%s': True} \
return entity._id"

#line1: iterating over all entities in the collection
#line2: iterating over all entity names of an entity
#line3: iterating over all aliases of an entity name
#line4: filtering aliases on the basis of language, script and alias name
#line5: returning entity_id