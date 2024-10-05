query = "FOR doc IN %s \
  Filter doc._key == '%s' \
  UPDATE doc WITH { attributes: { %s: null } } IN %s OPTIONS { keepNull: false }"
