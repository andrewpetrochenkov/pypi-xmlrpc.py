#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

__all__ = ["scripts"]


def valid_script_name(name):
    if name[0] == ".":  # skip .hidden files
        return False
    if " " in name:  # skip filename with ' ' space
        return False
    if ".txt" in name:  # skip .txt files
        return False
    return True


def _scripts(path):
    listdir = os.listdir(path)
    for l in listdir:
        if not valid_script_name(l):
            continue
        dst = os.path.join("/usr/local/bin/%s" % l)
        if os.path.exists(dst) and not os.path.isfile(dst):
            raise OSError("ERROR: %s EXISTS and NOT FILE" % dst)
        fullpath = os.path.join(path, l)
        if os.path.isfile(fullpath):
            yield os.path.join(folder, l)


repo = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


folder = "bin"
path = os.path.join(repo, folder)
if os.path.exists(path) and os.path.isdir(path):
    scripts = list(_scripts(path))
else:
    if __name__ == "__main__":
        print("SKIP: %s/ NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
