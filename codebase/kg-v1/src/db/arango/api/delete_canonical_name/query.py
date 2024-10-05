
query = "for p in %s \
        filter p._id == '%s' \
        UPDATE p WITH { name: { %s: null } } IN common_person OPTIONS { keepNull: false }"