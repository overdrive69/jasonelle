#!/usr/bin/env python3
# coding: utf-8
import subprocess
from helpers import config, shell, utils
from ratlog import Log

log = Log()
log("Deployment Script")
log("Detecting Changes")
log("Deploying to Repos")

log("Deploying Website")
utils.deploy("website")

log("Deploying Docs")
utils.deploy("docs")

utils.cleanup()
log("Jobs Done")
