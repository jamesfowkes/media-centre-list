#!/bin/bash

source `which virtualenvwrapper.sh`

workon mediacentre
python3 builder.py $1 $2 $3 > $4
python3 s3.py fowkc.mediacentre $4
