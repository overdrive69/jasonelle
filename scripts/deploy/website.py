#!/usr/bin/env python3
# coding: utf-8
import subprocess
from os import environ

# Deploys the website directory to the website repo
subprocess.call(["git", "remote", "add", "website", "git@github.com:jasonelle/jasonelle.github.io.git"])
subprocess.call(["git", "checkout", "-b", "develop"])
subprocess.call(["rm", "-rf", "celljs"])
subprocess.call(["rm", "-rf", "stjs"])
subprocess.call(["rm", "-rf", "jasonette"])
subprocess.call(["rm", "-rf", ".gitignore"])
subprocess.call(["rm", "-rf", ".travis.yml"])
subprocess.call(["rm", "-rf", "README.md"])
subprocess.call(["rm", "-rf", "LICENSE"])
subprocess.call(["rm", "-rf", "celljs"])
subprocess.call(["rm", "-rf", "scripts"])

subprocess.call(["cd", "website"])
subprocess.call(["mv", "-R", "*", ".."])
subprocess.call(["cd", ".."])
subprocess.call(["rm", "-rf", "website"])
subprocess.call(["git", "add", "."])

message =  "Travis build: " + environ["TRAVIS_BUILD_NUMBER"]
subprocess.call(["git", "commit", "-m", message])
subprocess.call(["git", "push", "website", "develop"])
subprocess.call(["git", "checkout", "master"])
subprocess.call(["git", "branch", "-D", "develop"])

print("Deployed Website")
