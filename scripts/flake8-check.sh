#!/bin/sh

# Go to root folder
cd $(dirname $0)/..

## flake8 is silent when it's successful, so make a small amount of noise

if [ -n "${ENVIRONMENT}" ]; then
    poetry run flake8 src && echo "flake8 successful in production"
else
    flake8 src && echo "flake8 successful in development"
fi
