#!/usr/bin/env python3
# coding: utf-8
import subprocess
import os
from os import environ
from distutils.dir_util import copy_tree
from time import time

# Deploys the website directory to the website repo
try:
    subprocess.check_call(
        [
            "git", "remote", "add", "website", 
            "git@github.com:jasonelle/jasonelle.github.io.git"
        ]
    )
except:
    pass

try:
    subprocess.check_call(["git", "checkout", "-b", "develop"])
except:
    subprocess.check_call(["git", "checkout", "develop"])


subprocess.check_call(["rm", "-rf", "celljs"])
subprocess.check_call(["rm", "-rf", "stjs"])
subprocess.check_call(["rm", "-rf", "jasonette"])
subprocess.check_call(["rm", "-rf", ".gitignore"])
subprocess.check_call(["rm", "-rf", ".travis.yml"])
subprocess.check_call(["rm", "-rf", "README.md"])
subprocess.check_call(["rm", "-rf", "LICENSE"])
subprocess.check_call(["rm", "-rf", "celljs"])
subprocess.check_call(["rm", "-rf", "scripts"])

dir_from = os.getcwd() + "/website"
dir_to = os.getcwd()
copy_tree(dir_from, dir_to)

subprocess.check_call(["rm", "-rf", "website"])
subprocess.check_call(["git", "add", "."])

message =  "Deploy: " + str(time())
subprocess.check_call(["git", "commit", "-m", message])
subprocess.check_call(["git", "push", "website", "develop", "--force"])
subprocess.check_call(["git", "checkout", "master"])
subprocess.check_call(["git", "stash"])
subprocess.check_call(["git", "branch", "-D", "develop"])

print("Deployed Website")