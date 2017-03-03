#!/usr/bin/env python
import subprocess
import sys

html_path = sys.argv[1]

dirs = set([l[2:].strip() for l in open("directory_list_from_site") if l[2:].strip() != ''])
files = set([l.strip()[2:-5] for l in open("html_file_list_from_new_crawl") if l.strip()[2:-5] != ''])

conflicting_files = dirs.intersection(files)
for file_name in conflicting_files:
    html_file = html_path + "/" + file_name + ".html"
    conflicting_file = "conflicting_files/" + file_name
    subprocess.call(["mkdir", "-p", "/".join(conflicting_file.split("/")[:-1])])
    subprocess.call(["cp", html_file, conflicting_file + ".html"])





