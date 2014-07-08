#!/usr/local/bin/python

from subprocess import Popen, PIPE, STDOUT, call


def packageCategory():
    category = ['accessibility', 'arabic', 'archivers', 'astro', 'audio',
    'benchmarks', 'biology', 'cad', 'chinese', 'comms', 'converters',
    'databases', 'deskutils', 'devel', 'dns', 'editors',
    'emulators', 'finance', 'french', 'ftp', 'games', 'german', 'graphics',
    'hebrew', 'hungarian', 'irc', 'japanese', 'java', 'korean', 'lang',
    'mail', 'math', 'misc', 'multimedia', 'net', 'net-im', 'net-mgmt',
    'net-p2p', 'news', 'palm', 'polish', 'ports-mgmt', 'portuguese', 'print',
    'russian', 'science', 'security', 'shells', 'sysutils', 'textproc',
    'ukrainian', 'vietnamese', 'www', 'x11', 'x11-clocks', 'x11-drivers',
    'x11-fm', 'x11-fonts', 'x11-servers', 'x11-themes','x11-toolkits','x11-wm']
    return category

def packagelist():
    cmd = "pkg rquery -a '%o' | sort"
    pkg_out = Popen(cmd, shell=True, stdout=PIPE, close_fds=True)
    lst = pkg_out.stdout.readlines()
    return lst