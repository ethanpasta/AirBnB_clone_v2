#!/usr/bin/python3

from fabric.api import env, run, put
import os
import re


env.hosts = ['35.196.108.226', '34.74.255.195']


def do_pack():
    """ Function generates a .tgz archive
        from the contents of the 'web_static' folder
    """
    local("mkdir -p versions")
    now = datetime.datetime.now()
    filename = "versions/web_static_{}.tgz".format(
        now.strftime("%Y%m%dT%H%M%S"))
    result = local("tar -czvf {} web_static".format(filename))
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """ Function distributes an archive to two web servers """
    if not os.path.exists(archive_path):
        return False
    match = re.search(r'^versions/(web_static_.+)\.tgz', archive_path)
    filename = match.group(1)
    result = put(archive_path,
                 "/tmp/{}.tgz".format(filename))
    if result.failed:
        return False
    result = run("mkdir -p /data/web_static/"
                 "releases/{}/".format(filename))
    if result.failed:
        return False
    result = run("tar -xzf /tmp/{}.tgz -C"
                 "/data/web_static/releases/{}/".format(filename, filename))
    if result.failed:
        return False
    result = run("rm /tmp/{}.tgz".format(filename))
    if result.failed:
        return False
    result = run("mv /data/web_static/releases/{}"
                 "/web_static/* /data/web_static/releases/"
                 "{}/".format(filename, filename))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/"
                 "{}/web_static/".format(filename))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run("ln -s /data/web_static/releases/{}/ "
                 "/data/web_static/current".format(filename))
    if result.failed:
        return False
    print("New version deployed!")
    return True
