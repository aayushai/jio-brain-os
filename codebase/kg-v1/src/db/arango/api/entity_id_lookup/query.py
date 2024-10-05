query = "For doc in %s \
        Filter Document(doc._id).id == %d \
        return doc"