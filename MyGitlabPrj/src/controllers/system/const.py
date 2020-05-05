# Copyright (c) 2020 Tummee. All Rights Reserved.
# Tummee Proprietary.

# ----GAE MODULES------------------------------------------------------------------------------- # MODULES
import os

# ----VISIBLEBOX MODULES------------------------------------------------------------------------ # MODULES

# SYSTEM VARS
DEV_ENV = os.environ['SERVER_SOFTWARE'].startswith('Dev')
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')

ADMIN_EMAIL_A = 'vineet@tummee.com'
ADMIN_EMAIL_B = 'sajal@visiblebox.com'