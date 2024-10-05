query = """ FOR doc in has_attribute
FILTER split(doc._from, "/")[1] == "%s"
RETURN split(doc._to, "/")[1] """