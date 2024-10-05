
query = "INSERT {_from: '%s', _to: '%s', 'predicateName': '%s', 'attributes': %s} IN %s \
		LET inserted = NEW \
		RETURN inserted._id"

		#line1: inserting predicate into edge collection by specifying from and to ids
		#line2: storing newly inserted predicate value in a variable
		#line3: returning the id of the newly inserted predicate value
