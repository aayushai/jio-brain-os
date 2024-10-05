
query = "For entity in %s \
		Filter entity._from == '%s' and entity._to == '%s' \
		REMOVE { _key: entity._key } IN %s \
		LET deleted = OLD \
		RETURN OLD._id"

		#line1: inserting predicate into edge collection by specifying from and to ids
		#line2: storing newly inserted predicate value in a variable
		#line3: returning the id of the newly inserted predicate value
