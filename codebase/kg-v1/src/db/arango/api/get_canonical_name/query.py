query = "LET entity = DOCUMENT('%s') \
        	Let language = '%s' \
        	return entity.name[language]['canonical']"