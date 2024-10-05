from environs import Env
from arango import ArangoClient
from db.arango.dao.db_config import DBConfig

env = Env()
env.read_env()

DB_NAME = env.str("DB_NAME")
DB_USER_NAME = env.str("DB_USER_NAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_HOST = env.str("DB_HOST")

arango = DBConfig(DB_HOST,DB_NAME,DB_USER_NAME,DB_PASSWORD)
client = ArangoClient(hosts=arango.host)
db = client.db(arango.db_name, username=arango.username, password=arango.password)