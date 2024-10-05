import sys
import json

from deeputil import Dummy
from arango import ArangoClient
import pandas as pd
from arango.exceptions import DatabaseCreateError


class FileIngestor():

    def __init__(self, database="http://localhost:8529", database_name="healthcare",
                user="root", password="" , data_fpath="sample-data/data.xlxs", log=Dummy()):
            self.database = database,
            self.database_name = database_name
            self.user = user
            self.password = password
            self.data_fpath = data_fpath
            self.log = log

            self.ARANGO_SYSTEM_DB = "_system"
            self.COLLECTION_EDGE = False
            self.COLLECTION_REPLICATION = 2
            self.COLLECTION_SHARDS = 3
            self.COLLECTION_NAME_PREFIX = self.database_name + "_"

    def get_db_connection(self):
        db = ArangoClient(hosts=self.database)
        try:
            sys_db = db.db(self.ARANGO_SYSTEM_DB,
                username=self.user,
                password=self.password)
        except Exception as e:
            self.log.error("error_connecting_to_DB", exp=e)
            sys.exit()

        if not sys_db.has_database(self.database_name):
            sys_db.create_database(self.database_name)

        db_conn = db.db(self.database_name,
                        username=self.user,
                        password=self.password)
        return db_conn

    def validate_file(self):
        pass

    def read_excel(self):
        # TODO: what id the file is too large?
        excel_file = pd.read_excel(self.data_fpath, sheet_name=None)
        return excel_file

    def create_collections(self,file):
        total_collections = file['collection_type'].size
        self.log.debug("collection_found", total_collections=total_collections)
        db = self.get_db_connection()

        for i in range(total_collections):
            col_type = file['collection_type'][i]
            collection_name = self.COLLECTION_NAME_PREFIX + col_type
            schema = json.loads(file['schema'][i])
            if db.has_collection(collection_name):
                self.log.debug("collection_already_present", collection_name=collection_name)
            else:
                db.create_collection(name=collection_name,
                                    edge=self.COLLECTION_EDGE,
                                    shard_count=self.COLLECTION_SHARDS,
                                    replication_factor=self.COLLECTION_REPLICATION,
                                    schema=schema)
                self.log.info("collection_added", collection=collection_name)

    def create_child_collections(self):
        pass

    def add_instances(self):
        pass

    def ingest(self):
        #TODO: handle csv
        file = self.read_excel()
        self.validate_file()
        self.create_collections(file['collection_type'])
        self.create_child_collections()
        self.add_instances()
