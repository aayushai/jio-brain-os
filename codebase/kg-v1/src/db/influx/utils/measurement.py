import datetime
import pytz
'''
the generate measurement method creates the structure of the measurement
that needs to be added to influx
'''
def generate_measurement(measurement_name,attribute_name,id,value):
    measurement = [
        {
            "measurement":measurement_name,
            "time":datetime.datetime.utcnow(),
            "tags":{"unified_id":id},
            "fields":{
                attribute_name:value, 
            }
        }
    ]
    return measurement