#!/usr/bin/python3
from fabric.api import *
from os import path

env.hosts = ['54.157.132.219', '100.26.156.236']

def do_deploy(archive_path):
    if not archive_path:
        return False

    if not path.exists(archive_path):
        return False

    put(archive_path, "/tmp/")

    file_name = archive_path.split("/")[-1]
    final = file_name.split(".")[0]
    # format === versions/web_static_20170315003959.tgz

    run("mkdir -p /data/web_static/releases/{}".format(final))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(file_name, final))
    run("rm /tmp/{}".format(file_name))
    run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(final, final))
    run("rm -rf /data/web_static/releases/{}/web_static".format(final))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{} /data/web_static/current".format(final))
    print("New version deployed!")
