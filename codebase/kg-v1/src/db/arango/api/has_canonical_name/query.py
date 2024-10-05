
query = "LET entity = DOCUMENT('%s') \
        	Let language = '%s' \
        	filter entity.name[language]['canonical'] == '%s' \
        	return entity._id"
