# -*- coding: utf-8 -*-


from datetime import datetime
from hashlib import sha256
import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient
import datetime
from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context

import json
from bson import json_util

__all__ = ['Exam']

class Exam:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.examanalysis
        self.exam = self.db.exam
        
    def insert_doc(self,doc):
        self.exam.insert(doc)
    
    def query_doc(self,_id):
        doc = self.exam.find_one({"_id":ObjectId(_id)})
        return doc
    
    def handle_json_serializing_issue(self,list_from_mongo):
        json_docs = []
        for doc in list_from_mongo:
            json_doc = json.dumps(doc, default=json_util.default)
            json_docs.append(json_doc)
        return json_docs
    
    def query_by_owner(self,_id):
        doc_list = self.exam.find({"owner": ObjectId(_id)})
        #doc_list = self.handle_json_serializing_issue(doc_list)
        return doc_list
