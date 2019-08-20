#!/usr/bin/python3

from fabric.api import *


env.hosts = ['35.196.108.226', '34.74.255.195']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"


def do_clean(number=0):
    """ Function deletes out-of-date archives """
    num = int(number)
    with lcd('versions'):
        if num == 0 or number == 1:
            local("ls -tr | head -n -1 | xargs rm -rf")
        else:
            local("ls -tr | head -n -{} | xargs rm -rf".format(number))
    with cd('/data/web_static/releases'):
        if number == 0 or number == 1:
            run("ls -tr | head -n - 1 | xargs rm -rf")
        else:
            run("ls -tr | head -n -{} | xargs rm -rf".format(number))
