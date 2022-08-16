#!/bin/bash

# Go to backend folder
cd $(dirname $0)/..

ARGS="--check-only"

# call this script with --fix to have it fix the files
if [[ "$1" = "--fix" ]]
then
    ARGS=""
fi



if [ -n "${ENVIRONMENT}" ]; then
    poetry run isort "${ARGS}" src 
else
    isort "${ARGS}" src 
fi
