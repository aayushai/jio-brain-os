query = "REMOVE '%s' IN %s \
        LET deleted = OLD \
		RETURN OLD._id"
#line1: deleting entity from collection using key