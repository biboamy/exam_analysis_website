# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.predicates import has_permission

from examanalysis.lib.base import BaseController

from examanalysis.model.PreProcessor.DBPreProcessor import DBPreProcessor

from examanalysis.model.mongo_interface import Exam

"""For testing"""
from examanalysis.model.PreProcessor.packet_from_client import *

import json

__all__ = ['ExamListController']

class ExamListController(BaseController):
    
    @expose(template='examanalysis.templates.exam_list')
    @expose('json')
    def index(self, user_id,**kw):
        """Handle the access page"""
        #userid = request.identity['repoze.who.userid']
        print user_id
        msg = None
        if kw.has_key('message'):
            msg = kw['message']
        message = msg
        
        """The following function call is for testing"""
        exam_list = self.access_by_owner(user_id, **kw)
        
        return dict(page='exam_list', params=kw, message=None, exam_list=exam_list)
    
    
        
    def access_by_owner(self, user_id, **kw):
        
        exam_collection = Exam()
        db_pre_processor = DBPreProcessor()
        
        exam_list = exam_collection.query_by_owner(user_id)
        
        result = []
        for exam_doc in exam_list:
            exam_doc = db_pre_processor.unicode_dict_from_DB_to_string(exam_doc)
            result.append(exam_doc)
        
        return result
        
    
        
        
    
