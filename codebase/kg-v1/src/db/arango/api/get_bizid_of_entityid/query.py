
query = "LET entity = DOCUMENT('%s')\
		FOR biz_id IN entity.bizId \
	    	FILTER biz_id.type == '%s' \
	    RETURN biz_id"
#line1: fetching the entity using entity_id
#line2: iterating through biz ids
#line3: filtering biz ids based on biz id type
#line4: returning biz id(s) of entity