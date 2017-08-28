#!/usr/bin/env python
import sh
import os.path
from lightup import Lightup

# TODO Check that sh is installed and print a nice error if not.

# Git updates:
### On initial install: `git submodule init`
### Every time get latest: `git submodule update --remote lightup-py`

l = Lightup()
l.install()
