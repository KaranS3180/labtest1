#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
lions=np.array([15,16,17,20,19,21,23,24,25,27])
elephants=np.array([50,52,54,53,55,56,57,59,60,62])
zebras=np.array([100,98,95,97,96,94,95,93,92,90])


# In[9]:


total1=np.sum(lions)
print("total population of lions ",total1)

total2=np.sum(elephants)
print("total population of elephants ",total2)

total3=np.sum(zebras)
print("total population of zebras ",total3)


# In[11]:


diff1=0
for i in range (1,len(lions)):
    diff1=diff1+(lions[i]-lions[i-1])
avg1=diff1/len(lions)
print("avg yearly growth for lions is ",avg1)

diff2=0
for i in range (1,len(elephants)):
    diff2=diff2+(elephants[i]-elephants[i-1])
avg2=diff2/len(elephants)
print("avg yearly growth for elephants is ",avg2)

diff3=0
for i in range (1,len(zebras)):
    diff3=diff3+(zebras[i]-zebras[i-1])
avg3=diff3/len(zebras)
print("avg yearly growth for zebras is ",avg3)


    


# In[12]:


for i in range (1,len(lions)):
    diff1=(lions[i]-lions[i-1])
    per1=(diff1/lions[i-1])*100
    print("percentage growth for lions in year", i+1," is ",per1,"%")


# In[13]:


for i in range (1,len(elephants)):
    diff2=(lions[i]-lions[i-1])
    per2=(diff2/elephants[i-1])*100
    print("percentage growth for elephants in year", i+1," is ",per2,"%")


# In[14]:


for i in range (1,len(zebras)):
    diff3=(lions[i]-lions[i-1])
    per3=(diff3/lions[i-1])*100
    print("percentage growth for zebras in year", i+1," is ",per3,"%")


# In[23]:


import matplotlib.pyplot as mp
import numpy as np

a=np.array(["year1","year2","year3","year4","year5","year6","year7","year8","year9","year10"])
mp.xlabel("year")
mp.ylabel("population")
mp.title("line plot")
mp.plot(a,lions)
mp.plot(a,elephants)
mp.plot(a,zebras)
mp.show()


# In[32]:


import matplotlib.pyplot as mp
import numpy as np

a=np.array(["lions"])
b=np.array(total1)
mp.xlabel("year")
mp.ylabel("population")
mp.title("bar plot after 10 years")
mp.bar(a,b)
mp.show()


# In[ ]:




