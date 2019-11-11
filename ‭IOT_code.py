
# coding: utf-8

# # Load the file 

# In[65]:


file1 = open("/dataset.txt","r")
contents = file1.readlines();
file1.close();
print(contents)


# # Clean the data : Put previous soil moisture value where none and out of range values i.e. 0 or greater than 100

# Following code takes only that data which has correct time value

# In[66]:


mylines = []
for line in contents:
    if("-05:00" in line or "-06:00" in line):
        mylines.append(line)
print(mylines)
    


# Split each line with \t

# In[67]:


myColumns = []
for line in mylines:
    myColumns.append(line.split('\t'))
print(myColumns)
    


# Wherever soil moisture value is 'None'  then it is changed to moisture values earlier on that sensor

# In[68]:


for i in range(len(myColumns)):
    for j in range(len(myColumns[i])):
        if(myColumns[i][j] == "None"):
            myColumns[i][j] = myColumns[i-1][j]
print(myColumns)


# Convert soil moisture values of all sensors into float

# In[69]:


for row in myColumns:
        row[1] = float(row[1])
        row[2] = float(row[2])
        row[3] = float(row[3])
        row[4] = float(row[4])
        row[5] = float(row[5])
        row[6] = float(row[6])
        row[7] = float(row[7])
        row[8] = float(row[8])
        row[9] = float(row[9])
print(myColumns)


# # Convert value above 100 to moisture value sensed earlier stored in previous row

# Convert value above 100 to moisture value sensed earlier stored in previous row

# In[70]:


for i in range(len(myColumns)):
    for j in range(len(myColumns[i])):
        if(j> 0 and (myColumns[i][j] > 100.0 or myColumns[i][j] == 0)):
            myColumns[i][j]=myColumns[i-1][j]
print(myColumns)


# Make training data and test data

# In[71]:


from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(myColumns, test_size=0.2, random_state=42)
print(len(train_set))
print(len(test_set))


# Make dataframe out of 'myColumns' list

# In[72]:


import pandas as pd
from pandas import DataFrame

myTrainDataFrame = DataFrame(train_set, columns = ['time','1','2','3','4','5','6','7','8','9'])
print (myTrainDataFrame)


# make different columns for labels and data

# In[77]:


trainLabels = myTrainDataFrame['5']
print(trainLabels)


# In[78]:


trainNeighbors = myTrainDataFrame[['1','2','3','4','6','7','8','9']]
print(trainNeighbors)


# Test set labels and data

# In[79]:


myTestDataFrame = DataFrame(test_set, columns = ['time','1','2','3','4','5','6','7','8','9'])
print (myTestDataFrame)


# In[80]:


testLabels = myTestDataFrame['5']
print(testLabels)


# In[81]:


testNeighbors = myTestDataFrame[['1','2','3','4','6','7','8','9']]
print(testNeighbors)


# # Apply different regression models

# In[82]:


from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(trainNeighbors, trainLabels)


# In[83]:


from sklearn.metrics import mean_squared_error

moisture_predictions = lin_reg.predict(testNeighbors)
print(moisture_predictions)
lin_mse = mean_squared_error(testLabels, moisture_predictions)
lin_rmse = np.sqrt(lin_mse)
print("root mean squared error =",lin_rmse)


# In[84]:


from sklearn.metrics import mean_absolute_error

lin_mae = mean_absolute_error(testLabels, moisture_predictions)
lin_mae

