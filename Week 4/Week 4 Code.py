import pandas as pd 

#creating a dataframe from a dictionary

var1 = {'people':['matt','chris','hanna','jenna'], 'numbers':[1,2,5,6]} 
#print(var1['people'][1])

df = pd.DataFrame(var1) #each section is made into a column 
#print(df)

rows = df.index
#print(rows)
   
cols = df.columns
#print(cols)
#print(df[df['people']=='chris'])

df2 = df.iloc[1:2]
#print(df2) #iloc prints rows of dataframe using indeces and does not use last index

dff = df.set_index('people')
df3 = dff.loc['chris'] #this is a variable the contians the row labeled as '1'
#print(df3) 

#working with csv files 

data_reader = pd.read_csv('/Users/matt1/Documents/Apple_banana.csv')
#print(data_reader)
#print(data_reader.iloc[:2]) #iloc prints rows of dataframe using indeces 
for index, row in data_reader.iterrows():
    #print(index)
    #print(row)