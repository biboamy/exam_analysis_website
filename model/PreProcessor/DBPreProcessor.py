# -*- coding: utf8 -*-
import datetime
import time
from bson.objectid import ObjectId


class DBPreProcessor:
    def __init__(self):
        
        pass
        
    def init_exam_doc(self):
        exam_doc = {
            'owner'        :ObjectId("554466e38153b612a4a2dad3"),
            'description'   :None,
            'exam_type'     :None,
            'exam_date'     :datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
            'scopes'        :[],
            'practices'     :{},
            'stu_ans'       :{}
        }
        return exam_doc
    
    def init_prac_doc(self):
        prac_doc = {
            'content':None,
            'type':None,
            'grade':None,
            'correct_ans':None,
            'scope':None,
            'felt_difficulty':None,
            'real_difficult':None,
            'level':None
        }
        return prac_doc
    
    def update_exam_mata_data(self,exam_doc,exam_info):
        
        for key, value in exam_info.iteritems():
            #print key, value
            exam_doc[key] = value
        
        return exam_doc
    
    def update_exam_prac_data(self,exam_doc,prac_info):
        
        """Process the practice info one by one"""
        """
        Data Format:
        exam_doc['practices'] = {
            '1':{
                'content':None,
                'type':None,
                'grade':None,
                'scope':None,
                'correct_ans':None,
                'felt_difficulty':None,
                'real_difficult':None,
                'level':None
            }
        }
        """
        
        exam_doc['practices'].update(prac_info)
        #print exam_doc['practices']
        
        
        return exam_doc
        
    def update_exam_ans_data(self,exam_doc,ans_info):
        exam_doc['stu_ans'].update(ans_info)
        return exam_doc
    
    
    def list_to_dict(self,key,list):
        dict = {
            list[key]:list[key:]
        }
        return dict
        
        
    def unicode_dict_from_DB_to_string(self, dict):
        #print dict
        result ={}
        for key, val in dict.iteritems():
            #print key, val
            if type(val) is type({}):
                #print "Dict Content :",val
                temp_dict= {
                    str(key) : self.unicode_dict_from_DB_to_string(val)
                }
                result.update(temp_dict)
            elif type(val) is list:
                #print "List Content ", val
                temp_dict = {
                    str(key): [v.encode('UTF8') for v in val]
                }
                #print temp_dict[str(key)]
                result.update(temp_dict)
            else:
                #print "Other Type :",val
                temp_dict = {
                    str(key):str(val)
                }
                result.update(temp_dict)
            
            
        #print "\nResult :\n",result
        
        return result