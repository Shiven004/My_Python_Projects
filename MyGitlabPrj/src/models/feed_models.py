# Copyright (c) 2019 Tummee. All Rights Reserved. Tummee Proprietary.

# ----INTRODUCTION------------------------------------------------------------------------------ # INTRODUCTION
# ----CHANGELIST-------------------------------------------------------------------------------- # CHANGELIST
# ----GAE MODULES------------------------------------------------------------------------------- # MODULES
from google.appengine.ext import ndb
 
#Database to store sequences  
class TestSequences(ndb.Model):
    
    #key = unique yoga sequence id
    user_email = ndb.StringProperty()
    user_type = ndb.StringProperty() #teacher, intraining, therapist, etc.    
    seq_poses = ndb.StringProperty(repeated=True)
    seq_poses_custom = ndb.TextProperty()
    seq_poses_num = ndb.IntegerProperty(default=0)
    seq_poses_breath_count = ndb.TextProperty()
    seq_poses_breath_type = ndb.TextProperty()
    seq_poses_duration = ndb.TextProperty()
    seq_poses_renames = ndb.TextProperty()
    seq_cues = ndb.TextProperty() #cues for all the poses in the sequence
    seq_title = ndb.StringProperty()
    seq_desc = ndb.TextProperty()
    seq_tags = ndb.StringProperty(repeated=True) #tags assigned by the user to the sequence
    seq_level = ndb.StringProperty() #Beginner, Intermediate, Advanced, Beginner-Intermediate, Intermediate-Advanced
    seq_theme = ndb.StringProperty()
    seq_focus = ndb.StringProperty()
    seq_props = ndb.StringProperty(repeated=True)
    seq_props_other = ndb.TextProperty()
    seq_access = ndb.StringProperty(default='Public') #whether sequence is private or public. Empty means public.
    seq_duration = ndb.IntegerProperty() #duration of the sequence in mins
    seq_playlist = ndb.StringProperty() #duration of the sequence in mins
    seq_local_id = ndb.StringProperty() #E.g., L1, L2, etc. in user's account
    seq_source_seq_id = ndb.StringProperty() #if the sequence was a duplicate or added from a duplicate sequence, what is the unique id of the source sequence
    seq_source_seq_type = ndb.StringProperty() #'self' sequence, 'teacher' sequence, 'tummee' sequence, 'merged'
    seq_yoga_type = ndb.StringProperty() #please see list of yoga types in /library/lists-yoga-styles.html    
    #Cannot do the following as there can be a race condition where the sequene owner is updating the sequence when another user upvotes/downvotes the sequence
    #This data should be maintained in SequenceIDs DB
    #stats_usr_ref_count = ndb.IntegerProperty(default = 0) #times sequence added as reference to help us identify most popular sequences.
    #stats_usr_votes_pos = ndb.IntegerProperty(default = 0) #positive votes received by the sequence
    #stats_usr_votes_neg = ndb.IntegerProperty(default = 0) #negative votes received by the sequence    
    deleted = ndb.BooleanProperty(default=False) #tracks if sequence has been deleted

#Databse to store sequences
class FeedsSequences (ndb.Model):
    #Key: yogatype
    record_type =  ndb.StringProperty()
    sequence_list = ndb.StringProperty(repeated=True)

