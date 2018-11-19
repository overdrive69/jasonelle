#!/usr/bin/env python3
# coding: utf-8
import subprocess

print("Deployment Script")

print("Detecting Changes")

print("Deploying to Repos")

print("Deploying Website")

try:
    result = subprocess.check_output(["python", "scripts/cascades/website.py"]).decode()
    print("Result", result)
except:
    pass

print("Deploying Docs")

try:
    result = subprocess.check_output(["python", "scripts/cascades/docs.py"]).decode()
    print("Result", result)
except:
    pass

try:
    subprocess.check_call(["git", "stash"])
    subprocess.check_call(["git", "checkout", "master"])
    subprocess.check_call(["git", "stash"])
    subprocess.check_call(["git", "branch", "-D", "deploy"])
except:
    pass

print("Jobs Done")
