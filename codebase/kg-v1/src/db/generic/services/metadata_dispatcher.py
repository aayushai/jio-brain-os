from db.generic.services.metadata.metadata_lookup import get_metadata


def get_metadata_attribute_query(collection_name, quantity_types, attribute_types):
    query = []
    format = "{ _key: '%s', attribute_type: '%s', quantity_type: '%s' }"
    for attribute in attribute_types:
        key = collection_name + "_" + attribute
        attribute_type = quantity_types[attribute]
        quantity_type = attribute_types[attribute]
        query.append(format % (key, attribute_type, quantity_type))

    final = "FOR doc in %s \
    INSERT doc IN metadata_attribute"

    final_query = (final % query).replace('"', '')
    return final_query


def get_metadata_entity_predicate_query(collection_name, static_attributes, dynamic_attributes):
    query = "LET doc = document('metadata_entity_predicate/%s') \
        UPSERT { _key: '%s' } \
        INSERT { _key: '%s', '%s': {  'static': %s,  'dynamic': %s  } }  \
        UPDATE { } \
        IN metadata_entity_predicate"

    final_query = query%(collection_name,collection_name,collection_name,collection_name,static_attributes,dynamic_attributes)
    return final_query