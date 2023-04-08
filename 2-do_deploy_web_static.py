#!/usr/bin/python3
"""Fabric script generating a .tgz archive from the
   contents of the web_static folder
"""
from datetime import datetime
from fabric.api import *
import os.path


env.hosts = ['54.166.139.118', '34.207.237.37']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ To compress or Distribute an archive to your web servers.
       Arguments:
        archive_path: Path to an already achrived file.
    """
    #  check if archive exist.
    if os.path.isfile(archive_path):
        try:
            #  Upload the archive to remote /tmp/
            put("{}".format(archive_path), "/tmp/")
            release = '/data/web_static/releases/'
            current = "/data/web_static/current"
            trim_arch = archive_path.split('/')[1].split('.')[0]
            #  Uncompress the archive to the release folder
            run("mkdir -p {}{}/".format(release, trim_arch))
            run("tar -xzf /tmp/{} -C {}{}/".format(archive_path.split('/')[1],
                                                   release,
                                                   trim_arch))
            #  Delete the archive from the web server
            run("rm /tmp/{}".format(archive_path.split('/')[1]))
            # Move Uncompressed files to release version
            run("mv {}{}/web_static/* {}{}".format(release, trim_arch,
                                                   release, trim_arch))
            run("rm -rf {}{}/web_static/".format(release, trim_arch))
            #  Delete current the symbolic link.
            run("rm -rf {}".format(current))
            #  Create a new the symbolic link
            run("ln -sf {}{} {}".format(release, trim_arch, current))
            return True
        except Exception as e:
            return False
    else:
        return False


def do_pack():
    """ Generating  a .tgz archive from the contents of
       the web_static folder of your AirBnB Clone repo
    """
    local("mkdir -p versions")
    created_at = datetime.now().strftime("%Y%m%d%H%M%S")
    # From the archive path and command
    arch_path = "versions/web_static_{}.tgz".format(created_at)
    command = "tar -cvzf {} web_static".format(arch_path)
    try:
        # perform fab command
        local(command)
        return arch_path
    except Exception as e:
        return None
