#!/usr/bin/env python
import sh
import os.path
import logging.handlers
import sys
import yaml

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


class Lightup(object):

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.git = sh.git.bake(_cwd=base_dir)

        # Load up the config
        self._get_config()


    def _get_config(self):
        config_file = os.path.join(self.base_dir, ".lightup.yaml")
        with open(config_file, 'r') as config:
            self.config = yaml.load(config)
            logger.debug(config)


    def status(self):
        status = self.git.status()
        logger.info(status)


if __name__ == "__main__":
    # Get the real location of this script
    real_loc = os.path.realpath(__file__)
    logger.info(real_loc)

    # The location of the parent codebase that has lightup embedded
    base_loc = os.path.join(os.path.dirname(real_loc), "..")
    l = Lightup(base_dir=base_loc)
    l.status()
