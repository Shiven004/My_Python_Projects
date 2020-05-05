# Copyright (c) 2019 Tummee. All Rights Reserved. Tummee Proprietary.

import webapp2
import logging
from google.appengine.api import taskqueue
from google.appengine.ext import ndb

from models.feed_models import TestSequences, FeedsSequences
from controllers.system import template, error as err, security as sec
from collections import defaultdict
from google.appengine.ext.ndb import Cursor




class FeedModelCheck(webapp2.RequestHandler):
        get_methods = {
                    '/admin/feed/test_create_dummy_TestSequences_records': 'test_create_dummy_TestSequences_records',                    
                    '/admin/feed/add-top-searches-daily' : 'feed_sequence_update_daily',
                    '/admin/feed/add-top-searches-alltime' : 'feed_sequence_update_alltime',
                      }

        post_methods = {                                               
                        '/admin/feed/add-top-searches-alltime' : 'feed_sequence_update_alltime',
                        '/admin/feed/add-top-searches-daily' : 'feed_sequence_update_daily'
                       }

        # Methods Definitions  
        def __init__(self, request='', response=''):
            super(FeedModelCheck, self).__init__(request, response)
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
                
        def test_create_dummy_TestSequences_records(self):
            #In this function, create 10-15 dummy records in TestSequences database for testing purposes
            logging.info("In test_create_dummy_TestSequences_records")
                        
            ## LOGIC GOES HERE ##
            key_seq_list = ["seqid_1","seqid_2","seqid_3", "seqid_4"]
            user_email_list = ["abc@gmail.com","def@gmail.com","efg@gmail.com","pqr@gmail.com"]
            user_type_list = ["teacher","intraining","therapist","teacher"]
            seq_poses_list = [["pose1","pose2","pose3","pose4"],["pose5","pose6","pose7","pose8"],["pose9","pose10","pose11","pose12"],["pose13","pose14","pose15","pose16"]]
            seq_poses_custom_list = ["pose_c1","pose_c2","pose_c3","pose_c4"]
            seq_poses_num_list = [1,2,3,4]
            seq_poses_breath_count_list = ["100","200","300","400"]
            seq_poses_breath_type_list = ["normal","high","low","normal"]
            seq_poses_duration_list = ["10 seconds","20 seconds","30 seconds","10 seconds"]
            seq_poses_renames_list = ["1","2","3","4"]
            seq_cues_list = ["cue1","cue2","cue3","cue4"]
            seq_title_list = ["seq_1","seq_2","seq_3","seq_4"]
            seq_desc_list = ["demo1","demo2","demo3","demo4"]
            seq_tags_list = [["tag1"],["tag2"],["tag3"],["tag4"]]
            seq_level_list = ["level_1","level_2","level_3","level_4"]
            seq_theme_list = ["theme1","theme2","theme3","theme4"]
            seq_focus_list = ["focus1","focus2","focus3","focus4"]
            seq_props_list = [["props1"],["props2"],["props3"],["props4"]]
            seq_props_other_list = ["props_others1","props_others2","props_others3","props_others4"]
            seq_access_list = ["public","private","public","private"]
            seq_duration_list = [150,250,360,450]
            seq_playlist_list = ["s10","s20","s30","s40"]
            seq_local_id_list = ["L1","L2","L1","L2"]
            seq_source_seq_id_list = ["0001","0002","0003","0004"]
            seq_source_seq_type_list = ["self","teacher","tummee","merged"]
            seq_yoga_type_list = ["yoga_type_a","yoga_type_a","yoga_type_a","yoga_type_b"]            
            deleted_list = [True,False,True,False]            
            
            i = 0
            for key_item in key_seq_list:
                #Use get_or_inser to fetch function to check data presence in TestSequences Model.
                test_sequence = TestSequences.get_or_insert(key_item, user_email= user_email_list[i],user_type = user_type_list[i],seq_poses=seq_poses_list[i],seq_poses_custom = seq_poses_custom_list[i],seq_poses_num = seq_poses_num_list[i],seq_poses_breath_count = seq_poses_breath_count_list[i],seq_poses_breath_type = seq_poses_breath_type_list[i],seq_poses_duration = seq_poses_duration_list[i],seq_poses_renames = seq_poses_renames_list[i],seq_cues = seq_cues_list[i],seq_title = seq_title_list[i],seq_desc = seq_desc_list[i],seq_tags = seq_tags_list[i],seq_level = seq_level_list[i],seq_theme = seq_theme_list[i],seq_focus = seq_focus_list[i],seq_props = seq_props_list[i],seq_props_other = seq_props_other_list[i],seq_access = seq_access_list[i],seq_duration = seq_duration_list[i],seq_playlist = seq_playlist_list[i],seq_local_id = seq_local_id_list[i],seq_source_seq_id = seq_source_seq_id_list[i],seq_source_seq_type = seq_source_seq_type_list[i],seq_yoga_type = seq_yoga_type_list[i],deleted = deleted_list[i])                
                #Use put() in a for loop to insert data in TestSequences Model.
                test_sequence.put()                                
                if (i < (len(key_seq_list)-1)):                    
                    i+=1                
                
            logging.info("Exiting test_create_dummy_TestSequences_records")
            return        
        
        def feed_sequence_update_alltime(self):
            
            logging.info("In feed_sequence_update_alltime")          
            urlsafe_cursor = self.request.get('cursor')
            cursor_from_url = Cursor(urlsafe=urlsafe_cursor) if urlsafe_cursor else None                                                                  
            logging.info("Cursor in start is: {}".format(cursor_from_url))                                        
            
            #Define query here
            gql_query_text = 'Select * From TestSequences' 
                
            #Execute query                        
            query_o = ndb.gql(gql_query_text)
            BATCH_SIZE = 500
            results, next_cursor, more = query_o.fetch_page(BATCH_SIZE, start_cursor=cursor_from_url)
                        
            if more:
                pass
            if next_cursor:
                pass            
                                        
            if not results:
                logging.info("feed_sequence_update_task: all done")
                return
            
            
            #Calling fn to insert data in FeedSequence            
            record_type = 'alltime'
            FeedModelCheck.add_feeds_sequences_records(self,results,record_type)
                                                                            
            cursor = query_o.fetch()
            taskqueue.add(url='/admin/feed/add-top-searches-alltime', params={'cursor': cursor})            
            logging.info("Exiting feed_sequence_update_alltime")
            return
    
        def feed_sequence_update_daily(self):
            
            logging.info("In feed_sequence_update_daily")             
            urlsafe_cursor = self.request.get('cursor')
            cursor_from_url = Cursor(urlsafe=urlsafe_cursor) if urlsafe_cursor else None                                                                  
            logging.info("cursor_from_url in start is: {}".format(cursor_from_url))
            logging.info("urlsafe_cursor in start is: {}".format(urlsafe_cursor))                                       
            
            #Define query here
            gql_query_text = 'Select * From TestSequences' 
                
            #Execute query                        
            query_o = ndb.gql(gql_query_text)
            BATCH_SIZE = 500
            results, next_cursor, more = query_o.fetch_page(BATCH_SIZE, start_cursor=cursor_from_url)
                        
            if more:
                pass
            if next_cursor:
                pass
            
            if not results:
                logging.info("feed_sequence_update_second_task: all done")
                return                     
            logging.info(" results is {}".format(results))
            
            #Calling fn to insert data in FeedSequence
            record_type = 'daily'
            FeedModelCheck.add_feeds_sequences_records(self,results,record_type)      
                                                                            
            cursor = query_o.fetch()
            taskqueue.add(url='/admin/feed/add-top-searches-daily', params={'cursor': cursor})            
            
            logging.info("Exiting feed_sequence_update_daily")
            return
        
        def add_feeds_sequences_records(self,results,rec_type):
                        
            logging.info("Entering add_feeds_sequences_records...")
            
            ## LOGIC TO RUN FOR LOOP AND PUT DATA IN FeedsSequences database ##            
            seq_yoga_list = []
            seq_id_list = []
            for record in results:
                seq_yoga_list = seq_yoga_list + list(str(record.seq_yoga_type).split())                
                seq_id_list = seq_id_list + list(str(record.key.id()).split())
            
            #yoga_type and corresponding seq_id are associated with each other as key, value pair in a dictionary
            dict_result = defaultdict(list)                                
            for k, v in zip(seq_yoga_list, seq_id_list):
                dict_result[k].append(v)            
            
            for record in results:                      
                sequence_key = record.seq_yoga_type
                record_type = rec_type                             
                feed_seq = FeedsSequences.get_or_insert(sequence_key,record_type=record_type,sequence_list=dict_result[record.seq_yoga_type])                 
                feed_seq.put()
                        
            logging.info("Exiting for add_feeds_sequences_records...")               
            return

    
app = template.webapp2.WSGIApplication([
    ('/admin/feed/test_create_dummy_TestSequences_records', FeedModelCheck),
    ('/admin/feed/add-top-searches-alltime', FeedModelCheck),
    ('/admin/feed/add-top-searches-daily', FeedModelCheck),
    ], debug=True)

