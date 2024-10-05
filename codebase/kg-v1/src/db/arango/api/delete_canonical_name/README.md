# Introduction
delete_canonical_name API is used to delete canonical name from an entity.

# Getting Started
1. In .env set username and password for your own arangoDB web interface.
2. server_port = 50062

# Files Description

---proto file---
the inputs required from the user are:
1. String entity_id
2. EntityName entity_name, which furthur includes:
    a)Language language (string script and string language)
    b)String canonical_name
    c)Repeated string alias (list) 

the output from the system is:
1.  the status to mention if canonical_name has been successfully deleted from the entity or not

---query---
this is an arango query where:
#line1: fetching the entity using entity ID
#line2: updating the entity by removing the canonical name of entity in collection


---req_res---

1. def convert_request_to_query
we fetch the entity_id from the user
using the fetched entity_id we obtain the entity_type(collection type,i.e, edge or document collection)
we fetch the entity name from the user and then obtain the language, script (from language proto in entity name), canonical name and alias from the given entity name
we then create a canonical name dictionary which contains the language, script, canonical name and alias
we convert the canonical name dictionary to string format
then we pass the required parameters to the to the query and store in _query and return _query.

2. def convert_db_output_to_response
We first check if the canonical name has been successfully deleted by checking the status variable
We return the status as the response to the user

# Build and Test
makefile -
    commands: make server_delete_canonical_name,    make client_delete_canonical_name,      make client_test_delete_canonical_name

# Contribute 






