# Copyright (c) 2013 Tummee. All Rights Reserved.
# Tummee Proprietary.
#
# ----INTRODUCTION------------------------------------------------------------------------------ # INTRODUCTION
# Defines template engine to be used
#
# ----CHANGELIST-------------------------------------------------------------------------------- # CHANGELIST
#
# 05.29.2013: file created

import webapp2
from webapp2_extras import jinja2
import logging

class TemplateHandler(webapp2.RequestHandler):
    def __init__(self, request='', response=''):
        super(TemplateHandler, self).__init__(request, response) #previously, self.initialize(request, response)

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, **template_args):
        #logging.info('calling jinja2 render function %s %s', self, filename)
        #self.response.headers['Content-Type'] = 'text/html'
        #self.response.write(self.jinja2.render_template(filename, **template_args))
        return self.jinja2.render_template(filename, **template_args)

    def initialize_template_values(self):
        # initialize all template values
        template_values = {
        }

        return template_values

    def initialize_user_account_template_values(self):
        # initialize all template values
        template_values = {
        }
        return template_values

    def initialize_admin_template_values(self):
        # initialize all template values
        template_values = {
        }
        
        return template_values

    def initialize_features_template_values(self):
        # initialize all template values
        template_values = {
        }
        
        return template_values


    def template_render_page(self, page_to_display='/'):
        self.template_values.update({
            'msg' : self.msg,
            'user' : self.user,
        })
        return self.render_template(page_to_display+'.html', **self.template_values)

