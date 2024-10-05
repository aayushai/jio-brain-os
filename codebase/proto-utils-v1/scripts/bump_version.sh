#!/bin/bash

#TODO:Import logger
function yellow(){
    echo -e "\x1B[33m $1 \x1B[0m"
    if [ ! -z "${2}" ]; then
    echo -e "\x1B[33m $($2) \x1B[0m"
    fi
}

function bump(){
    #version_string=$(cat setup.py | grep "version=\".*\"")
    current_version=$(grep "version=\".*\"" setup.py | awk -F'"' '{print $2}')
    new_version=$(echo $current_version | awk -F. '{$NF = $NF + 1;} 1' | sed 's/ /./g')
    yellow "updating version from ${current_version} to ${new_version}"
    echo ${version_string}
    sed -i '' 's/version="'${current_version}'"/version="'${new_version}'"/g' setup.py
}

bump