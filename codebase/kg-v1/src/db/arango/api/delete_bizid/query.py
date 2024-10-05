
query = "LET entity = DOCUMENT('%s')  \
        UPDATE entity \
        WITH {bizId: remove_value(entity.bizId, %s)}  \
        IN %s " 
#line1: fetching the entity using entity_id
#line2: updating the entity by deleting the bizID (type and value) of entity in collection
