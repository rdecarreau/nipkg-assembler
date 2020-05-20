"""Common utility functions for the package"""
import os
import shutil
import argparse
import pathlib

PKG_ROOT_DIRECTORY = 'PKG_ROOT_DIRECTORY'


def get_package_root(directory):
    """
    Finds the root of the package
    :param directory:
    :return: root folder for the package:
    """
    # First, check for the -d input
    if directory is not None:
        destination_dir = pathlib.Path(directory)
        # if relative path, add cwd
        if not destination_dir.is_absolute():
            destination_dir = pathlib.Path(os.getcwd(), directory)
    # Next, check the environment variable
    elif os.getenv(PKG_ROOT_DIRECTORY) is not None:
        destination_dir = pathlib.Path(os.getenv(PKG_ROOT_DIRECTORY))
    # Finally, use current working directory
    else:
        destination_dir = pathlib.Path(os.getcwd())

    return destination_dir


def make_dir(directory, template, overwrite):
    """
    This will create a directory at path and return True if successful.
    If the path exists and you want to overwrite, set overwrite to True
    :param directory: Absolute directory to create the path
    :param template: Path to the template package
    :param overwrite: True to delete the one which exists
    """
    # This is just to ensure the type is Path()
    _dir = pathlib.Path(directory)
    if _dir.exists():
        if overwrite:
            shutil.rmtree(_dir)
        else:
            raise FileExistsError(
                'Directory "{}" already exists and "overwrite" is false'.format(
                    _dir.absolute()))
    copytree(template, _dir.absolute())


def copytree(src, dst, symlinks=False, ignore=None):
    """ Override for copytree which does directory and files"""
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
