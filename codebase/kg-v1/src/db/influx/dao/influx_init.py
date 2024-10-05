from influxdb import InfluxDBClient
from db.influx.dao.influx_config import *

influx_client = InfluxDBClient(host, port)


