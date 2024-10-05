
query = "LET entity = DOCUMENT('%s') \
		UPDATE entity WITH { name: {'%s': %s}} \
		IN %s"
#line1: fetching entity using entity_id
#line2: updating entity by adding canonical name in collection


