#!/usr/bin/env python
import sh

# Link lightup.pt to /etc/cron.hourly
sh.ln("-s", "lightup.py", "/etc/cron.hourly")
