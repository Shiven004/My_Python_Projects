# Copyright (c) 2013 Tummee. All Rights Reserved.
# Tummee Proprietary.

# ----INTRODUCTION------------------------------------------------------------------------------ # INTRODUCTION
# VisibleBox security related features
# ----CHANGELIST-------------------------------------------------------------------------------- # CHANGELIST
# 02.14.2013: file created
# ----GAE MODULES------------------------------------------------------------------------------- # MODULES
# ----VISIBLEBOX MODULES------------------------------------------------------------------------ # MODULES

class SecurityHandler():
    def is_url_valid(self, url):        
        return True if url[0] != '_' else False 

    def validate_url(self, url):        
        return True if url[0] != '_' else False 

    def validate_form_input(self, url):
        pass

