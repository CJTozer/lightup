#!/usr/bin/env python
import sh
import os.path
from lightup import Lightup

# TODO Check that sh is installed and print a nice error if not.

# Git updates:
### On initial install: `git submodule init`
### Every time get latest: `git submodule update --remote lightup-py`

# Get the real location of this script, following symlinks.
real_loc = os.path.realpath(__file__)

# The location of the parent codebase that has lightup-py embedded
base_loc = os.path.join(os.path.dirname(real_loc), "..")
l = Lightup(lightup_base_dir=base_loc)
l.status()
