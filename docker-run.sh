#!/bin/bash

url=$1
dir_dest=$PWD
if [ ! -z $2 ]; then
    dir_dest=$2
    if [ ! -d "$dir_dest" ]; then
        mkdir $dir_dest
    fi
fi

echo "URL: "$url
echo "Output: "$dir_dest

cmd="docker run -ti -u $(id -u):$(id -g) -v $dir_dest:/output mario21ic/slidesget:latest $url /output"
echo $cmd
eval $cmd
