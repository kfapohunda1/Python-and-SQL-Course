#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/Logos/organization_logo/organization_logo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 
# # Introduction to Pandas in Python
# 
# Estimated time needed: **15** minutes
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# -   Use Pandas to access and view data
# 

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li><a href="dataset">About the Dataset</a></li>
#         <li><a href="pandas">Introduction of <code>Pandas</code></a></li>
#         <li><a href="data">Viewing Data and Accessing Data</a></li>
#         <li><a href="quiz">Quiz on DataFrame</a></li>
#     </ul>
#   
# </div>
# 
# <hr>
# 

# <h2 id="dataset">About the Dataset</h2>
# 

# The table has one row for each album and several columns
# 
# <ul>
#     <li><b>artist</b>: Name of the artist</li>
#     <li><b>album</b>: Name of the album</li>
#     <li><b>released_year</b>: Year the album was released</li>
#     <li><b>length_min_sec</b>: Length of the album (hours,minutes,seconds)</li>
#     <li><b>genre</b>: Genre of the album</li>
#     <li><b>music_recording_sales_millions</b>: Music recording sales (millions in USD) on <a href="http://www.song-database.com/">[SONG://DATABASE]</a></li>
#     <li><b>claimed_sales_millions</b>: Album's claimed sales (millions in USD) on <a href="http://www.song-database.com/">[SONG://DATABASE]</a></li>
#     <li><b>date_released</b>: Date on which the album was released</li>
#     <li><b>soundtrack</b>: Indicates if the album is the movie soundtrack (Y) or (N)</li>
#     <li><b>rating_of_friends</b>: Indicates the rating from your friends from 1 to 10</li>
# </ul>
# 
# You can see the dataset here:
# 
# <font size="1">
# <table font-size:xx-small>
#   <tr>
#     <th>Artist</th>
#     <th>Album</th> 
#     <th>Released</th>
#     <th>Length</th>
#     <th>Genre</th> 
#     <th>Music recording sales (millions)</th>
#     <th>Claimed sales (millions)</th>
#     <th>Released</th>
#     <th>Soundtrack</th>
#     <th>Rating (friends)</th>
#   </tr>
#   <tr>
#     <td>Michael Jackson</td>
#     <td>Thriller</td> 
#     <td>1982</td>
#     <td>00:42:19</td>
#     <td>Pop, rock, R&B</td>
#     <td>46</td>
#     <td>65</td>
#     <td>30-Nov-82</td>
#     <td></td>
#     <td>10.0</td>
#   </tr>
#   <tr>
#     <td>AC/DC</td>
#     <td>Back in Black</td> 
#     <td>1980</td>
#     <td>00:42:11</td>
#     <td>Hard rock</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td></td>
#     <td>8.5</td>
#   </tr>
#     <tr>
#     <td>Pink Floyd</td>
#     <td>The Dark Side of the Moon</td> 
#     <td>1973</td>
#     <td>00:42:49</td>
#     <td>Progressive rock</td>
#     <td>24.2</td>
#     <td>45</td>
#     <td>01-Mar-73</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Whitney Houston</td>
#     <td>The Bodyguard</td> 
#     <td>1992</td>
#     <td>00:57:44</td>
#     <td>Soundtrack/R&B, soul, pop</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td>Y</td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Meat Loaf</td>
#     <td>Bat Out of Hell</td> 
#     <td>1977</td>
#     <td>00:46:33</td>
#     <td>Hard rock, progressive rock</td>
#     <td>20.6</td>
#     <td>43</td>
#     <td>21-Oct-77</td>
#     <td></td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Eagles</td>
#     <td>Their Greatest Hits (1971-1975)</td> 
#     <td>1976</td>
#     <td>00:43:08</td>
#     <td>Rock, soft rock, folk rock</td>
#     <td>32.2</td>
#     <td>42</td>
#     <td>17-Feb-76</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Bee Gees</td>
#     <td>Saturday Night Fever</td> 
#     <td>1977</td>
#     <td>1:15:54</td>
#     <td>Disco</td>
#     <td>20.6</td>
#     <td>40</td>
#     <td>15-Nov-77</td>
#     <td>Y</td>
#     <td>9.0</td>
#   </tr>
#     <tr>
#     <td>Fleetwood Mac</td>
#     <td>Rumours</td> 
#     <td>1977</td>
#     <td>00:40:01</td>
#     <td>Soft rock</td>
#     <td>27.9</td>
#     <td>40</td>
#     <td>04-Feb-77</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
# </table></font>
# 

# <hr>
# 

# <h2 id="pandas">Introduction of <code>Pandas</code></h2>
# 

# In[20]:


# Dependency needed to install file 

get_ipython().system('pip install xlrd')


# In[21]:


# Import required library

import pandas as pd


# After the import command, we now have access to a large number of pre-built classes and functions. This assumes the library is installed; in our lab environment all the necessary libraries are installed. One way pandas allows you to work with data is a dataframe. Let's go through the process to go from a comma separated values (<b>.csv</b>) file to a dataframe. This variable <code>csv_path</code> stores the path of the <b>.csv</b>, that is  used as an argument to the <code>read_csv</code> function. The result is stored in the object <code>df</code>, this is a common short form used for a variable referring to a Pandas dataframe. 
# 

# In[22]:


# Read data from CSV file

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)


# We can use the method <code>head()</code> to examine the first five rows of a dataframe: 
# 

# In[23]:


# Print first five rows of the dataframe

df.head()


#  We use the path of the excel file and the function <code>read_excel</code>. The result is a data frame as before:
# 

# In[5]:


# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()


# We can access the column <b>Length</b> and assign it a new dataframe <b>x</b>:
# 

