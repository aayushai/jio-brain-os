query = "FOR entity IN %s \
		FILTER entity.name.%s.canonical == '%s' \
		RETURN entity._id"

#line1: iterating over entities in collection
#line2: iterating over entity names of an entity
#line3: filtering entity names on the basis of canonical name, language and script
#line4: returning entity id