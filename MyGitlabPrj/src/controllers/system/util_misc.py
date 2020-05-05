from controllers.system import const
import logging 

def get_target_module(cls):
    ''' Target module for taskqueue
        Needed, bcos, on different environments, we have different targets
    '''
    domain_url = cls.request.host_url
    if 'sgtummee' in domain_url or 'sgadmin' in domain_url:
        target_module = 'v1.sgadmin'
    else:
        target_module = 'admin'
    return target_module

def send_gmail_to_sg(esubject, ebody='   '):
        from google.appengine.api import mail
       
        message = mail.EmailMessage(sender="Tummee.com <vineet@tummee.com>")
        message.to = 'sajal@visiblebox.com'
        message.html = ebody
        message.body = ebody
        message.subject = esubject
        message.send()
        return

def inform_admin_of_error(esubject, ebody='', cc='', to=''):
        from google.appengine.api import mail
        logging.error(esubject + ' | ' + ebody)
       
        message = mail.EmailMessage(sender="Tummee.com <vineet@tummee.com>")
        if to:
            message.to = 'vineet@tummee.com'
        else:
            message.to = 'vineet@visiblebox.com;sajal@visiblebox.com'   
        if cc:
            message.cc = cc
        if ebody:
            message.html = ebody
        message.body = ebody
        message.subject = esubject
        message.send()
        return
    
def get_start_date_from_day_param(cls):
    '''***** Date from where to start based on parameter provided in the url******'''
    from datetime import datetime, timedelta

    process_day = cls.request.get('process_day')
    p_days = 1
    if not process_day: #Processing for all updates SINCE yesterday
        p_days = 1
    else:
        try:
            p_days = int(process_day)
        except:
            p_days = 1
            pass
    process_date = datetime.now() - timedelta(days=p_days)
    process_date = datetime(process_date.year, process_date.month, process_date.day, 0, 0,0) #strip hour etc from datetime variable for query
    return process_date    
    