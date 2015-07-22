# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash, redirect
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.predicates import has_permission

from examanalysis.lib.base import BaseController

from examanalysis.model.PreProcessor.ClientPreProcessor import ClientPreProcessor
from examanalysis.model.PreProcessor.DBPreProcessor import DBPreProcessor
from examanalysis.model.mongo_interface import Exam

"""For testing"""
from examanalysis.model.PreProcessor.packet_from_client import *

import json

__all__ = ['UploadController']

class UploadController(BaseController):
    
    @expose(template='examanalysis.templates.upload')
    def index(self, **kw):
        """Handle the upload page"""
        
        msg = None
        if kw.has_key('message'):
            msg = kw['message']
        message = msg
        
        return dict(page='upload', params=kw, message=msg)
    
    @expose('examanalysis.templates.upload')
    @expose('json')
    def upload_excel(self,**kw):
        global exam_info
        
        """Decode the json string"""
        excel_info = json.loads(kw['excel_info'])
        
        """Preprocess the data from client"""
        client_pre_processor = ClientPreProcessor()
        
        
        """"Transform the format"""
        raw_ans_info = client_pre_processor.transform_fromat(excel_info,u'學生答題狀況',u'學號')
        raw_prac_info = client_pre_processor.transform_fromat(excel_info,u'試題資訊',u'試題編號')
        
        #print raw_ans_info
        #print raw_prac_info['1']
        
        """Delete unwanted column data"""
        raw_ans_info = client_pre_processor.drop_unwanted_column(raw_ans_info)
        #print raw_ans_info['1010102']
        
        
        """ Transform key from Chinese to Eng"""
        ans_info = client_pre_processor.chinese_to_eng(raw_ans_info)
        prac_info = client_pre_processor.chinese_to_eng(raw_prac_info)
        #print raw_ans_info['1010102']
        #print raw_prac_info['1']
        
        """ Transform meaning data to the format for DB """
        db_pre_processor = DBPreProcessor()
        exam_doc = db_pre_processor.init_exam_doc()
        #print "Init Doc:\n", exam_doc
        exam_doc = db_pre_processor.update_exam_mata_data(exam_doc,exam_info)
        #print "With Metadata:\n",exam_doc
        exam_doc = db_pre_processor.update_exam_ans_data(exam_doc,ans_info)
        #print "With Ans:\n",exam_doc['stu_ans']['1010102']
        exam_doc = db_pre_processor.update_exam_prac_data(exam_doc,prac_info)
        #print "With Prac:\n",exam_doc['practices']['3']
        
        """Store in DB"""
        exam_collection = Exam()
        exam_collection.insert_doc(exam_doc)
        
        redirect('/upload',params=dict(page='upload',message="Upload Success!"))
        
