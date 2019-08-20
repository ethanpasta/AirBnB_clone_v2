#!/usr/bin/python3

import datetime
from fabric.api import local


def do_pack():
    """ Function generates a .tgz archive from the
        contents of the 'web_static' folder
    """
    local("mkdir -p versions")
    now = datetime.datetime.now()
    filename = "versions/web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S"))
    result = local("tar -czvf {} web_static".format(filename))
    if result.failed:
        return None
    return result
