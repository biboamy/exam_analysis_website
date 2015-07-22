
packet = {
    'TestPaper':{
        '_id':ObjectId("554466e38153b612a4a2dad4"),
        'author_id':ObjectId("551266e38123b612a4a2dad4"),
        'description':'This is a testing exmple.',
        'type':'midterm',
        'subject':'math',
        'exam_date':'2015-05-13',
        'year_specs':['1-n-01','1-n-02','1-n-03','1-n-04','1-n-05','1-n-06','1-n-07'],
        'practices':[
            {
                '_id':ObjectId("554466e38153b612a4a2dad5"),
                'year_specs':'1-n-01',
                'answer_by':[
                    {
                        'account':'E1234'
                        'score':None,
                        'answer':'true'
                    },
                    {
                        'account':'E1233'
                        'score':None,
                        'answer':'true'
                    },
                    {
                        'account':'E1222'
                        'score':None,
                        'answer':'false'
                    },
                    {
                        'account':'E1111'
                        'score':None,
                        'answer':'true'
                    },
                    {
                        'account':'E1232'
                        'score':None,
                        'answer':'true'
                    }
                ],
                'type':'true or false',
                'point':3,
                'correct_answer':'true',
                'self_difficult':1,
                'ability_lv':1
            }
            {
                '_id':ObjectId("554462e33153b612a4a2dad5"),
                'year_specs':'1-n-03',
                'answer_by':[
                    {
                        'account':'E1234'
                        'score':None,
                        'answer':'A'
                    },
                    {
                        'account':'E1233'
                        'score':None,
                        'answer':'C'
                    },
                    {
                        'account':'E1222'
                        'score':None,
                        'answer':'B'
                    },
                    {
                        'account':'E1111'
                        'score':None,
                        'answer':'A'
                    },
                    {
                        'account':'E1232'
                        'score':None,
                        'answer':'A'
                    }
                ],
                'type':'mutiple choice',
                'point':3,
                'correct_answer':'A',
                'self_difficult':2,
                'ability_lv':3
            },
            {
                '_id':ObjectId("554462e33153b6s2b4a2dad5"),
                'year_specs':'1-n-03',
                'answer_by':[
                    {
                        'account':'E1234'
                        'score':10,
                        'answer':None
                    },
                    {
                        'account':'E1233'
                        'score':8,
                        'answer':None
                    },
                    {
                        'account':'E1222'
                        'score':10,
                        'answer':None
                    },
                    {
                        'account':'E1111'
                        'score':0,
                        'answer':None
                    },
                    {
                        'account':'E1232'
                        'score':0,
                        'answer':None
                    }
                ],
                'type':'other',
                'point':10,
                'correct_answer':'Testing',
                'self_difficult':3,
                'ability_lv':4
            }
        ]
        
    }
    
}