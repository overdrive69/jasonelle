#!/usr/bin/env python3
# coding: utf-8
import subprocess

subprocess.call(["git", "config", "--global" , "user.email " "travis@travis-ci.org"])
subprocess.call(["git", "config", "--global" , "user.name " "Travis CI"])

print("Deployment Script")

print("Detecting Changes")

print("Deploying to Repos")

print("Deploying Website")
result = subprocess.check_output(["python", "scripts/deploy/website.py"]).decode()
print("Result", result)

print("Jobs Done")
