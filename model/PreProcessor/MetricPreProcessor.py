# -*- coding: utf8 -*-
import datetime
import time
from bson.objectid import ObjectId


class MetricPreProcessor:
    def __init__(self):
        
        self.packet = {
            'type'              :[],
            'grade'             :[],
            'scope'             :[],
            'felt_difficulty'   :[],
            'level'             :[],
            'correct_ans'       :[],
            'stu_num_order'     :[],
            'stu_ans'           :[]
        }
        
    
    
    def produce_packet(self,dict):
        #print dict['practices']
        
        self.packet['stu_num_order'] = dict['stu_ans'].keys()
        self.packet['stu_ans'] = dict['stu_ans'].values()
        
        cur_num = 1
        list_len = len(dict['practices'].keys())
        
        while (cur_num <= list_len):
            #print cur_num
            #print dict['practices'][str(cur_num)]
            cur_prac = dict['practices'][str(cur_num)]
            
            keys = self.packet.keys()
            
            for key in keys:
                if key != 'stu_num_order' and key != 'stu_ans' :
                    self.packet[key].append(cur_prac[key])
            
            cur_num = cur_num + 1
        
        #print self.packet['stu_ans']
        #print self.packet
        return self.packet

    
    
   