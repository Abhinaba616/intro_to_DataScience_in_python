
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 

import pandas as pd
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()
def answer_one():
    oli_df= df.copy()
    col_to_keep = ['Gold']
    oli_df = oli_df[col_to_keep]
    maxi = oli_df.idxmax(axis = 0)
    return maxi['Gold']
answer_one()

import pandas as pd
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()
def answer_two():
    columns_to = ['Gold','Gold.1']
    ol1_df = df.copy()
    ol1_df = ol1_df[columns_to]
    maxi = ol1_df.idxmax(axis = 0)
    if maxi['Gold'] > maxi['Gold.1']:
        return maxi['Gold']
    else:
        return maxi['Gold.1']
    
    
answer_two()

import pandas as pd
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()
def answer_three():
    ol2_df = df.copy()
    ol2_df = ol2_df[(ol2_df['Gold'] > 0) & ol2_df['Gold.1'] > 0]
    cols_to_keep =['Gold','Gold.1','Gold.2']
    ol2_df = ol2_df[cols_to_keep]
    ol2_df['relative'] = ((ol2_df['Gold'] - ol2_df['Gold.1'])/ol2_df['Gold.2'])
    ans = ol2_df.idxmax(axis=0)
    
    return ans['relative']
answer_three()

import pandas as pd
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()
def answer_four():
    ol3_df =df.copy()
    col_to_keep =['Gold.2','Silver.2','Bronze.2']
    ol3_df = ol3_df[col_to_keep]
    ol3_df['Points'] = (ol3_df['Gold.2'] *3) + (ol3_df['Silver.2']*2) +(ol3_df['Bronze.2']*1)
    return   ol3_df['Points']
answer_four()

census_df = pd.read_csv('census.csv')
census_df.head()

census_df = pd.read_csv('census.csv')
census_df.head()
def answer_five():
    c_df = census_df.copy()
    filtered_df = c_df[c_df['SUMLEV']==50]
    filtered_df = filtered_df.set_index('STNAME')
    col_to_keep = ['CTYNAME']
    filtered_df = filtered_df[col_to_keep]
    filtered_df['count'] = 0



    for st in filtered_df.index:
        stcount = filtered_df.loc[st]
        d = len(stcount)
        filtered_df['count'].loc[st] = d 
    column = filtered_df['count']
    column = column.sort_values()
    val = column.index[-1]
    
    return val
answer_five()

import pandas as pd
census_df = pd.read_csv('census.csv')
def answer_six():
    fulldf3 = pd.DataFrame()
    for i in census_df.STNAME.unique():
        top3=census_df[(census_df.STNAME==i) & (census_df.SUMLEV==50)].groupby(['STNAME','CTYNAME'])['CENSUS2010POP'].sum().nlargest(3)
        dftop3=pd.DataFrame(top3)
        fulldf3=fulldf3.append(dftop3)

    fulldf3['CENSUS2010POP'].sum(level=0).nlargest(3)
    return fulldf3['CENSUS2010POP'].sum(level=0).nlargest(3).index.tolist()
answer_six()

import pandas as pd
import numpy as np    
def answer_seven():
    pop = pd.read_csv('census.csv',usecols=['SUMLEV','CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015'])
    pop = pop[pop.SUMLEV ==50]
    popcols= ['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
    cols = ['CTYNAME'] + popcols
    pop = pop[cols]
    pop = pop.set_index('CTYNAME')
    pop['low'] = pop.loc[:,popcols].min(axis=1)
    pop['high'] = pop.loc[:,popcols].max(axis=1)

    pop['diff'] = pop['high'] - pop['low']

    pop = pop['diff'].sort_values(ascending = False)
    
    return pop.index[0]
answer_seven()

import pandas as pd
def answer_eight():
    popdf = pd.read_csv('census.csv')
    popdf =popdf[(popdf.SUMLEV==50)  & ((popdf['REGION']==1) | (popdf['REGION']==2)) & (popdf.CTYNAME.str.startswith("Washington")) & (popdf.POPESTIMATE2015 > popdf.POPESTIMATE2014)]
    cols = ['STNAME', 'CTYNAME'] 
    popdf = popdf[cols] 
                   
    return popdf
answer_eight()




