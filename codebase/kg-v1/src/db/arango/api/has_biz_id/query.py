query = "LET entity = DOCUMENT('%s') \
        FOR biz_id in entity.bizId \
            FILTER biz_id.type == '%s' \
        RETURN entity._id"
#line1: fetching entity using entity_id
#line2: iterating over biz ids in entity
#line3: filtering biz ids on the basis of biz_id_type
#line4: returning entity