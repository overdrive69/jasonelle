#!/usr/bin/env python3
# coding: utf-8
import subprocess

print("Deployment Script")

print("Detecting Changes")

print("Deploying to Repos")

print("Deploying Website")
result = subprocess.check_output(["python", "scripts/cascades/website.py"]).decode()
print("Result", result)

subprocess.check_call(["git", "checkout", "master"])
subprocess.check_call(["git", "stash"])
subprocess.check_call(["git", "branch", "-D", "develop"])

print("Jobs Done")
