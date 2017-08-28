#!/usr/bin/env python
import sh

git = sh.git.bake(_cwd='.')
status = git.status()
print(status)
