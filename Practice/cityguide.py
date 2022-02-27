#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


random.random()


# In[3]:


random.randint(-90, 89)


# In[4]:


random_number = random.randint(-90, 89) + random.random() 

random_number


# In[5]:


x = 1
latitudes = []
while x < 11:
    random_lat = random.randint(-90, 89) + random.random()
    latitudes.append(random_lat)
    x += 1

latitudes


# In[6]:


# Import the NumPy module.
import numpy as np


# In[7]:


np.random.uniform(-90.000, 90.000)


# In[8]:


# Import timeit.
import timeit


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[10]:


lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)
lat_lngs


# In[11]:


coordinates = list(lat_lngs)


# In[1]:


import citipy


# In[12]:


print(citipy.nearest_city(coordinate[0], coordinate[1]).city_name,
          citipy.nearest_city(coordinate[0], coordinate[1]).country_code)


# In[13]:


# Create a list for holding the cities.
cities = []
# Identify the nearest city for each latitude and longitude combination.
for coordinate in coordinates:
    city = citipy.nearest_city(coordinate[0], coordinate[1]).city_name

    # If the city is unique, then we will add it to the cities list.
    if city not in cities:
        cities.append(city)
# Print the city count to confirm sufficient count.
len(cities)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




