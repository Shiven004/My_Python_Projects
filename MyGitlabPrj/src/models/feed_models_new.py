# Copyright (c) 2019 Tummee. All Rights Reserved. Tummee Proprietary.

# ----INTRODUCTION------------------------------------------------------------------------------ # INTRODUCTION
# ----CHANGELIST-------------------------------------------------------------------------------- # CHANGELIST
# ----GAE MODULES------------------------------------------------------------------------------- # MODULES
from google.appengine.ext import db,ndb
 
#Database to store sequences  
class TestSequences(db.Model):
    
    #key = unique yoga sequence id
    user_email = db.StringProperty()
    user_type = db.StringProperty() #teacher, intraining, therapist, etc.    
    seq_poses = db.StringListProperty()
    seq_poses_custom = db.TextProperty()
    seq_poses_num = db.IntegerProperty(default=0)
    seq_poses_breath_count = db.TextProperty()
    seq_poses_breath_type = db.TextProperty()
    seq_poses_duration = db.TextProperty()
    seq_poses_renames = db.TextProperty()
    seq_cues = db.TextProperty() #cues for all the poses in the sequence
    seq_title = db.StringProperty()
    seq_desc = db.TextProperty()
    seq_tags = db.StringListProperty() #tags assigned by the user to the sequence
    seq_level = db.StringProperty() #Beginner, Intermediate, Advanced, Beginner-Intermediate, Intermediate-Advanced
    seq_theme = db.StringProperty()
    seq_focus = db.StringProperty()
    seq_props = db.StringListProperty()
    seq_props_other = db.TextProperty()
    seq_access = db.StringProperty(default='Public') #whether sequence is private or public. Empty means public.
    seq_duration = db.IntegerProperty() #duration of the sequence in mins
    seq_playlist = db.StringProperty() #duration of the sequence in mins
    seq_local_id = db.StringProperty() #E.g., L1, L2, etc. in user's account
    seq_source_seq_id = db.StringProperty() #if the sequence was a duplicate or added from a duplicate sequence, what is the unique id of the source sequence
    seq_source_seq_type = db.StringProperty() #'self' sequence, 'teacher' sequence, 'tummee' sequence, 'merged'
    seq_yoga_type = db.StringProperty() #please see list of yoga types in /library/lists-yoga-styles.html    
    #Cannot do the following as there can be a race condition where the sequene owner is updating the sequence when another user upvotes/downvotes the sequence
    #This data should be maintained in SequenceIDs DB
    #stats_usr_ref_count = db.IntegerProperty(default = 0) #times sequence added as reference to help us identify most popular sequences.
    #stats_usr_votes_pos = db.IntegerProperty(default = 0) #positive votes received by the sequence
    #stats_usr_votes_neg = db.IntegerProperty(default = 0) #negative votes received by the sequence    
    deleted = db.BooleanProperty(default=False) #tracks if sequence has been deleted

#Databse to store sequences
class FeedsSequences (ndb.Model):
    #Key: yogatype
    record_type =  ndb.StringProperty()
    sequence_list = ndb.StringProperty()

