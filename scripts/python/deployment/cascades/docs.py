#!/usr/bin/env python3
# coding: utf-8
import subprocess
import os
import glob
from os import environ
from distutils.dir_util import copy_tree
from time import time

# Deploys the docs directory to the docs repo
branch = "deploy-docs"
repo = "docs"
folder = "docs"
build_command = ["./build.sh"]

try:
    subprocess.check_call(
        [
            "git", "remote", "add", repo, 
            "https://github.com/jasonelle/" + repo + ".git"
        ]
    )
except:
    pass

try:
    subprocess.check_call(["git", "checkout", "-b", branch])
except:
    subprocess.check_call(["git", "branch", "-D", branch])
    subprocess.check_call(["git", "checkout", "-b", branch])


subprocess.check_call(["rm", "-rf", "celljs"])
subprocess.check_call(["rm", "-rf", "website"])
subprocess.check_call(["rm", "-rf", "stjs"])
subprocess.check_call(["rm", "-rf", "jasonette"])
subprocess.check_call(["rm", "-rf", ".gitignore"])
subprocess.check_call(["rm", "-rf", ".travis.yml"])
subprocess.check_call(["rm", "-rf", "README.md"])
subprocess.check_call(["rm", "-rf", "LICENSE"])
subprocess.check_call(["rm", "-rf", "celljs"])
subprocess.check_call(["rm", "-rf", "scripts"])

dir_from = os.getcwd() + "/" + folder
dir_to = os.getcwd()
copy_tree(dir_from, dir_to)

# Deploy to develop branch
message =  "Deploy: " + str(time())

subprocess.check_call(["rm", "-rf", folder])
subprocess.check_call(["git", "add", "."])
subprocess.check_call(["git", "commit", "-m", message])
subprocess.check_call(["git", "push", repo, branch + ":develop", "--force"])

# Build page

dir_from = os.getcwd() + "/src"
dir_to = os.getcwd()
copy_tree(dir_from, dir_to)

print("Executing Build Command " + str(build_command))

subprocess.check_call(build_command)

# Remove src files
for files in glob.glob("*.Rmd"):
    os.remove(files)

for files in glob.glob("*.yml"):
    os.remove(files)

for files in glob.glob("*.bib"):
    os.remove(files)

for files in glob.glob("*.tex"):
    os.remove(files)

subprocess.check_call(["rm", "-rf", "old"])
subprocess.check_call(["rm", "-rf", "src"])
subprocess.check_call(["rm", "-rf", "build.sh"])
subprocess.check_call(["rm", "-rf", "docs.Rproj"])
subprocess.check_call(["rm", "-rf", "./style.css"])

dir_from = os.getcwd() + "/_book"
dir_to = os.getcwd()
copy_tree(dir_from, dir_to)

# Deploy build to master branch
subprocess.check_call(["rm", "-rf", "_bookdown_files"])
subprocess.check_call(["rm", "-rf", "_book"])

subprocess.check_call(["git", "add", "."])
subprocess.check_call(["git", "commit", "-m", message])
subprocess.check_call(["git", "push", repo, branch + ":master", "--force"])

subprocess.check_call(["git", "checkout", "master"])
subprocess.check_call(["git", "stash"])
subprocess.check_call(["git", "branch", "-D", branch])

print("Deployed Docs")
