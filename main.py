#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

filename = 'acacia.csv'

# Read csv as dataframe
df = pd.read_csv(filename, sep=';')

# Variable name for statistical tests
varname = filename.split('.')[0]

# Separates text with blank line, or awaits key click
def sep():
    print()
    #input()

def dt_analysis(df):
    # Initialize dictionary with column names
    # This dict will hold the datatype for each column
    dt = {c:'' for c in df.columns}
    
    # Display 5 initial rows
    def overview(df):
        return df.head()

    # Display number of rows and columns
    def dimensions(df):
        sep()
        nr_rows     = df.shape[0]
        nr_columns  = df.shape[1]
        return (nr_rows, nr_columns)

    # Count and remove rows with null values
    def null_values(df):
        # Columns where empty values are present
        null_vals = [column for column in df.columns if df[column].isnull().values.any()]
        
        # If any column with empty values exists
        if len(null_vals) > 0:
            print('Null values found in: \n%s' % ('\n'.join(null_vals)))
            print('\nRemoving rows with empty values...')
            
            # Remove rows with null values
            df = df.dropna(how='any')
            
            # Recheck dimensions
            print( dimensions(df), '(updated)')
            
            return df # Return updated dataframe
            
        else:
            print('No null values found.\n')
            return df # Return unchanged dataframe
    
    # Display pandas interpretation of datatypes (int64, float64, object etc.)
    def data_types(df):
        for column in df.columns:
            print(column, '\t%s' % df[column].dtypes)
    
    # Number of unique values in each column (null-values exluded)
    def uniques(df):
        # Initialize dictionary with column names
        # all values set to 0
        uniq = {c:0 for c in df.columns}
        
        # Iterate df by column
        for column in df.columns:
            # Add all column values into a list
            x = [v for v in df[column]]
            
            # set = the unique values in the column
            # len = the number of unique values in the column
            # Update dict: key = column name, value = nr uniques
            uniq[column] = len(set(x))
        return uniq

    # This is where we suggest the datatype for each column
    # for the user to specify in R
    def suggested_type(df, cid):
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
                
                
    # 1.
    print('#1. Dataset overview\n')
    print( overview(df) )
    print('(...)')
    
    # 2.
    print('\n#2. Dimensions')
    shape = dimensions(df)
    print('Rows: %d, Columns: %d' % (shape[0], shape[1]))
    
    # 3.
    print('\n#3. Empty values\n')
    df = null_values(df)
    
    # 4.
    print('\n#4. Data types\n')
    data_types(df)
    uniq = uniques(df)
    
    # 5.
    print('\n#5. Number of unique values in columns\n')
    for k,v in uniq.items():
        print(k, v)
    
    # 6. in progress
    print('\# Suggested type\n')
    suggested_type(df,0)
    
    # 7. in progress
    
    #tree(df)
    return(df)

df = dt_analysis(df)
