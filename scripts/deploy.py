#!/usr/bin/env python3
# coding: utf-8
import subprocess

print("Deployment Script")

print("Detecting Changes")

print("Deploying to Repos")

subprocess.call(["python", "scripts/deploy/website.py"])

print("Jobs Done")
