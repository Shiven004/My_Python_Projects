# Copyright (c) 2019 Tummee. All Rights Reserved. Tummee Proprietary.

# ----INTRODUCTION------------------------------------------------------------------------------ # INTRODUCTION
# ----CHANGELIST-------------------------------------------------------------------------------- # CHANGELIST
# ----GAE MODULES------------------------------------------------------------------------------- # MODULES
from google.appengine.ext import db, ndb
    
class UserActivity(db.Model):
    #key = user email (entry created when user signs-up and proceeds to filling out the form)
    email_pref = db.StringProperty() #preferred email address user would like to receive emails instead of the sign-up account.
    date_updated = db.DateTimeProperty(auto_now = True)
    date_created = db.DateTimeProperty(auto_now_add = True)


#Database to store preferred emails of user (used for checking whether an email should be allowed to sign up or not
class UserProfilePrefEmails(ndb.Model):
        #key = preferred email address
        original_email = ndb.StringProperty()
        date_created = ndb.DateTimeProperty(auto_now_add=True)
        date_updated = ndb.DateTimeProperty(auto_now=True)

