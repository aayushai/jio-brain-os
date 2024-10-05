
import argparse
from basescript import init_logger

from healthkg.server import start
from healthkg.ingest import FileIngestor

class HealthcareKnowledgeCLI():

    def __str__(self):
        return "Commandline tool for Heatlthcare knowledge APIs"

    def __init__(self):

        self.parser = argparse.ArgumentParser(description='Commandline tool for Heatlthcare knowledge APIs')

        #logger arguments
        self.parser.add_argument("--log-level", default="debug", help="logging level as picked from the logging module, default: %(default)s")
        self.parser.add_argument("--log-format", default="pretty", choices=("json", "pretty"),
                                help=("Force the format of the logs. By default, if the "
                                  "command is from a terminal, print colorful logs. "
                                  "Otherwise print json, default: %(default)s"),)
        self.parser.add_argument("--log-file", default=None,
                                help="Writes logs to log file if specified, default: %(default)s",)
        self.parser.add_argument("--quiet", default=False, action="store_true",
                                help="if true, does not print logs to stderr, default: %(default)s",)
        self.parser.add_argument("--metric-grouping-interval", default=None, type=int,
                                help="To group metrics based on time interval ex:10 i.e;(10 sec), default: %(default)s",)
        self.parser.add_argument("--debug", default=False, action="store_true",
                                help="To run the code in debug mode, default: %(default)s",)
        self.parser.add_argument("--minimal", default=False, action="store_true",
                                help="Hide log keys such as id, host, default: %(default)s",)

        # Subparser for runserver command
        self.subparser = self.parser.add_subparsers(help='Subcommands')

        self.runserver_subparser = self.subparser.add_parser('runserver', help='runs healthcare-knowledge API service')
        self.runserver_subparser.add_argument('-p', '--port', metavar='-p', type=str, nargs='?',
                                            default='31050',
                                            help='port on which server is started, default: %(default)s')
        self.runserver_subparser.add_argument('-w', '--workers', metavar='-w', type=int, nargs='?',
                                            default=5,
                                            help='the number of workers to start the server with, default: %(default)s')

        self.runserver_subparser.set_defaults(func=self.runserver)

        #TODO: a function that validates syntax of proto files

        # Subparser for ingesting a file
        self.ingest_subparser = self.subparser.add_parser('ingest-file', help='ingests data files into arangoDB')
        self.ingest_subparser.add_argument('-db', '--database', metavar='-d', type=str, nargs='?',
                                            default='http://localhost:8529',
                                            help='ArangoDB endpoint in http://xx.xx.xx.xx:xxxx format, default: %(default)s')
        self.ingest_subparser.add_argument('-dn', '--database-name', metavar='-n', type=str, nargs='?',
                                            default='healthcare',
                                            help='ArangoDB database name to store all the data in, default: %(default)s')
        self.ingest_subparser.add_argument('-u', '--user', metavar='-u', type=str, nargs='?',
                                            default='root',
                                            help='username at arango to connect with _system db, default: %(default)s')
        self.ingest_subparser.add_argument('-p', '--password', metavar='-p', type=str, nargs='?',
                                            default='',
                                            help='password for arangoDB to connect with _system db, default: %(default)s')
        self.ingest_subparser.add_argument('-f', '--data-fpath', metavar='-f', type=str, nargs='?',
                                            default="healthkg/sample-data/data.xlxs",
                                            help='data file in form of .xlxs or .csv, default: %(default)s')


        self.ingest_subparser.set_defaults(func=self.ingest_file)

        self.args = self.parser.parse_args()

        self.log = init_logger(
            fmt=self.args.log_format,
            quiet=self.args.quiet,
            level=self.args.log_level,
            fpath=self.args.log_file,
            processors=[],
            metric_grouping_interval=self.args.metric_grouping_interval,
            minimal=self.args.minimal,
        )

        self.args.func()

    def runserver(self):
        start(max_workers=self.args.workers,
                server_port=self.args.port)

    def ingest_file(self):
        self.log.debug('arguments_set', args=self.args)
        file_ingestor = FileIngestor(database=self.args.database,
                                    database_name=self.args.database_name,
                                    user=self.args.user,
                                    password=self.args.password,
                                    data_fpath=self.args.data_fpath,
                                    log=self.log)

        file_ingestor.ingest()


def main():
    obj = HealthcareKnowledgeCLI()

if __name__ == '__main__':
    main()
