import argparse
import logging

import yaml

from common import *


def main(directory, attribute, value):
    """
    Updates an attribute in the control file. You can reference the current
    value of the attribute in 'value' using a format string '{}'"
    :param directory: Package root
    :param attribute: Name of the attribute to change
    :param value: String to which you'd like to set the attribute
    :return: True if the attribute was updated.
    """
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    package = get_package_root(directory)
    control_file = package.joinpath('control/control')
    logger.debug("Loading Control File: %s", control_file)
    if not control_file.exists():
        raise FileNotFoundError("Control file not found: {}".format(
            package
        ))

    with open(control_file, 'r+') as cf:
        should_save = False
        control = yaml.safe_load(cf)

        if attribute in control:
            control[attribute] = value
            should_save = True
        else:
            raise Exception("Attribute {} not found in the control file".format(
                            attribute))
        if should_save:
            # Return to start of file
            cf.seek(0)
            yaml.dump(control, cf)
            # remove the rest of the file
            cf.truncate()


parser = argparse.ArgumentParser()
parser.add_argument('-d',
                    '--directory',
                    help="""Root directory to create for this package. You can 
                    also set the PKG_ROOT_DIRECTORY environment variable. This 
                    directory must be an absolute path.""",
                    required=False,
                    default=None)
parser.add_argument('-a',
                    '--attribute',
                    help='The name of the attribute you would like to change.',
                    required=True)
parser.add_argument('-v',
                    '--value',
                    help='The value to which you would like to set the attribute.',
                    required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args.directory, args.attribute, args.value)