# In[54]:


# Access to the column Length

x = df[['Length']]
x


# #### The process is shown in the figure: 
# 

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Images/DataEgOne.png" width="750" />
# 

# <hr>
# 

# <h2 id="data">Viewing Data and Accessing Data</h2>
# 

# You can also get a column as a series. You can think of a Pandas series as a 1-D dataframe. Just use one bracket: 
# 

# In[32]:


# Get the column as a series

x = df['Length']
x


# You can also get a column as a dataframe. For example, we can assign the column <b>Artist</b>:
# 

# In[33]:


# Get the column as a dataframe

x = type(df[['Artist']])
x


# You can do the same thing for multiple columns; we just put the dataframe name, in this case, <code>df</code>, and the name of the multiple column headers enclosed in double brackets. The result is a new dataframe comprised of the specified columns:
# 

# In[34]:


# Access to multiple columns

y = df[['Artist','Length','Genre']]
y


# The process is shown in the figure:
# 

# <img src = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Images/DataEgTwo.png" width="1100" />
# 

# One way to access unique elements is the <code>iloc</code> method, where you can access the 1st row and the 1st column as follows:
# 

# In[35]:


# Access the value on the first row and the first column

df.iloc[0, 0]


# You can access the 2nd row and the 1st column as follows:
# 

# In[36]:


# Access the value on the second row and the first column

df.iloc[1,0]


# You can access the 1st row and the 3rd column as follows: 
# 

# In[37]:


# Access the value on the first row and the third column

df.iloc[0,2]


# In[38]:


# Access the value on the second row and the third column
df.iloc[1,2]


# In[ ]:





# This is shown in the following image
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/2_loc.PNG" width="750" />
# 

# You can access the column using the name as well, the following are the same as above: 
# 

# In[ ]:





# In[39]:


# Access the column using the name

df.loc[1, 'Artist']


# In[40]:


# Access the column using the name

df.loc[1, 'Artist']


# In[41]:


# Access the column using the name

df.loc[0, 'Released']


# In[42]:


# Access the column using the name

df.loc[1, 'Released']


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/1_loc.png" width="750" />
# 

# You can perform slicing using both the index and the name of the column:
# 

# In[65]:


# Slicing the dataframe

df.iloc[0:2, 0:3]


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/4_loc.png" width="750" />
# 

# In[44]:


# Slicing the dataframe using name

df.loc[0:2, 'Artist':'Released']


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/3_loc.png" width="750" />
# 

# <hr>
# 

# <h2 id="quiz">Quiz on DataFrame</h2>
# 

# Use a variable <code>q</code> to store the column <b>Rating</b> as a dataframe
# 

# In[47]:


# Write your code below and press Shift+Enter to execute
q=df[['Rating']]
q


# <details><summary>Click here for the solution</summary>
# 
# ```python
# q = df[['Rating']]
# q
#     
# ```
# 
# </details>
# 

# Assign the variable <code>q</code> to the dataframe that is made up of the column <b>Released</b> and <b>Artist</b>:
# 

# In[67]:


# Write your code below and press Shift+Enter to execute
q=df[['Released','Artist']]
q


# <details><summary>Click here for the solution</summary>
# 
# ```python
# q = df[['Released', 'Artist']]
# q
#     
# ```
# 
# </details>
# 

# Access the 2nd row and the 3rd column of <code>df</code>:
# 

# In[68]:


# Write your code below and press Shift+Enter to execute
df.iloc[1,2]


# <details><summary>Click here for the solution</summary>
# 
# ```python
# df.iloc[1, 2]
#     
# ```
# 
# </details>
# 

# Use the following list to convert the dataframe index <code>df</code> to characters and assign it to <code>df_new</code>; find the element corresponding to the row index <code>a</code> and column  <code>'Artist'</code>. Then select the rows <code>a</code> through <code>d</code> for the column  <code>'Artist'</code>
# 

# In[71]:


new_index=['a','b','c','d','e','f','g','h']

df_new = df
df_new.loc["a":'d', 'Artist']

# or

df_new=df
df_new.index=new_index
df_new.loc['a', 'Artist']
df_new.loc['a':'d', 'Artist']


# <details><summary>Click here for the solution</summary>
# 
# ```python
# df_new=df
# df_new.index=new_index
# df_new.loc['a', 'Artist']
# df_new.loc['a':'d', 'Artist']
#     
# ```
# 
# </details>
# 

# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. However, there is one more thing you need to do. The Data Science community encourages sharing work. The best way to share and showcase your work is to share it on GitHub. By sharing your notebook on GitHub you are not only building your reputation with fellow data scientists, but you can also show it off when applying for a job. Even though this was your first piece of work, it is never too early to start building good habits. So, please read and follow <a href="https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks/" target="_blank">this article</a> to learn how to share your work.
# <hr>
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <h2>Get IBM Watson Studio free of charge!</h2>
#     <p><a href="https://cloud.ibm.com/catalog/services/watson-studio"><img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/BottomAd.png" width="750" align="center"></a></p>
# </div>
# 

# ## Authors:
# 
#  [Joseph Santarcangelo](https://www.linkedin.com/in/joseph-s-50398b136?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ) 
# 
# Joseph Santarcangelo has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 
# ## Change Log
# 
# | Date (YYYY-MM-DD) | Version | Changed By | Change Description                 |
# | ----------------- | ------- | ---------- | ---------------------------------- |
# | 2020-08-26        | 2.0     | Lavanya    | Moved lab to course repo in GitLab |
# | 2020-11-24        | 3.0     | Nayef      | Added new images                   |
# |                   |         |            |                                    |
# 
# <hr/>
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 

# In[ ]:




