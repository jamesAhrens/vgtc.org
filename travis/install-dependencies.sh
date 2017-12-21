#!/bin/bash
sudo apt-get install python
sudo apt-get install python-magic
virtualenv venv
. ./venv/bin/activate
pip install boto3
pip install python-frontmatter
pip install PyYAML
