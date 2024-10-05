
query = "LET entity = DOCUMENT('%s') \
			FOR entity_biz in entity.bizId  \
		RETURN entity_biz.type"

#line1: fetching entity using entity_id
#line2: iterating over biz ids of entity
#line3: returning biz id types of entity