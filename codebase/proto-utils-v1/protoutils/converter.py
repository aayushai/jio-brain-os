import os, subprocess
from pathlib import Path
from pprint import pprint

from colorama import Fore


class Converter():
    SETUP_CONTENT = '''
import setuptools

setuptools.setup(
    name="{name}",
    version="{version_tag}",
    author="me",
    author_email="me@example.com",
    description="Knowlegde graph apis",
    long_description="",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("."),

)
'''
    GENERATE_COMMAND = '{protoc_path} --{language}_out={output_path} {extra} -I{proto_dir} {protofile}'
    PROTO_EXTENSION = '.proto'
    PY_EXTENSION = '.py'

    def __init__(self, protopath, pythonpath='', gopath='', javapath='',
                 protoc_path='python -m grpc_tools.protoc', version_tag='1.0'):
        self.protopath = protopath
        #TODO: make it work with proper python library structure where pythonpath = pythonpath/pythonpath
        #self.pythonpath = pythonpath #os.path.join(pythonpath, os.path.basename(os.path.normpath(pythonpath)))
        self.pythonpath = os.path.abspath(pythonpath) if pythonpath else ''
        self.gopath = os.path.abspath(gopath) if gopath else ''
        self.javapath = os.path.abspath(javapath) if javapath else ''
        self.protoc_path = protoc_path
        self.version_tag = version_tag

    def _get_files_with_suffix(self, root_dir, suffix):
        '''
        Return a dictionary of the following type:
        [{'../../myrepo/protos/keyvaluestore/keyvaluestore.proto': {'parent_path': '../../myrepo/protos/keyvaluestore'}},
         {'../../myrepo/protos/helloworld/helloworld.proto': {'parent_path': '../../myrepo/protos/helloworld'}},
         {'../../myrepo/protos/auth_sample/auth_sample.proto': {'parent_path': '../../myrepo/protos/auth_sample'}},
         {'../../myrepo/protos/route_guide/route_guide.proto': {'parent_path': '../../myrepo/protos/route_guide'}}]
        '''
        files = list()
        for root, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(suffix):
                    files.append( {os.path.join(root, filename): {'parent_path': root}} )
        return files

    def _get_output_dirs(self, protofiles, output_path):
        for filename in protofiles:
            for key, value in filename.items():
                value['pythonpath'] = os.path.join(self.pythonpath, value['parent_path'].removeprefix(self.protopath))
        return protofiles

    def _generate(self, protofiles, output_path, language, extra):
        for p in protofiles:
            for f, d in p.items():
                command = self.GENERATE_COMMAND.format(protofile=f,
                                                        proto_dir=self.protopath,
                                                        output_path=output_path,
                                                        language=language,
                                                        extra=extra,
                                                        protoc_path=self.protoc_path
                                                )
                run = subprocess.run(command.split(), capture_output=True)

                if run.returncode == 0:
                    pass
                    #print("{}Sucessfull: {}".format(Fore.GREEN, command))
                else:
                    print("{}Failed: {}".format(Fore.RED, command))
                    print(Fore.RED + run.stderr.decode('utf-8'))
                    print(Fore.RED + run.stdout.decode('utf-8'))

    def _create_init_files(self):
        for root, dirnames, filenames in os.walk(self.pythonpath):
            init_file = open(os.path.join(root, '__init__.py'), 'w+')
            for filename in filenames:
                if not filename.startswith('_') and not filename == 'setup.py' and filename.endswith('.py'):
                    import_line = 'from . import {}\n'.format(filename.split('.py')[0])
                    init_file.write(import_line)
            for dirname in dirnames:
                if not dirname.startswith('_'):
                    import_line = 'from . import {}\n'.format(dirname)
                    init_file.write(import_line)
            init_file.close()

    def _create_setup_file(self):
        setup_file = open(os.path.join(self.pythonpath, 'setup.py'), 'w+')
        lines = self.SETUP_CONTENT.format(name=os.path.basename(os.path.normpath(self.pythonpath)),
                                          version_tag=self.version_tag)
        setup_file.write(lines)

    def _mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def start(self):
        for output_path in [self.pythonpath, self.gopath, self.javapath]:
            protofiles = self._get_files_with_suffix(self.protopath, self.PROTO_EXTENSION)
            protofiles = self._get_output_dirs(protofiles, output_path)


            if output_path: self._mkdir(output_path)
            else: continue

            if output_path == self.pythonpath:
                language = 'python'
                extra = '--grpc_python_out={}'.format(output_path)
                self._generate(protofiles, output_path, language, extra)
                self._create_init_files()
                self._create_setup_file()

            #TODO: exclude if java and go is not required
            '''
            elif output_path == self.javapath:
                language = 'java'
                self._generate(protofiles, output_path, language)

            elif output_path == self.gopath:
                language = 'go'
                self._generate(protofiles, output_path, language)
            '''

