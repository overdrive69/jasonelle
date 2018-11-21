import os
import glob
import .config

from distutils.dir_util import copy_tree
from .shell import call

def rm(item):
    return call(["rm", "-rf", item])

def rm_glob(pattern):
    for files in glob.glob(pattern):
        os.remove(files)

def cwd():
    return os.getcwd()

def path(path_):
    return cwd() + "/" + path_

def copy_contents(dir_from, dir_to):
    copy_tree(dir_from, dir_to)

def copy_from_path_to_cwd(path_):
    copy_contents(path(path_), cwd())

def rm_all(paths):
    for item in paths:
        rm(item)

def rm_globs(globs):
    for item in globs:
        rm_glob(item)

def rm_all_except(paths, name):
    for item in paths:
        if item == name:
        continue
        rm(item)

def rm_all_in_config_except(name):
    rm_all_except(config.directories + config.files, name)