#!/usr/bin/env python
import sh
import os.path

# Link lightup.py to /etc/cron.hourly
script_path = os.path.join(os.path.abspath("./lightup.py"))
if not os.path.exists(script_path):
    raise Exception("%s doesn't exist" % script_path)
print(script_path)

with sh.contrib.sudo:
    sh.ln("-s", script_path, "/etc/cron.hourly/lightup.py")
