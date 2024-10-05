
query = "LET entity = DOCUMENT('%s') \
        UPDATE entity WITH { bizId: \
        (FOR entity_bizid IN entity.bizId \
          RETURN entity_bizid.type == '%s' AND entity_bizid.value == '%s'? \
        MERGE(entity_bizid, %s) : entity_bizid) \
        } IN %s" \
#line1: fetching entity using entity_id
#line2: updating entity by
#line3: iterating over biz ids
#line4: filtering using biz id type and value and merging if they match to given values respectively
#line5: updating biz id with new values and merging with entity bizid in collection