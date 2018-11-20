#!/usr/bin/env python3
# coding: utf-8
import subprocess
from helpers import config, shell, utils

print("Deployment Script")
print("Detecting Changes")
print("Deploying to Repos")

print("Deploying Website")
utils.deploy("website")

print("Deploying Docs")
utils.deploy("docs")

utils.cleanup()
print("Jobs Done")
