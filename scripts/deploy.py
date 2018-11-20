#!/usr/bin/env python3
# coding: utf-8
import subprocess
from helpers import config, shell

print("Deployment Script")

print("Detecting Changes")

print("Deploying to Repos")

print("Deploying Website")

try:
    params = [config.cascades["website"]]
    result = shell.py(params)
    print("Result", result)
except:
    print("Error")
    pass

print("Deploying Docs")

try:
    params = [config.cascades["docs"]]
    result = shell.py(params)
    print("Result", result)
except:
    print("Error")
    pass

try:
    shell.git_stash()
    shell.git_checkout_master()
    shell.clean()
    shell.git_hard_reset()
except:
    print("Some step failed")
    pass

print("Jobs Done")
