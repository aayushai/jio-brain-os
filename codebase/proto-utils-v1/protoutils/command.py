
from protoutils.converter import Converter
import argparse

class ProtoUtilsCommand:

    def __str__(self):
        return "Commandline tool for transpiling .proto files to _pb2.py files"

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='For transpiling .proto files to _pb2.py files')
        self.subparser = self.parser.add_subparsers(help='Subcommands')

        self.convert_subparser = self.subparser.add_parser('convert', help='convert files')
        self.convert_subparser.add_argument('-d', '--protopath', metavar='-d', type=str, nargs='?',
                                            required=True,
                                            help='path to directory containing .proto files')
        self.convert_subparser.add_argument('-p', '--pythonpath', metavar='-p', type=str, nargs='?',
                                            required=True,
                                            help='output directory for .py files')
        self.convert_subparser.add_argument('-b', '--protoc-path', metavar='-b', type=str, nargs='?',
                                            default='python -m grpc_tools.protoc',
                                            help='path to the protoc binary')
        self.convert_subparser.add_argument('-t', '--version-tag', metavar='-t', type=str, nargs='?',
                                            default='1.0',
                                            help='tag the converted library with this version')
        #TODO: uncomment when java ang go compilation is to be done
        '''
        self.convert_subparser.add_argument('--gopath', metavar='-g', type=str, nargs='?',
                                            default='',
                                            help='output directory for .go files')
        self.convert_subparser.add_argument('--javapath', metavar='-j', type=str, nargs='?',
                                            default='',
                                            help='output directory for .java files')
        '''
        self.convert_subparser.set_defaults(func=self.convert)

        #TODO: a function that validates syntax of proto files
        self.validate_subparser = self.subparser.add_parser('validate', help='validates .proto files')
        self.validate_subparser.add_argument('-f', '--fpath', metavar='-f', type=str, nargs='?',
                                            required=True,
                                            help='path to directory containing .proto files')
        self.validate_subparser.set_defaults(func=self.validate)

        self.args = self.parser.parse_args()
        self.args.func()

    def convert(self):
        converter = Converter(protopath=self.args.protopath,
                                pythonpath=self.args.pythonpath,
                                protoc_path=self.args.protoc_path,
                                version_tag=self.args.version_tag,
                                #gopath=self.args.gopath,
                                #javapath=self.args.javapath)
        )
        converter.start()

    def validate(self):
        print("Not implemented this functionality ye :P")

def main():
    obj = ProtoUtilsCommand()

if __name__ == '__main__':
    main()
