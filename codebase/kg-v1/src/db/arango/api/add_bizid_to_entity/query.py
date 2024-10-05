
query = "LET entity = DOCUMENT('%s') \
        UPDATE entity \
        WITH {bizId: append(entity.bizId, [%s], true)}  \
        IN %s " 
#line1: fetching the entity using entity ID
#line2: updating the entity by appending the bizID (type and value) in collection
