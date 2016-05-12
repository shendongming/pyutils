#!/usr/bin/env python
# encoding: utf-8

"""
wget https://github.com/shendongming/pyutils/raw/master/update-hosts.py
sudo python update-hosts.py
curl https://www.google.com/ncr
更新hosts 文件
@author: sdm
@software: PyCharm
@file: update-hosts.py
@time: 16/5/12 09:44
"""

import datetime
import logging
import shutil
import time
import urllib
from os.path import exists
from os.path import getmtime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('hosts')
src = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
cache_host = '/tmp/hosts.txt'
hosts = ''
if not exists(cache_host) or time.time() - getmtime(cache_host) > 1800:

    log.info('load:%s' % src)
    with open(cache_host, 'w') as fp:
        f = urllib.urlopen(src)
        hosts = f.read()
        fp.write(f.read())
else:

    log.info('load cache:%s' % cache_host)
    with open(cache_host) as fp:
        hosts = fp.read()

# read system hosts
now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')

shutil.copy('/etc/hosts', '/tmp/hosts.bak.%s' % now)
log.info('bak hosts:%s=>%s' % ('/etc/hosts', '/tmp/hosts.bak.%s' % now))
with open('/etc/hosts') as fp:
    old_hosts = fp.read()
    hosts_start = old_hosts.find('# https://github.com/racaljk/hosts')
    hosts_end = old_hosts.find('# Modified hosts end')

    if hosts_start != -1 and hosts_end != -1:
        hosts_new = old_hosts[0:hosts_start] + "\n" + old_hosts[hosts_end + len('# Modified hosts end'):]
    else:
        hosts_new = old_hosts

hosts_new += "\n" + hosts

# print 'new_hosts:'
# print hosts_new
with open('/etc/hosts', 'w') as fp:
    fp.write(hosts_new)

log.info('write /etc/hosts done')
