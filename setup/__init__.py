#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os.path import *
from imp import *
try:
    # pypi.python.org/pypi/setuptools
    from setuptools import setup # python setup.py develop
except ImportError:
    # standart library
    from distutils.core import setup
import sys
import warnings

# https://docs.python.org/2/distutils/setupscript.html
# https://docs.python.org/3/distutils/setupscript.html

def pyfiles(dir):
    list = os.listdir(dir)
    list = filter(lambda l:splitext(l)[1]==".py" and l.find("__")<0,list)
    return list

def main():
    dir = dirname(dirname(__file__))
    if not dir or dir==".": dir=os.getcwd()
    sys.path.append(dir)
    kwargs=dict()

    sys.path.append(dirname(__file__))
    files = pyfiles(dirname(__file__))
    # RuntimeWarning: Parent module 'modname' not found while handling absolute import
    warnings.simplefilter("ignore", RuntimeWarning)
    for file in files:
        try:
            fullpath=join(dir,"setup",file)
            with open(fullpath,'rb') as fp:
                # .hidden.py invisible for mdfind
                mod = load_module(file,fp,fullpath,('.py', 'rb', PY_SOURCE))  
                if not hasattr(mod,'__all__'):
                    raise ValueError("ERROR: %s __all__ required" % file)
                for k in getattr(mod,"__all__"):
                    if getattr(mod,k):
                        kwargs[k] = getattr(mod,k)
        except AttributeError: # variable from __all__ not initialized
            continue
    if len(sys.argv)==1 and len(getattr(mod,"__all__"))>0:
        print("%s: %s" % (file,mod.__all__))

    name = basename(dir).lower().replace(".py","")
    while name and name[-1]=="_": 
        name=name[0:-1]

    def isstring(object):
        try:
            int(object)
            return False
        except ValueError:
            return True
        except:
            return False
    if len(sys.argv)==1 and kwargs:
        print('\nsetup(name="%s",' % name)
        # for i,(k,v) in enumerate(sorted(kwargs.iteritems(),key=lambda (k,v):k),1): # python2
        for i,k in enumerate(sorted(list(kwargs.keys())),1): # python3
            v=kwargs[k]
            print("    %s = %s%s" % (k,'"%s"' % v if isstring(v) else v,"," if i!=len(kwargs) else ""))
        print(')')  

    if len(sys.argv)==1: return
    setup(name=name,**kwargs)

#if __name__=="__main__":
main()
