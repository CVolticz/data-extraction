#!/bin/bash

# Find Conda Enviornment, 
# Activate it if found, else build the enviornment and activate it
if { conda env list | grep 'burl_run_env'; } > /dev/null 2>&1; then
    conda activate burl_run_env
else 
    conda env create -n burl_run_env python=3.8
    conda activate burl_run_env
    pip install -r requirements.txt
    exit
fi;