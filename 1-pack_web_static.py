#!/usr/bin/python3
"""Compress static files."""
from time import localtime
from fabric import task


@task
def do_pack(c):
    """Compress and version."""
    c.run('mkdir versions')
    tm = localtime()
    path = f"./versions/web_static_{tm.tm_year}{tm.tm_mon}\
            {tm.tm_mday}{tm.tm_hour}{tm.tm_min}{tm.tm_sec}.tgz"
    c.run(f"tar -zcvf {path} ./web_static")
    return path
