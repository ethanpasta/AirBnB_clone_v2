#!/usr/bin/python3

from fabric.api import env, run, put
import os


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
    result = put("versions/web_static_20190820T000226.tgz",
                 "/tmp/web_static_20190820T000226.tgz")
    if result.failed:
        return False
    result = run("mkdir -p /data/web_static/"
                 "releases/web_static_20190820T000226/")
    if result.failed:
        return False
    result = run("tar -xzf /tmp/web_static_20190820T000226.tgz -C"
                 "/data/web_static/releases/web_static_20190820T000226/")
    if result.failed:
        return False
    result = run("rm /tmp/web_static_20190820T000226.tgz")
    if result.failed:
        return False
    result = run("mv /data/web_static/releases/web_static_20190820T000226"
                 "/web_static/* /data/web_static/releases/"
                 "web_static_20190820T000226/")
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/"
                 "web_static_20190820T000226/web_static/")
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run("ln -s /data/web_static/"
                 "releases/web_static_20190820T000226/ "
                 "/data/web_static/current")
    if result.failed:
        return False
    print("New version deployed!")
    return True
