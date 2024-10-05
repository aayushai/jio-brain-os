
query = "LET entity = DOCUMENT('%s')  \
        UPDATE entity WITH { name: { '%s': \
        MERGE(entity.name.%s, {canonical : '%s'}) \
        } } IN %s"
#line1: fetching entity using entity_id
#line2: updating entity by
#line3: iterating over entity names
#line4: filtering using language, script and canonical name and merging if they match to given values respectively
#line5: updating name with new values and merging with entity_name in collection