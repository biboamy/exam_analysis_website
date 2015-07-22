# -*- coding: utf8 -*-


class ClientPreProcessor:
    def __init__(self):
        self.chi_to_eng_table = {
            '試題編號':'number',
            '試題類別':'type',
            '層次':'level',
            '自定難度':'felt_difficulty',
            '分年細目':'scope',
            '配分':'grade',
            '標準答案':'correct_ans',
            '選擇':'selection',
            '非選':'non-selection',
            '學生答題狀況':'ans_info',
            '試題資訊':'prac_info'
        }
        
    