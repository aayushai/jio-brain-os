'''
the datatype store contains a list of dictionaries 
making quantity and type look ups easy
'''

data_types = {
    "symbolic":"static",
    "timeseries":"dynamic",
    "numeric":"static",
    "image":"image"
}

values = {
    "string":"value",
    "uint32Value":"uint32Value"
}

value_types = {
    "value":"string",
    "uint32Value":"number"
}
