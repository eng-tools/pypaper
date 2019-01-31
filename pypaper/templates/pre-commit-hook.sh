#!/usr/bin/env bash
source venv/bin/activate
python -m pytest
ret=$?
if [ $ret -ne 0 ]; then
     exit 1
fi

