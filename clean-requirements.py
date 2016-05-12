#!/usr/bin/env python
# encoding: utf-8
"""

source project1/prj.env/bin/activate
pip install pip_check_reqs

python clean-requirements.py project1/requirements.txt project1/src


"""
import sys

from os import system
from os.path import dirname, abspath

PATH = dirname(abspath(__file__))
if len(sys.argv) < 2:
    print('''
    python clean-requirements.py project1/requirements.txt project1/src

    ''')

requirements_path, src_path = sys.argv[1:]
print requirements_path, src_path
tmp_unused = requirements_path + '_unused'
tmp_clean = requirements_path + '_clean'

cmd = 'pip-extra-reqs %s &> %s' % (src_path, tmp_unused)
print(cmd)
system(cmd)

with open(requirements_path) as fp:
    code = fp.read()

exts = set()
with open(tmp_unused) as fp:
    code2 = fp.read()

    for line in code2.split('\n'):
        t = line.split(' ')[0].strip()
        if t:
            exts.add(t)

with open(requirements_path) as fp:
    with open(tmp_clean, 'w') as fp2:
        code = fp.read()
        for line in code.split('\n'):
            arr = line.split('==')
            if arr[0] in exts:
                arr[0] = '#' + arr[0]
            fp2.write('=='.join(arr) + '\n')

print("write cleand:%s" % tmp_clean)
