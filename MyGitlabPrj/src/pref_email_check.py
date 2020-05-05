# Copyright (c) 2019 Tummee. All Rights Reserved. Tummee Proprietary.

import webapp2
import logging
from google.appengine.api import taskqueue
from google.appengine.ext import db,ndb

from models.usermodels import UserActivity, UserProfilePrefEmails
from controllers.system import template, error as err, security as sec
from controllers.system import util_misc
        
class PrefEmailCheck(webapp2.RequestHandler):
        get_methods = {
                    '/admin/user/test_create_dummy_UserActivity_records': 'test_create_dummy_UserActivity_records',
                    '/admin/user/pref-email-update-task' : 'pref_email_update_task',
                      }

        post_methods = {
                        '/admin/user/pref-email-update-task' : 'pref_email_update_task'
                       }

    # Methods Definitions  
        def __init__(self, request='', response=''):
            super(PrefEmailCheck, self).__init__(request, response)
            self.request = request
            self.response = response
            self.GETSTR = 'get'
            self.POSTSTR = 'post'
            return 
    
        def get(self):
            logging.info('In get method')
            self.process_url(self.GETSTR)
            return

        def post(self):
            logging.info('In Post method')
            self.process_url(self.POSTSTR)
            return

        def process_url(self, source):
            #validate URL
            rcvd_url = self.request.path
            logging.info('Rcvd url = %s', rcvd_url)            
            if source == self.GETSTR:
                func_map = self.get_methods
            else:
                func_map = self.post_methods
            
            secObj = sec.SecurityHandler()
            if secObj.validate_url(rcvd_url):
                #get destination method using key-value pair
                dest_method = func_map.get(rcvd_url, None) # Correction 2
                logging.info("dest_method is {}".format(dest_method))
                if dest_method:
                    func = getattr(self, dest_method, None)
                    logging.info("func is {}".format(func))
                    if func:
                        func()
                        logging.info('Finished %s method', source)        
                        return
            #Invalid url
            else:
                pass #case handled below

            #Invalid URL
            err_obj = err.ErrorHandler()
            err_obj.handle_invalid_url(rcvd_url)
            self.error(404)
            logging.info('Finished %s method with error', source)        
            return
    
        def pref_email_update_task(self):
            
            logging.info("In pref_email_update_task")
            cursor_from_url = self.request.get('cursor')            
            logging.info("Cursor in start is: {}".format(cursor_from_url))
             
            process_date = util_misc.get_start_date_from_day_param(self)
            logging.info("=======1===========")
            gql_query_text = 'Select * From UserActivity where date_updated >= :1' #Define query conditions here            
            logging.info("=======2===========")
            #Execute query
            query_o = db.GqlQuery(gql_query_text, process_date)
            
            logging.info("=======3===========")
            if cursor_from_url:
                logging.info("=======inside if cursor from url===========")                           
                query_o.with_cursor(cursor_from_url)
                logging.info("******test shiv query_o.with_cursor(cursor_from_url) is {}".format(query_o.with_cursor(cursor_from_url)))
                BATCH_SIZE = 500
                results = query_o.fetch(BATCH_SIZE)
            else:
                logging.info("=======inside else cursor from url===========")                                
                BATCH_SIZE = 1                
                results = query_o.fetch(BATCH_SIZE)

            if not results:
                logging.info("pref_email_update_task: all done")
                return                     
            logging.info("=======4===========") 
            ## LOGIC TO RUN FOR LOOP AND PUT DATA IN UserProfilePrefEmails database ##            
            for record in results:
                #get or insert use here for existence
                if(len(str(record.email_pref)) > 1): #Still to check
                    user_mail = record.key().name()
                    email_pref_o = record.email_pref               
                    pref_emails_o = UserProfilePrefEmails.get_or_insert(email_pref_o)
                    pref_emails_o.original_email = user_mail                   
                    pref_emails_o.put()
                else:
                    continue 
                                                                            
            cursor = query_o.cursor()
            taskqueue.add(url='/admin/user/pref-email-update-task', params={'cursor': cursor})
            logging.info("Exiting pref_email_update_task")
            return
    
        def is_pref_email(self, email):
            logging.info("Entering is_pref_email_task")
            #Check if this email id exists in the PrefEmail database, if so, return the original_email
            pref_email_o = UserProfilePrefEmails.get_by_id(id)
            email = pref_email_o
            #email = User_Profile_Prefemails.get(id)                                     
            if  email:                
                return UserProfilePrefEmails.original_email
            else:
                logging.info("Email does not exist")
                return None
                
            logging.info("Exiting is_pref_email_task")       
            return

        def test_create_dummy_UserActivity_records(self):
            #In this function, create 10-15 dummy records in UserActivity database for testing purposes
            logging.info("In test_create_dummy_UserActivity_records")
                        
            ## LOGIC GOES HERE ##                             
            s1 = UserActivity.get_or_insert("user1@gmail.com", email_pref="Abc@gmail.com")
            s1.put()
            s2 = UserActivity.get_or_insert("user2@gmail.com", email_pref="Ram@gmail.com")
            s2.put()
            s3 = UserActivity.get_or_insert("user3@gmail.com", email_pref="Ice@gmail.com")
            s3.put()             
            s4 = UserActivity.get_or_insert("user4@gmail.com", email_pref="Rock@gmail.com")
            s4.put()      
            s5 = UserActivity.get_or_insert("user5@gmail.com", email_pref="Paige@gmail.com")
            s5.put()
            s6 = UserActivity.get_or_insert("user6@gmail.com", email_pref="Shyam@gmail.com")
            s6.put()            
            s7 = UserActivity.get_or_insert("user7@gmail.com", email_pref="Ajay@gmail.com")
            s7.put()                           
            s8 = UserActivity.get_or_insert("user8@gmail.com", email_pref="Suresh@gmail.com")
            s8.put()               
            s9 = UserActivity.get_or_insert("user9@gmail.com", email_pref="Kamal@gmail.com")
            s9.put()                
            s10 = UserActivity.get_or_insert("user10@gmail.com", email_pref = "Venkat@gmail.com")
            s10.put() 
            s11 = UserActivity.get_or_insert("user11@gmail.com", email_pref = "Sameer@gmail.com")
            s11.put()            
            s12 = UserActivity.get_or_insert("user12@gmail.com", email_pref = " ")
            s12.put()        
            s13 = UserActivity.get_or_insert("user13@gmail.com", email_pref = " ")
            s13.put()      
            s14 = UserActivity.get_or_insert("user14@gmail.com", email_pref = "Navjot@gmail.com")
            s14.put()
            s15 = UserActivity.get_or_insert("user15@gmail.com", email_pref = "shiv@gmail.com")
            s15.put()
            
            logging.info("Exiting test_create_dummy_UserActivity_records")
            return 

    
app = template.webapp2.WSGIApplication([
    ('/admin/user/test_create_dummy_UserActivity_records', PrefEmailCheck),
    ('/admin/user/pref-email-update-task', PrefEmailCheck),
    ], debug=True)

