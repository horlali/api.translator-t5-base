#!/bin/sh

# Go to backend folder
cd $(dirname $0)/..

echo "add logic here to validate that the required env vars are actually set?"

pytest --cov
