
query_attribute = "LET entity = DOCUMENT('%s') \
		RETURN entity.attributes['%s']"

query_predicate = "For edge in %s \
				   Filter edge._from == '%s'\
				   return DOCUMENT(edge._to)"