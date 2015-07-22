# -*- coding: utf8 -*-
from packet_from_client import *
from ClientPreProcessor import *
from DBPreProcessor import *

if __name__ == '__main__':
    
    client_pre_processor = ClientPreProcessor()
    
    raw_prac_info = client_pre_processor.chinese_to_eng(raw_prac_info)
    raw_ans_info = client_pre_processor.chinese_to_eng(raw_ans_info)
    #print raw_prac_info
    #print raw_ans_info
    
    prac_info = client_pre_processor.row_major_process(raw_prac_info,0,1,None)
    ans_info = client_pre_processor.row_major_process(raw_ans_info,3,4,"1")
        
    exam_info = {
        'author':'peggy',
        'description':'This is a testing sample!',
        'type':'midterm',
        'scopes':['9-d-01','9-d-02','9-d-03','9-d-04','9-d-05','9-s-13','9-s-14','9-s-15','9-s-16']
    }
    #print "Exam Info:\n",exam_info
    #print "Practice Info:\n",prac_info
    #print "Ans Info:\n",ans_info
    
    db_pre_processor = DBPreProcessor()
    exam_doc = db_pre_processor.init_exam_doc()
    #print "Init Doc:\n", exam_doc
    exam_doc = db_pre_processor.update_exam_mata_data(exam_doc,exam_info)
    #print "With Metadata:\n",exam_doc
    exam_doc = db_pre_processor.update_exam_ans_data(exam_doc,ans_info)
    #print "With Ans:\n",exam_doc
    exam_doc = db_pre_processor.update_exam_prac_data(exam_doc,prac_info)
    print "With Prac:\n",exam_doc['practices']['3']