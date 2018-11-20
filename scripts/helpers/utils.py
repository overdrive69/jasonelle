
import .config
import .shell

from time import time

def timestamp():
    return str(time())

def deploy(name):
    try:
        params = [config.cascades[name]]
        result = shell.py(params)
        print("Result", result)
    except:
        print("Error")
        pass

def cleanup():
    try:
        shell.git_stash()
        shell.git_checkout_master()
        shell.clean()
        shell.git_hard_reset()
    except:
        print("Some step failed")
        pass