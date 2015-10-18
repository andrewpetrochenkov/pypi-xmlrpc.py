#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

dir = os.path.dirname(__file__)
if not dir or dir==".": dir=os.getcwd()
sys.path.append(dir)

if __name__=="__main__":
	import setup

