#!/usr/bin/env python3
# coding: utf-8

import subprocess

def call(params):
    print("Calling ", params)
    return subprocess.check_output(params).decode()

def py(params):
    params = ["python"] + params
    return call(params)

def git(params):
    params = ["git"] + params
    return call(params)

def git_hard_reset():
    params = ["reset", "HEAD", "--hard"]
    return git(params)

def git_stash():
    params = ["stash"]
    return git(params)

def git_clean():
    params = ["clean", "-x", "-d", "-f"]
    return git(params)

def git_add_all():
    params = ["add", "."]
    return git(params)

def git_commit(message):
    params = ["commit", "-m", message]
    return git(params)

def git_force_push(remote, branch, branch_remote = None):
    branch_remote = branch_remote or branch
    params = ["push", remote, branch + ":" + branch_remote, "--force"]
    return git(params)

def git_checkout(branch):
    params = ["checkout", branch]
    return git(params)

def git_checkout_master():
    return git_checkout("master")

def git_checkout_new_branch(branch):
    params = ["checkout", "-b", branch]
    return git(params)

def git_branch_remove(branch):
    params = ["branch", "-D", branch]
    return git(params)

def git_remote_add(name, url):
    params = ["remote", "add", name, url]
    return git(params)

def git_branch_safe_create(branch):
    try:
        git_checkout_new_branch(branch)
    except:
        git_branch_remove(branch)
        git_checkout_new_branch(branch)



