from db.generic.utils.config import *

# add_entity API Logger Messages
ENTITY_ADDED = "Entity added"
ENTITY_NOT_ADDED = "Entity not added"

#add_entity Influx Messages (For Atomicity)
MEASUREMENT_ADDED = ". measurement added to influx"
MEASUREMENT_NOT_ADDED = ". measurement not addded to influx due to some error"
