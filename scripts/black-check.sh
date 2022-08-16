#!/bin/bash

# Go to root folder
cd $(dirname $0)/..

ARGS="--check"

# call this script with --fix to have it fix the files
if [[ "$1" = "--fix" ]]
then
    ARGS=""
fi

if [[ -n "${ENVIRONMENT}" ]]; then
    poetry run black "${ARGS}" src
else
    black "${ARGS}" src
fi
