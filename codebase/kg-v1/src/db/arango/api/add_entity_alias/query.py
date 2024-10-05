
query = "LET entity = DOCUMENT('%s') \
		UPDATE entity WITH { name: \
 		(FOR entity_name IN entity.name \
   			RETURN entity_name.language.language == '%s' AND entity_name.canonical == '%s'? \
     	 	MERGE(entity_name, {alias: first(return push(entity_name.alias, '%s'))}) : entity_name) \
		} IN %s"

#line1: fetching entity using entity_id
#line2: updating entity by
#line3: iterating over entity names
#line4: filtering using language, script and canonical name and merging if they match to given values respectively
#line5: updating name with new alias and merging with entity_name in collection