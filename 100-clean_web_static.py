#!/usr/bin/python3
"""a Fabric script (based on the file 3-deploy_web_static.py) that deletes
 out-of-date archives, using the function do_clean"""
import os
from fabric.api import *
env.hosts = ["54.175.254.46", "18.210.20.195"]


def do_clean(number=0):
    """Delete out-of-date archives"""
    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    archives = os.listdir("versions")
    archives_sorted = sorted(archives)
    archives_to_remove = archives_sorted[:-number]
    with lcd("versions"):
        for archive in archives_to_remove:
            local(f"rm {archive}")
    archives = run("ls -tr /data/web_static/releases").split()
    archives_filtered = [a for a in archives if "web_static_" in a]
    archives_filtered_sorted = sorted(archives_filtered)
    archives_to_remove = archives_filtered_sorted[:-number]
    with cd("/data/web_static/releases"):
        for archive in archives_to_remove:
            run(f"rm -rf {archive}")
