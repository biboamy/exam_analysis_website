# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash, redirect
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.predicates import has_permission

from examanalysis.lib.base import BaseController

from examanalysis.model.PreProcessor.ClientPreProcessor import ClientPreProcessor
from examanalysis.model.PreProcessor.DBPreProcessor import DBPreProcessor
from examanalysis.model.PreProcessor.MetricPreProcessor import MetricPreProcessor

from examanalysis.model.mongo_interface import Exam

"""For testing"""
from examanalysis.model.PreProcessor.packet_from_client import *

import json

__all__ = ['AccessController']

class AccessController(BaseController):
    
    @expose(template='examanalysis.templates.access')
    @expose('json')
    def index(self, **kw):
        """Handle the access page"""
        
        msg = None
        if kw.has_key('message'):
            msg = kw['message']
        message = msg
        
        """The following function call is for testing"""
        msg = self.access("55681f078153b6275478e83e", **kw)
        
        return dict(page='access', params=kw, message=msg)
    
    
        
    def access(self, exam_id, **kw):
        
        exam_collection = Exam()
        metric_preprocessor = MetricPreProcessor()
        db_pre_processor = DBPreProcessor()
        
        exam_doc = exam_collection.query_doc(exam_id)
        #print exam_data
        
        exam_dict = db_pre_processor.unicode_dict_from_DB_to_string(exam_doc)
        
        packet_to_metric = metric_preprocessor.produce_packet(exam_dict)
        
        #for key, val in packet_to_metric.iteritems():
            #print '\n{} : {}\n'.format(key,val)
        
        return packet_to_metric
        
    
        
        
    
