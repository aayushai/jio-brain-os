
def set_comparator(comparator_enum):
    if comparator_enum == 0:
        comparator = "<"
    if comparator_enum == 1:
        comparator = "<="
    if comparator_enum == 2:
        comparator = ">"
    if comparator_enum == 3:
        comparator = ">="
    if comparator_enum == 4:
        comparator = "=="
    if comparator_enum == 5:
        comparator = "!="
    return comparator