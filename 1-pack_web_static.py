#!/usr/bin/python3
"""Compress static files."""
from datetime import datetime
from fabric import task


@task
def do_pack(c):
    """Compress and version."""
    try:
        c.run('mkdir versions')
        tm = datetime.now().strftime('%Y%m%d%H%M%s')
        path = "./versions/web_static_{}.tgz".format(tm)
        c.run("tar -zcvf {} ./web_static".format(path))
    except:
        return None
    return path
