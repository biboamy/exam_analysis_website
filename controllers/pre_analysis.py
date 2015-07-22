# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash, redirect
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.predicates import has_permission

from examanalysis.lib.base import BaseController

from examanalysis.model.PreProcessor.ClientPreProcessor import ClientPreProcessor
from examanalysis.model.PreProcessor.DBPreProcessor import DBPreProcessor
from examanalysis.model.PreProcessor.MetricPreProcessor import MetricPreProcessor
from examanalysis.model.metric import *

from examanalysis.model.mongo_interface import Exam

"""For testing"""
from examanalysis.model.PreProcessor.packet_to_client import *

import json

__all__ = ['PreAnalysisController']

class PreAnalysisController(BaseController):
    
    @expose(template='examanalysis.templates.pre_analysis')
    @expose('json')
    def index(self, **kw):
        """Handle the before page"""
        
        msg = None
        if kw.has_key('message'):
            msg = kw['message']
        message = msg
        
        """The following function call is for testing"""
        exam = self.access("55681f078153b6275478e83e", **kw)
        
        return dict(page='pre_analysis', exam_statics=exam['exam_statics'], exam_doc=exam['exam_doc'], params=kw, message=msg)
    
    def access_fake_data(self, exam_id, **kw):
        
        global packet_to_client

        exam_collection = Exam()
        metric_preprocessor = MetricPreProcessor()
        db_pre_processor = DBPreProcessor()
        
        exam_doc = exam_collection.query_doc(exam_id)
        #print exam_data
        
        exam_doc = db_pre_processor.unicode_dict_from_DB_to_string(exam_doc)

        exam = {
            'exam_doc':exam_doc,
            'exam_statics':packet_to_client
        }

        return exam
    
        
    def access(self, exam_id, **kw):
        
        exam_collection = Exam()
        metric_preprocessor = MetricPreProcessor()
        client_preprocessor = ClientPreProcessor()
        db_pre_processor = DBPreProcessor()
        
        exam_doc = exam_collection.query_doc(exam_id)
        #print exam_data
        
        exam_dict = db_pre_processor.unicode_dict_from_DB_to_string(exam_doc)
        
        packet_to_metric = metric_preprocessor.produce_packet(exam_dict)
        
        """ Calculate the statistics information """
        statistics_info = all(packet_to_metric)
        
        """ Prepare information that will send to client """
        exam_doc['practices'] = client_preprocessor.dict_to_list(exam_doc['practices'])
        exam_doc['practices'] = client_preprocessor.sort_by_id(exam_doc['practices'])

        exam = {
            'exam_doc':exam_doc,
            'exam_statics':statistics_info
        }
        
        return exam
        
    
        
        
    
