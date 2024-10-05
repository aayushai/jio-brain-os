query = """ FOR doc in is_a
FILTER split(doc._from, "/")[1] == "%s"
RETURN split(doc._to, "/")[1] """