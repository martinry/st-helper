#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:42:18 2017

@author: martin
"""

import pandas as pd
        
class column(object):
    
    def __init__(self, name, data, dtype, level = None):
        self.name = name
        self.data = data
        self.dtype = dtype
        self.level = level
        
    def get_name(self):
        return self.name
    
    def get_data(self):
        return self.data
    
    def get_dtype(self):
        return self.dtype
    
    def get_level(self):
        return self.level
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_dtype(self, new_dtype):
        self.dtype = new_dtype
        
    def set_level(self, new_level):
        self.level = new_level   
    
    def suggest_dtype(self):
        if self.dtype == 'float64':
            self.set_dtype('Numeric')
        
        elif self.dtype == 'int64':
            unique = sorted(set(self.data))
            sequential = [i for i in range(unique[0],unique[0]+len(unique))]
            
            if unique == sequential:
                self.set_dtype('Factor')
                self.set_level(len(unique))
            else:
                self.set_dtype('Numeric')
        
        elif self.dtype == 'object':
            self.set_dtype('Factor')
            self.set_level(len(set(self.data)))             
                
    def switch_dtype(self):
        if self.get_dtype() == 'Factor':
            self.set_dtype('Numeric')
            self.set_level(None)
        else:
            self.set_dtype('Factor')
            self.set_level(len(set(self.data)))
    
    
    
if __name__ == '__main__':
    filename = 'tiger.csv'
    df = pd.read_csv(filename, sep = ';')
    
    cols = []
    
    for c in df.columns:
        tmp = column(c,df[c], df[c].dtypes)
        cols.append(tmp)
    
    def check_dtype():
        print('\tName\tType\tLevel')
        for i,c in enumerate(cols):
            c.suggest_dtype()
            print('%d.\t%s\t%s\t%s' % (i+1, c.get_name(), c.get_dtype(), c.get_level()))

        feedback = input('Are the datatypes correct? y/n: ')

        if feedback in ['no', 'No', 'NO', 'n', 'N']:
            feedback = input('Which column\'s datatype should be changed? (select number): ')
            cols[int(feedback) - 1].switch_dtype()
            print()
            check_dtype()
                
    check_dtype()
    
    
    
    

    
        
