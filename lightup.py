#!/usr/bin/env python
import sh
import os.path
import logging.handlers
import sys
import yaml
from utils import merge_dicts

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

    def __init__(self, lightup_base_dir):
        # Get the _real_ lightup dir containing this script.
        self.lightup_base_dir = base_loc = os.path.dirname(os.path.realpath(__file__))
        self.project_dir = os.path.join(lightup_base_dir, "..")
        self.git = sh.git.bake(_cwd=self.project_dir)

        # Load up the config
        self._get_config()


    def _get_config(self):
        user_config_file = os.path.join(self.project_dir, ".lightup.yaml")
        self.debug("User config file: %s" % user_config_file)
        if os.path.isfile(user_config_file):
            with open(user_config_file, 'r') as config:
                user_config = yaml.load(config)
        else:
            user_config = {}

        default_config_file = os.path.join(self.lightup_base_dir, ".lightup_defaults.yaml")
        self.debug("Default config file: %s" % default_config_file)
        with open(default_config_file, 'r') as config:
            default_config = yaml.load(config)

        self.config = merge_dicts(defaults=default_config, overrides=user_config)
        logger.debug("Config: %s" % self.config)


    def status(self):
        status = self.git.status()
        logger.info(status)

    def install(self):
        # Link lightup.py to /etc/cron.hourly
        script_name = os.path.join("etc", "cron.hourly". self.config("script_name"))
        logger.info("Installing script to %s" % script_name)
        with sh.contrib.sudo:
            sh.ln("-s", os.path.abspath(__file__), script_name)


if __name__ == "__main__":
    l = Lightup()
    l.status()
