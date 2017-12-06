#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:14:32 2017

@author: martin
"""

import pandas as pd

filename = 'acacia.csv'

df = pd.read_csv(filename, sep=';')

varname = filename.split('.')[0]

# Separates text with blank line, or awaits key click
def sep():
    print()
    #input()
    
    #s = '- ' * 10
    #print('%s' % s)

def dt_analysis(df):
    dt = {c:'' for c in df.columns}
    
    print("\t###### DATA ANALYSIS ######")
    
    # Display 5 initial rows
    def overview(df):
        print('# Dataset overview\n')
        print(df.head())
        print('(...)')
    
    # Display number of rows and columns
    def shape(df, info):
        sep()
        print('# Dimensions%s\n' % info)
        nr_rows     = df.shape[0]
        nr_columns  = df.shape[1]
        print('Rows: %d, Columns: %d' %
              (nr_rows, nr_columns))
    
    # Count and remove rows with null values
    def null_values(df):
        sep()
        print('# Empty values\n')
        null_vals = [column for column in df.columns if df[column].isnull().values.any()]
        if len(null_vals) > 0:
            print('Null values found in: \n%s' % ('\n'.join(null_vals)))
            print('\nRemoving rows with empty values (for analysis, don\'t worry)...')
            
            # Remove rows with null values
            df = df.dropna(how='any')
            
            # Run shape to recheck dimensions
            shape(df, ' (updated)')
            return df # Don't forget to return dataframe if you have made changes to it
        else:
            print('No null values found.\n')
            return df
    
    def data_types(df):
        sep()
        print('# Data types\n')
        for column in df.columns:
            print(column, '\t%s' % df[column].dtypes)
#        print(df.dtypes)
    
    def uniques(df):
        sep()
        uniq = {c:0 for c in df.columns}
        #print('# Number of unique values in columns\n')
        for column in df.columns:
            x = [v for v in df[column]]
            #print(column, '\t%d' % len(set(x)))
            uniq[column] = len(set(x))
        return uniq

    def suggested_type(df, cid):
        sep()
        print('# Suggested type\n')
        
        # Check if we've been here before
        #if all(item == '' for item in dt.values()):
            
#        if(column == df.columns[cid]):
                
        for column in df.columns:
                
            if df[column].dtypes == 'object':
                x = [v for v in df[column]]
                dt[column] = 'factor'
                print(column, '\tFactor w/ %d levels' % len(set(x)))
            
            elif df[column].dtypes == 'float64':
                dt[column] = 'numeric'
                print(column, '\tNumeric')

          
            elif df[column].dtypes == 'int64':
                x = [v for v in df[column]]
                unique = set(x)
                su = (sorted(unique))
                sequential = {i for i in range(su[0],su[0]+len(su))}
                
                if unique == sequential:
                    dt[column] = 'factor'
                    print(column, '\tFactor w/ %d levels' % len(set(x)))
                    
                else:
                    dt[column] = 'numeric'
                    print(column, '\tNumeric')
            
        #print(dt)            
        ui = input('\nAre the suggested datatypes correct? (yes / no): ')
        print()
        def selection(df):
            global dt
            for i, column in enumerate(df.columns):
                print(i+1, '\t%s' % column)
        
        if ui in ['no', 'No', 'NO', 'n', 'N']:
            selection(df)
            i = int(input('Change datatype (select a number): ')) - 1
            print()
            
            
            if i > 0 and i <= len(df.columns):
                if dt[df.columns[i]] == 'numeric':
                    dt[df.columns[i]] = 'factor'
                    print('%s set to factor' % df.columns[i])
                    
                elif dt[df.columns[i]] == 'factor':
                    dt[df.columns[i]] = 'numeric'
                    print('%s set to numeric' % df.columns[i])
            suggested_type(df, i)
        
            
    def tree(df):
        # Factor + Factor + Numeric
        # Find highest level factor
        # For each group in hlf, cbind 
        dtypes = ([x for x in dt.values()])
        #print('factor', dtypes.count('factor'))
        #print('numeric', dtypes.count('numeric'))
        #print(uniques(df))
        
        # Check dimensions
        
        if len(dtypes) == 1:
            None
            
        elif len(dtypes) == 2:
            
            ## Check datatypes
            
            # Are both columns factors?
            if all(value == 'factor' for value in dtypes):
                
                # Are both columns same level factors?
                uniq = [value for value in uniques(df).values()]
                
                if uniq[0] == uniq[1]:
                    
                    # Pearson chi-square test
                
                    print()                    
                    print('counts <- table(%s$%s, %s$%s)' %
                         (varname, df.columns[0], varname, df.columns[1]))                    
                    print('chisq.test(counts)')    
                    print('fisher.test(counts)')                    
                    print('library(DescTools)')
                    print('GTest(counts)')
        
        elif len(dtypes) == 3:
            
            # Two factor, one numeric
            if dtypes.count('factor') == 2 and dtypes.count('numeric') == 1:
                
                # Find numeric column
                num = [k for k,v in dt.items() if v == 'numeric'][0]
               # print(num)
                
                #print( df[num] )
                iters = [iter(df[num])] * 2
                z = zip(*iters)
                
                
                
                #cbind = [(start, stop) for start, stop in z]
                #print(cbind)
               # for start, stop in z:
               #     print(start, stop)
                
               # for i in z:
               #     print(i)
                
                #for item in df[num]:
                 #   print(item)
                
                
                    
                
               # print('%s.test <- cbind(%s' % (varname, (x for x in cbind)))
                
                
                
      

    
    overview(df)
    shape(df,'')
    df = null_values(df)
    data_types(df)
    uniq = uniques(df)
    print('# Number of unique values in columns')
    for k,v in uniq.items():
        print(k, v)
    suggested_type(df,0)
    #tree(df)
    return(df)

df = dt_analysis(df)
