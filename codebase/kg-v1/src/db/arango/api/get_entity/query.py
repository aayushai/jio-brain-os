
query = "LET entity = DOCUMENT('%s')\
		RETURN {entity_type: entity.entityType, biz_id: entity.bizId, name: entity.name, attributes: entity.attributes}"
		
#Fetching the entity with entity id
#returning the entity type, biz_id, name and attributes of the entity