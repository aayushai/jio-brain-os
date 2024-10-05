
query = "for entity in %s \
    		for bizid in entity.bizId\
			FILTER bizid.type == '%s' and bizid.value == '%s'\
			return entity._id"

			#For entity in collection
			#for biz_id in entity.bizId
			#filter biz_id.type and value
			#return the entity id

