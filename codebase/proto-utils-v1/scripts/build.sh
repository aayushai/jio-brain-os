#!/bin/bash

#TODO:Import logger
function yellow(){
    echo -e "\x1B[33m $1 \x1B[0m"
    if [ ! -z "${2}" ]; then
    echo -e "\x1B[33m $($2) \x1B[0m"
    fi
}
#export https_proxy=http://prodproxy.jio.com:8080
#export http_proxy=http://prodproxy.jio.com:8080

yellow 'Starting..'
yellow 'Download virtualenv'
pip3 install virtualenv --trusted-host nexus.rjil.ril.com --index-url http://Brain_os:Brain_os@nexus.rjil.ril.com:9081/repository/Brain_os-py-group/simple/
yellow 'Activate virtualenv'
python3 -m venv ./protoutilsenv
source ./protoutilsenv/bin/activate

yellow 'Upgrade pip'
pip install --upgrade pip --trusted-host nexus.rjil.ril.com --index-url http://Brain_os:Brain_os@nexus.rjil.ril.com:9081/repository/Brain_os-py-group/simple/

yellow 'Install twine'
pip3 install twine --trusted-host nexus.rjil.ril.com --index-url http://Brain_os:Brain_os@nexus.rjil.ril.com:9081/repository/Brain_os-py-group/simple/

yellow 'Build distribution'
python3 setup.py sdist

yellow 'Upload distribution to nexus using twine'
twine upload -r nexus --repository-url http://10.141.51.157:9081/repository/Brain_os-py/ -u Brain_os -p Brain_os ./dist/*

yellow 'Pull protoutils from nexus'
pip3 install protoutils --trusted-host nexus.rjil.ril.com --index-url http://Brain_os:Brain_os@nexus.rjil.ril.com:9081/repository/Brain_os-py-group/simple/

yellow 'Run protoutils command protoutils --help'
protoutils -h

yellow 'Deactivate virtualenv and delete folder'
deactivate
rm -rf ./protoutilsenv

yellow 'Delete dist/'
rm -rf ./dist
