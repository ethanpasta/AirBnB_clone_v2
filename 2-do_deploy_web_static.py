#!/usr/bin/python3

from fabric.api import env, run, put, sudo
import os


env.hosts = ['35.196.108.226', '34.74.255.195']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"


def do_deploy(archive_path):
    """ Function distributes an archive to web servers """
    if not os.path.exists(archive_path):
        return False
    filename = os.path.basename(archive_path)
    name = filename.split(".")[0]
    result = put(archive_path,
                 "/tmp/{}".format(filename))
    if result.failed:
        return False
    result = run("mkdir -p /data/web_static/"
                 "releases/{}/".format(name))
    if result.failed:
        return False
    result = run("tar -xzf /tmp/{} -C"
                 "/data/web_static/releases/{}/".format(filename, name))
    if result.failed:
        return False
    result = run("rm /tmp/{}".format(filename))
    if result.failed:
        return False
    result = run("mv /data/web_static/releases/{}"
                 "/web_static/* /data/web_static/releases/"
                 "{}/".format(name, name))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/"
                 "{}/web_static/".format(name))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run("ln -s /data/web_static/releases/{}/ "
                 "/data/web_static/current".format(name))
    if result.failed:
        return False
    sudo("service nginx restart")
    return True
