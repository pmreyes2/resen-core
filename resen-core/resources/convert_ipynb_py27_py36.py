#!/usr/bin/env python
#
# Code to convert a generic python2 and python3 to the corresponding
# py27 and py36 from the resen-core
#
from __future__ import (absolute_import, division, print_function)

import argparse
import glob
import json

PY27_VERSION = '2.7.15'
PY36_VERSION = '3.6.7'
PY27_NAME = 'py27'
PY36_NAME = 'py36'

def convert_ipynb(fnames):
    print(fname)
    with open(fname,'r') as fp:
        json_data = json.load(fp)
    changes = False
    if json_data['metadata']['kernelspec']['name'] not in [PY27_NAME,PY36_NAME]:
        if json_data['metadata']['language_info']['pygments_lexer'] == 'ipython2':
            json_data['metadata']['language_info']['version']=PY27_VERSION
            json_data['metadata']['kernelspec']['display_name'] = PY27_NAME
            json_data['metadata']['kernelspec']['name'] = PY27_NAME
            changes = True
        elif json_data['metadata']['language_info']['pygments_lexer'] == 'ipython3':
            json_data['metadata']['language_info']['version']=PY36_VERSION
            json_data['metadata']['kernelspec']['display_name'] = PY36_NAME
            json_data['metadata']['kernelspec']['name'] = PY36_NAME
            changes = True
    if changes:
        with open(fname,'w') as fp:
            json.dump(json_data,fp,indent=1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert to py27 or py36.')
    parser.add_argument('input_files', nargs='+',
            metavar='files_2_convert',
            help='list the files to convert')

    args = parser.parse_args()

    for fname in args.input_files:
        fnames = glob.glob(fname)
        for sfname in fnames:
            convert_ipynb(sfname)
