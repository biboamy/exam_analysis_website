# -*- coding: utf8 -*-


class ClientPreProcessor:
    
    def __init__(self):
        self.chi_to_eng_table = {
            u'試題編號':u'number',
            u'試題類別':u'type',
            u'層次':u'level',
            u'自定難度':u'felt_difficulty',
            u'分年細目':u'scope',
            u'配分':u'grade',
            u'標準答案':u'correct_ans',
            u'選擇':u'selection',
            u'非選':u'non-selection',
            u'學生答題狀況':u'ans_info',
            u'試題資訊':u'prac_info'
        }
        
        self.wanted_items = [u'class',u'name',u'ge']
        
    def transform_fromat(self,data,type,id):
        print "In transform_fromat()"
        #print type, id
        result = {}
        for key,values in data.iteritems():
            #print key
            if key == type :
                #print values
                for val in values:
                    temp_dict = { val.pop(id,None): val}
                    #print temp_dict
                    result.update(temp_dict)
        #print result
        return result
    
    def drop_unwanted_column(self,data):
        print "In drop_unwanted_item()"
        #print data
        for key, values in data.iteritems():
            for unwanted_item in self.wanted_items:
                if values.has_key(unwanted_item):
                    values.pop(unwanted_item) 
        
        return data
    
    def string_to_unicode(self,data):
        print "In string_to_unicode "
        
        for key, values in data.iteritems():
            #print key
            temp = []
            temp_dict = {key:temp}
            
            for val in values:
                temp.append(val.decode('utf8'))
            
            data.update(temp_dict)
            
        return data
    
    def chinese_to_eng(self,data):
        print "In chinese_to_eng() "
        result = {}
        for key,values in data.iteritems():
            temp_dict = {key:values}
            for k, val in values.iteritems():
                if self.chi_to_eng_table.has_key(val):
                    temp = {
                        k: self.chi_to_eng_table[val]
                    }
                    temp_dict[key].update(temp)
                if self.chi_to_eng_table.has_key(k):
                    temp_dict[key].pop(k)
                    temp = {
                        self.chi_to_eng_table[k]:val
                    }
                    temp_dict[key].update(temp)
                
            result.update(temp_dict)
        """
        print "Handle Val in Dictionary"
        #print self.chi_to_eng_table.keys()
        for key, values in data.iteritems():
            temp = []
            temp_dict = {key:temp}
            
            for val in values:
                
                if val in self.chi_to_eng_table.keys():
                    temp.append(self.chi_to_eng_table[val])
                else:
                    temp.append(val)
            
            data.update(temp_dict)
        """
        return result
        
    
    def row_major_process(self,data,key_index,val_start_index,not_key):
        print "In row_major_process"
        result = {}
        for key, values in data.iteritems():
            #print key
            #print values[0]
            #print self.chi_to_eng_table[values[0]]
            
            if not_key != None:
                if key == not_key:
                    continue
            temp = {
                values[key_index]:values[val_start_index:]
            }
            result.update(temp)
        
        return result
            
    
    def dict_to_list(self,data):
        
        result = []
        for key, values in data.items():
            temp = {'_id':key}
            values.update(temp)
            #print values
            result.append(values)

        return result
    
    def sort_by_id(self,data):
        for item in data:
            temp = {'_id':int(item['_id'])}
            item.update(temp)

        result = sorted(data, key=lambda k: k['_id'])  
        print result
        return result   

    def add_key_from_list(self,data,key_name,list):
        i = 0
        for item in data:
            temp = {key_name:list[i]}
            item.update(temp)
            i = i + 1

        return data

