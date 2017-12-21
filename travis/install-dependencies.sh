#!/bin/bash
sudo apt-get install python
virtualenv venv
. ./venv/bin/activate
pip install boto3
pip install frontmatter
pip install magic
pip install PyYAML
