#!/usr/bin/env python
import sh
import os.path
import logging.handlers
import sys

# Set up logging
logger = logging.getLogger("lightup.py")
logger.setLevel(logging.DEBUG)

# Log to syslog
syslog_handler = logging.handlers.SysLogHandler(address ='/dev/log')
syslog_handler.setLevel(logging.INFO)
syslog_formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
syslog_handler.setFormatter(syslog_formatter)
logger.addHandler(syslog_handler)

# Also log to stdout - for testing only
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(stdout_formatter)
logger.addHandler(stdout_handler)

# Test command - git status
git = sh.git.bake(_cwd='.')
status = git.status()
logger.info(status)

# Get the real location of this script
real_loc = os.path.realpath(__file__)
logger.info(real_loc)
