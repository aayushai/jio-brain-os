query = "LET entity = DOCUMENT('%s')  \
        UPDATE entity \
        WITH {attributes: {'%s': %s }} \
        IN %s"