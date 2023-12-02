#!/usr/bin/env python3

import re
import sys
from collections import OrderedDict
from icecream import ic

max_size = 100000

fs_size = 70000000

space_reqd = 30000000

dirs = OrderedDict()

sumsize = 0

pathinfo = []


if __name__ == "__main__":
    with open(sys.argv[1]) as input:
        listing = input.readlines()
        for line in listing:
            ic(pathinfo)
            line = line.strip()
            ic(line)
            if line.startswith("$ cd"):
                dirname = line.split()[-1]
                if dirname != '..':
                    print(f"change into {dirname}")
                    pathinfo.append(dirname)
                    fullpath = '/'.join(pathinfo)
                    if not dirs.get(fullpath):
                        dirs[fullpath] = 0
                else:
                    cwd = pathinfo.pop()
                    parent = pathinfo[-1]
                    parentpath = '/'.join(pathinfo)
                    current_path = parentpath + '/' + cwd
                    dirs[parentpath] += dirs[current_path]
                    print(f"changing from {current_path} to {parentpath}")
                    ic(parent, cwd, dirs[parentpath], dirs[current_path])
            elif line.startswith("$ ls"):
                next
            elif re.match(r'^(\d+)', line):
                m = re.match(r'^(\d+)', line)
                current_path = '/'.join(pathinfo)
                dirs[current_path] += int(m.group(1))
                ic(current_path, m.group(1))
            elif line.startswith("dir"):
                next
    for k, v in dirs.items():
        if v < max_size:
            sumsize += v
    ic("part1", sumsize)
    available = fs_size - dirs['/']
    delta = space_reqd - available
    ic(available)
    ic(delta)
    dirs2bedeleted = []
    for d, s in dirs.items():
        if dirs[d] + available > space_reqd:
            ic(d, dirs[d])
            dirs2bedeleted.append(s)

    ic(sorted(dirs2bedeleted))

