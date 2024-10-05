query = "LET entity = DOCUMENT('%s') \
         UPDATE entity WITH { name: { '%s': {aliases: null } }} IN %s OPTIONS { keepNull: false }"
#line1: fetching entity using entity_id
#line2: updating entity by
#line3: iterating over entity names
#line4: filtering using language and canonical name and merging if they match to given values respectively
#line5: removing entity alias and merging with entity name in collection