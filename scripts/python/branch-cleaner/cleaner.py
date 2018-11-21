#!/usr/bin/env python3
# coding:utf-8
"""Use tags to archive unwanted branches.

This script would delete all branches except the default.
In order to preserve the branch contents, they will be stored
in  a tag with the format archive/branch-{branch_name}

This helps keeping the repository clean and tidy.

See README.md for details.

This Source Code Form is subject to the terms of the Mozilla Public License, 
v. 2.0. If a copy of the MPL was not distributed with this file, 
You can obtain one at https://mozilla.org/MPL/2.0/.

"""

import subprocess
import sys

# The branch that would not be deleted
default = "master"
consider_current_branch_as_default = True

# Other branches to keep around
# example 'master', develop'
protected = []

# Where to push changes
origin = "origin" 

# Enable verbose output 
# ./cleaner -v
quiet = (len(sys.argv) <= 1)

branches = subprocess.check_output(["git", "branch", "-a"]).decode().split("\n")

is_default_branch = False

for branch in branches:

    branch = branch.strip()
    
    if branch == "":
        continue
    
    if branch.startswith("remotes/origin/"):
        branch = branch[len("remotes/origin/"):]

    is_default_branch = branch.startswith("*")
    
    if is_default_branch:
        branch = branch[1:].strip()

        if consider_current_branch_as_default:
            quiet or print("Branch {} is now default".format(branch))
            default = branch
            continue
    
    if is_default_branch or branch in protected:
        quiet or print("Branch {} skipped".format(branch))
        continue
    
    # Checkout to branch and tag its contents
    subprocess.call(["git", "checkout", branch])
    tag = "archive/branch-{}".format(branch)
    
    # Save contents to local and origin
    subprocess.call(["git", "tag", tag])
    subprocess.call(["git", "push", origin, "tag", tag])
    
    # Delete branch from local and origin
    subprocess.call(["git", "checkout", default])
    subprocess.call(["git", "push", origin, ":{}".format(branch)])
    subprocess.call(["git", "branch", "-D", branch])
    
    quiet or print("Archived branch", branch)

quiet or print("Jobs Done")