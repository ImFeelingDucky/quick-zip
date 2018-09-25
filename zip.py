#!/usr/bin/env python3
"""Create a .zip file of all .py files in the current directory"""

import os
import zipfile
import argparse

FILENAME = 'my_zip'
PROMPT_BEFORE_OVERWRITING = True
DEFAULT_EXTENSIONS = ['.py', '.java']

def create_parser():
    """Return a configured argparse.ArgumentParser instance"""
    parser = argparse.ArgumentParser(description='Create a .zip file.')

    parser.add_argument(
        '-e',
        '--extensions',
        metavar='EXTENSIONS',
        nargs='*',
        type=str,
        default=DEFAULT_EXTENSIONS,
        help='a list of extensions files ending in which will be zipped (default: %(default))'
    )
    parser.add_argument(
        '-f',
        '--filename',
        metavar='FILENAME',
        type=str,
        default=get_filename(),
        help='your student number. This will be the name of the zip file.'
    )

    return parser

def get_filename():
    """
    Return the filename the zip that will be created should have.

    Having to edit source code to set configuration is bad UX, so we may get this from an config file in a later version.
    """
    return FILENAME

def main():
    args = create_parser().parse_args()

    zip_filename = args.filename + '.zip'

    if PROMPT_BEFORE_OVERWRITING and zip_filename in os.listdir('.'):
        if input('A zip ({}) already exists. Would you like to overwrite it? Y/N\n'.format(zip_filename)).lower() not in ('y', 'yes'):
            print('You chose not to overwrite the existing zip. Aborting...')
            return

    files_to_zip = [f for f in os.listdir('.') if os.path.splitext(f)[1] in args.extensions]

    print('Zipping files:', ', '.join(files_to_zip))

    with zipfile.ZipFile(zip_filename, 'w') as zip:
        for f in files_to_zip:
            zip.write(f)

    print(f'Files zipped as {zip_filename}')

if __name__ == '__main__':
    main()
