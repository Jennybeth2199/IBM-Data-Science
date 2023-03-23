#!/usr/bin/env python
# coding: utf-8

# ## Overview of the DataSet
# 
# SpaceX has gained worldwide attention for a series of historic milestones. 
# 
# It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.
# SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. 
# 
# 
# Therefore if we can determine if the first stage will land, we can determine the cost of a launch. 
# 
# This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.
# 
# This dataset includes a record for each payload carried during a SpaceX mission into outer space.
# 

# ### Download the datasets
# 
# This assignment requires you to load the spacex dataset.
# 
# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):
# 
#  <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv" target="_blank">Spacex DataSet</a>
# 
# 

# In[2]:


get_ipython().system('pip install nbformat')


# In[3]:


get_ipython().system('pip install sqlalchemy==1.3.9')


# ### Connect to the database
# 
# Let us first load the SQL extension and establish a connection with the database
# 

# In[4]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[5]:


import csv, sqlite3

con = sqlite3.connect("my_data1.db")
cur = con.cursor()


# In[6]:


get_ipython().system('pip install -q pandas==1.1.5')


# In[7]:


get_ipython().run_line_magic('sql', 'sqlite:///my_data1.db')


# In[8]:


import pandas as pd
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.to_sql("SPACEXTBL", con, if_exists='replace', index=False,method="multi")


# ## Tasks
# 
# Now write and execute SQL queries to solve the assignment tasks.
# 
# **Note: If the column names are in mixed case enclose it in double quotes
#    For Example "Landing_Outcome"**
# 
# ### Task 1
# 
# 
# 
# 
# ##### Display the names of the unique launch sites  in the space mission
# 

# In[9]:


get_ipython().run_cell_magic('sql', '', 'Select * \nFrom SPACEXTBL\nlimit 2')


# In[10]:


get_ipython().run_cell_magic('sql', '', 'select * \nfrom SPACEXTBL \nlimit 10')


# In[11]:


get_ipython().run_cell_magic('sql', '', 'Select distinct Launch_Site\nFrom SPACEXTBL')


# 
# ### Task 2
# 
# 
# #####  Display 5 records where launch sites begin with the string 'CCA' 
# 

# In[12]:


get_ipython().run_cell_magic('sql', '', "Select sum(PAYLOAD_MASS__KG_) as Total_pyld_mass\nFrom SPACEXTBL\nWhere Customer = 'NASA (CRS)'")


# ### Task 3
# 
# 
# 
# 
# ##### Display the total payload mass carried by boosters launched by NASA (CRS)
# 

# In[13]:


get_ipython().run_line_magic('sql', "select sum(payload_mass_kg) as sum from SPACEXTBL where customer like 'NASA (CRS)'")


# ### Task 4
# 
# 
# 
# 
# ##### Display average payload mass carried by booster version F9 v1.1
# 

# In[14]:


get_ipython().run_cell_magic('sql', '', "Select distinct Booster_Version\nFrom SPACEXTBL\nWhere Booster_Version like 'F9 v1.1%'")


# ### Task 5
# 
# ##### List the date when the first succesful landing outcome in ground pad was acheived.
# 
# 
# _Hint:Use min function_ 
# 

# In[15]:


get_ipython().run_cell_magic('sql', '', 'Select min(Date) as Fst_Successful_landing\nFrom SPACEXTBL\nWhere "Landing _Outcome" = \'Success (ground pad)\'')


# ### Task 6
# 
# ##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
# 

# In[16]:


get_ipython().run_cell_magic('sql', '', 'Select Booster_Version\nFrom SPACEXTBL\nWhere "Landing _Outcome" = \'Success (drone ship)\' and PAYLOAD_MASS__KG_ Between 4000 and 6000')


# ### Task 7
# 
# 
# 
# 
# ##### List the total number of successful and failure mission outcomes
# 

# In[17]:


get_ipython().run_cell_magic('sql', "-- merge 'Success ' and 'Success' (space at the end)", "Update SPACEXTBL\nSET Mission_Outcome = 'Success'\nWhere Mission_Outcome = 'Success '")


# In[18]:


get_ipython().run_cell_magic('sql', '', 'Select Mission_Outcome, count(Mission_Outcome) as Outcome_count\nFrom SPACEXTBL\nGroup by Mission_Outcome\nOrder by 2 desc')


# ### Task 8
# 
# 
# 
# ##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery
# 

# In[19]:


get_ipython().run_cell_magic('sql', '', 'Select Booster_Version\nFrom SPACEXTBL\nWhere PAYLOAD_MASS__KG_ = (\n    Select Max(PAYLOAD_MASS__KG_)\n    From SPACEXTBL\n)')


# ### Task 9
# 
# 
# ##### List the records which will display the month names, failure landing_outcomes in drone ship ,booster versions, launch_site for the months in year 2015.
# 
# **Note: SQLLite does not support monthnames. So you need to use  substr(Date, 4, 2) as month to get the months and substr(Date,7,4)='2015' for year.**
# 

# In[20]:


get_ipython().run_cell_magic('sql', '', 'Select substr(Date, 4, 2) as month, "Landing _Outcome", Booster_Version, Launch_Site\nFrom SPACEXTBL\nWhere substr(Date,7,4)=\'2015\' and "Landing _Outcome" = \'Failure (drone ship)\'')


# ### Task 10
# 
# 
# 
# 
# ##### Rank the  count of  successful landing_outcomes between the date 04-06-2010 and 20-03-2017 in descending order.
# 

# In[21]:



get_ipython().run_cell_magic('sql', '', 'Select \n    "Landing _Outcome", count("Landing _Outcome") as cnt\nFrom SPACEXTBL\nWhere Date Between \'04-06-2010\' and \'20-03-2017\'\nGroup by "Landing _Outcome"\nOrder by 2 desc')


# ### Reference Links
# 
# * <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : String Patterns, Sorting and Grouping</a>  
# 
# *  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?origin=www.coursera.org">Hands-on Lab: Built-in functions</a>
# 
# *  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>
# 
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb">Hands-on Tutorial: Accessing Databases with SQL magic</a>
# 
# *  <a href= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb">Hands-on Lab: Analyzing a real World Data Set</a>
# 
# 
# 

# ## Author(s)
# 
# <h4> Lakshmi Holla </h4>
# 

# ## Other Contributors
# 
# <h4> Rav Ahuja </h4>
# 

# ## Change log
# | Date | Version | Changed by | Change Description |
# |------|--------|--------|---------|
# | 2021-07-09 | 0.2 |Lakshmi Holla | Changes made in magic sql|
# | 2021-05-20 | 0.1 |Lakshmi Holla | Created Initial Version |
# 

# ## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>
# 
