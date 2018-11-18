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
            "https://github.com/jasonelle/jasonelle.github.io.git"
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

# Deploy to develop branch
message =  "Deploy: " + str(time())

subprocess.check_call(["git", "commit", "-m", message])
subprocess.check_call(["git", "push", "website", "develop", "--force"])

# Build page
subprocess.check_call(['scripts/generate-public.sh'])

subprocess.check_call(["rm", "-rf", "archetypes"])
subprocess.check_call(["rm", "-rf", "content"])
subprocess.check_call(["rm", "-rf", "data"])
subprocess.check_call(["rm", "-rf", "layouts"])
subprocess.check_call(["rm", "-rf", "resource"])
subprocess.check_call(["rm", "-rf", "scripts"])
subprocess.check_call(["rm", "-rf", "static"])
subprocess.check_call(["rm", "-rf", "themes"])
subprocess.check_call(["rm", "-rf", "config.toml"])
subprocess.check_call(["rm", "-rf", "docker-compose.yml"])

dir_from = os.getcwd() + "/public"
dir_to = os.getcwd()
copy_tree(dir_from, dir_to)

subprocess.check_call(["rm", "-rf", "public"])
subprocess.check_call(["git", "commit", "-m", message])
subprocess.check_call(["git", "push", "website", "develop:master", "--force"])

subprocess.check_call(["git", "checkout", "master"])
subprocess.check_call(["git", "stash"])
subprocess.check_call(["git", "branch", "-D", "develop"])

print("Deployed Website")
