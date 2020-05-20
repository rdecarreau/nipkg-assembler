import argparse

from common import *


def main(directory, template, overwrite):
    """
    Copies the default_package to the directory passed in, the environment
    variable PKG_ROOT_DIRECTORY or the current working directory.
    :param directory: Directory to create for this package
    :param template: Path to the template package to be used
    :param overwrite: Set to True to remove directory if it exists
    :return: Generates a folder on disk at 'directory'
    """
    destination_dir = get_package_root(directory)
    make_dir(destination_dir, template, overwrite)


parser = argparse.ArgumentParser()
parser.add_argument('-d',
                    '--directory',
                    help="""Root directory to create for this package. You can 
                    also set the PKG_ROOT_DIRECTORY environment variable. This 
                    directory must be an absolute path.""",
                    required=False,
                    default=None)
parser.add_argument('-t',
                    '--template',
                    help='Template package to use when creating a new package',
                    required=True)
parser.add_argument('-o',
                    '--overwrite',
                    help='Set to True to remove "directory" if it exists',
                    type=str2bool,
                    nargs='?',
                    required=False,
                    default='False')

if __name__ == '__main__':
    args = parser.parse_args()
    main(args.directory, args.template, args.overwrite)
