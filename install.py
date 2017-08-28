#!/usr/bin/env python
import sh
import sys
import os.path

# TODO Check that sh is installed and print a nice error if not.

LIGHTUP_DIR="lightup"

# On initial install: `git submodule init` to get main scripts
git = sh.git.bake(_cwd=os.path.dirname(__file__))
print(git.submodule.update("--init", "--recursive", LIGHTUP_DIR))

# Now use the code to install itself!
sys.path.insert(0, LIGHTUP_DIR)
from lightup import Lightup

l = Lightup()
l.install()
