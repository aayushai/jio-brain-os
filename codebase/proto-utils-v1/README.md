# protoutils
The idea is to have **one** command-line utility that is a wrapper over all the traditional utilities.
The problem with existing protobuff utilities are that there is no one **one** tool to satisfy all needs. Some of the problems that we faced with the traditional tools:
* The "protoc" compiler has a python implementation which works best for python files and the "gen-doc" tool works best on golang.
* The compiler takes one file at a time as an input rather than the whole directory.
* The output is a bunch of files whereas usually one would require a readily installable library.
* Seperate doccumentation for and installations for different languages.

The command-line utility "protoutils" is a wrapper around the traditional utilities that aims to make things more **self-documented**, **Readily usable** and **user-friendly**


## Prerequisites
```
Python >= 3.9
```

## Install from nexus
```bash
pip3 install protoutils --trusted-host nexus.rjil.ril.com --index-url http://Brain_os:Brain_os@nexus.rjil.ril.com:9081/repository/Brain_os-py-group/simple/
```

## Install from source code
```bash
git clone https://devops.jio.com/AICOE/BrainOS/_git/protoutils
pip3 install protoutils/
```

## CLI Usage
### Help command
```bash
$ protoutils  --help
usage: protoutils [-h] {convert,validate} ...

For transpiling .proto files to _pb2.py files

positional arguments:
  {convert,validate}  Subcommands
    convert           convert files
    validate          validates .proto files

optional arguments:
  -h, --help          show this help message and exit
```


```bash
$ protoutils convert --help
usage: protoutils convert [-h] -d [-d] -p [-p] [-b [-b]] [-t [-t]]

optional arguments:
  -h, --help            show this help message and exit
  -d [-d], --protopath [-d]
                        path to directory containing .proto files
  -p [-p], --pythonpath [-p]
                        output directory for .py files
  -b [-b], --protoc-path [-b]
                        path to the protoc binary
  -t [-t], --version-tag [-t]
                        tag the converted library with this version
```

### Compile files
```bash
$ protoutils convert --protopath ./examples/ --pythonpath ./examplelib
```

### Input proto directory
```bash
$ tree examples/
examples/
└── protos
    ├── auth_sample
    │   └── auth_sample.proto
    ├── hellostreamingworld
    │   └── hellostreamingworld.proto
    ├── helloworld
    │   └── helloworld.proto
    ├── keyvaluestore
    │   └── keyvaluestore.proto
    ├── route_guide
    │   └── route_guide.proto
    └── taskmanager
        └── todolist.proto
```

### Output python directory
```bash
$ tree examplelib/
examplelib/
├── __init__.py
├── protos
│   ├── __init__.py
│   ├── auth_sample
│   │   ├── __init__.py
│   │   ├── auth_sample_pb2.py
│   │   └── auth_sample_pb2_grpc.py
│   ├── hellostreamingworld
│   │   ├── __init__.py
│   │   ├── hellostreamingworld_pb2.py
│   │   └── hellostreamingworld_pb2_grpc.py
│   ├── helloworld
│   │   ├── __init__.py
│   │   ├── helloworld_pb2.py
│   │   └── helloworld_pb2_grpc.py
│   ├── keyvaluestore
│   │   ├── __init__.py
│   │   ├── keyvaluestore_pb2.py
│   │   └── keyvaluestore_pb2_grpc.py
│   ├── route_guide
│   │   ├── __init__.py
│   │   ├── route_guide_pb2.py
│   │   └── route_guide_pb2_grpc.py
│   └── taskmanager
│       ├── __init__.py
│       ├── todolist_pb2.py
│       └── todolist_pb2_grpc.py
└── setup.py
```

> As you see the command compiles the directory all at once and you don't have to specify one file at a time like you would normally do: 
> ```
> protoc -I=./examples --python_out=./examplelib/protos/auth_sample/ ./examples/protos/auth_sample/auth_sample.proto
> protoc -I=./examples --python_out=./examplelib/protos/helloworld/ ./examples/protos/helloworld/helloworld.proto
> ```

### Import converted directory as a library
> Note: using python3.9 and pip3.9 as default python and pip

#### Installing the output library:
```bash
$ pip install examplelib/
...
...
Successfully installed examplelib-1.0
```

#### Importing "examplelib" and exploring the contents of it
```python
$ python
Python 3.9.7 (default, Oct 13 2021, 06:44:56) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import examplelib
>>> dir(examplelib)
['__builtins__', '__cached__', '__doc__', ... 'protos']
>>> dir(examplelib.protos)
['__builtins__', '__cached__', '__doc__', ... 'auth_sample', 'hellostreamingworld', 'helloworld', 'keyvaluestore', 'route_guide', 'taskmanager']
>>> dir(examplelib.protos.taskmanager)
['__builtins__', '__cached__', '__doc__', ... 'todolist_pb2', 'todolist_pb2_grpc']
>>> dir(examplelib.protos.taskmanager.todolist_pb2)
```
#### Using the same in a python program
```python=

from examplelib.protos.taskmanager import todolist_pb2 as TodoList

my_list = TodoList.TodoList()
my_list.owner_id = 1234
my_list.owner_name = "Tim"

first_item = my_list.todos.add()
first_item.state = TodoList.TaskState.Value("TASK_DONE")
first_item.task = "Test ProtoBuf for Python"
first_item.due_date = "02.02.2022"

print(my_list)
```

```json
owner_id: 1234
owner_name: "Tim"
todos {
  state: TASK_DONE
  task: "Test ProtoBuf for Python"
  due_date: "02.02.2022"
}
```

## Development
* Adding --javapath and --gopath to convert subcommand
* Adding linting and validating logic
* Integrating "gen-doc" utility with hosting capablities
* Packaging inside docker instead of a python package``
