import argparse
import pathlib
from common import copytree, get_package_root


def main(directory, source_folder, target_root):
    """
    Copies the source folder and its subfolders to the package, under the
    desired target_root. This will not verify the target_root is proper.
    """
    source_folder = pathlib.Path(source_folder)
    if not source_folder.exists():
        raise FileNotFoundError(
            "Source folder not found: {}".format(source_folder))
    package_root = get_package_root(directory)
    if not package_root.exists():
        raise FileNotFoundError(
            "Root folder for the package was not found: {}".format(directory))
    target_root_dir = pathlib.Path(package_root, 'data', target_root)
    if not target_root_dir.exists():
        # Create a new target root folder
        target_root_dir.mkdir()

    copytree(source_folder, target_root_dir.joinpath(source_folder))


parser = argparse.ArgumentParser()
parser.add_argument('-d',
                    '--directory',
                    help="""Root directory to create for this package. You can 
                    also set the PKG_ROOT_DIRECTORY environment variable. This 
                    directory must be an absolute path.""",
                    required=False,
                    default=None)
parser.add_argument('-s',
                    '--source_folder',
                    help="""Path to the directory you would like to add to 
                    your package.""",
                    required=True)
parser.add_argument('-t',
                    '--target_root',
                    help="""Installation target root. See NIPM documentation 
                    for options""",
                    required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args.directory, args.source_folder, args.target_root)
