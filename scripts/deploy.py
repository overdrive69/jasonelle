#!/usr/bin/env python3
# coding: utf-8
import subprocess
from helpers import config, shell

print("Deployment Script")

print("Detecting Changes")

print("Deploying to Repos")

print("Deploying Website")

try:
    result = shell.py(config.cascades["website"])
    print("Result", result)
except:
    pass

print("Deploying Docs")

try:
    result = shell.py(config.cascades["docs"])
    print("Result", result)
except:
    pass

try:
    shell.git_stash()
    shell.git_checkout_master()
    shell.clean()
    shell.git_hard_reset()
except:
    pass

print("Jobs Done")
