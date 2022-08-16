#!/bin/bash

# Go to root folder
cd $(dirname $0)

./black-check.sh 
./isort-check.sh 
./flake8-check.sh 

