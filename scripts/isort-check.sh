#!/bin/bash

# Go to root folder
cd $(dirname $0)/..

ARGS="--check-only"

# call this script with --fix to have it fix the files
if [[ "$1" = "--fix" ]]
then
    ARGS=""
fi



if [ -n "${ENVIRONMENT}" ]; then
    poetry run isort "${ARGS}" src && echo "isort successful in production"
else
    isort "${ARGS}" src && echo "isort successful in development"
fi
