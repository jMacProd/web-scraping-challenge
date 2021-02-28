#!/usr/bin/env python
# coding: utf-8

# In[159]:


# Dependencies
import os
import pandas as pd

#enables to read and search html
from bs4 import BeautifulSoup as bs

#allows Python to reach out to the internet 
import requests


# In[160]:


#splinter actications
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### NASA Mars News

# In[161]:


#Tell the splinter browser to go to this website
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[ ]:


# URL of page to be scraped - this the beautiful soup straight from htm - didn;t pick up all html
#url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[ ]:


# Retrieve page with the requests module
#response = requests.get(url)


# In[162]:


# Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
html = browser.html
soup = bs(html, 'html.parser')


# In[163]:


print(soup.prettify())
#now the full html has appeared


# In[166]:


#Collect the latest News Title and Paragraph Text
    # Examine the results, then determine element that contains sought info
    # results are returned as an iterable list
results = soup.find_all('li', class_='slide')


# In[226]:


#Assign the text to variables that you can reference later

news_title = []
paragraph_text = []

# Loop through returned results
for result in results:
    
    # Retrieve the news item title
    title = result.find('div', class_='content_title')
    
    # Access the titles text content
    title_text = title.a.text
    
    # Retrieve the Paragraph Text
    article_teaser = result.find('div', class_='article_teaser_body')
    
    # Access the paragraphs's text content
    article_teaser_text = article_teaser.text
    
    #Append the lists
    news_title.append(title_text)
    paragraph_text.append(article_teaser_text)
    
    
    print("")
    print(title_text)
    print("--")
    print(article_teaser_text)
    print("--------------------")


# In[224]:


browser.links.find_by_partial_text('More')


# In[ ]:


# Retrieve the Paragraph Text

#    article_teaser = result.find('div', class_='article_teaser_body')
   
   # Access the thread's text content
#    article_teaser_text = article_teaser.text
#    print(article_teaser_text)


# ### JPL Mars Space Images - Featured Image

# In[168]:


#set new browser
browserfi = Browser('chrome', **executable_path, headless=False)

#Tell the splinter browser to go to this website

urlfi = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
browserfi.visit(urlfi + 'index.html')


# In[169]:


# Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
htmlfi = browserfi.html
soupfi = bs(htmlfi, 'html.parser')


# In[170]:


print(soupfi.prettify())


# In[171]:


#Collect the image container

resultsfi = soupfi.find('div', class_='floating_text_area')


# In[172]:


resultsfi


# In[173]:


# Assign the url string to a variable called `featured_image_url`.

link = resultsfi.a['href']
featured_image_url = urlfi + link

featured_image_url


# ### Mars Facts Table

# In[174]:


#Visit the Mars Facts webpage [here](https://space-facts.com/mars/)
urlmf = 'https://space-facts.com/mars/'


# In[175]:


# Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Panda's `read_html` to parse the url

tables = pd.read_html(urlmf)
tables


# In[176]:


mars_fact = tables[0]
mars_fact


# In[177]:


#reset index
mars_fact.set_index(0, inplace=True)


# In[178]:


mars_fact


# In[179]:


#remove index label
mars_fact.index.names = ['']
mars_fact


# In[180]:


#reset columns
mars_fact.columns = ['Mars']
mars_fact


# In[181]:


#Use Pandas to convert the data to a HTML table string.
mars_fact_html = mars_fact.to_html()
mars_fact_html


# In[182]:


#You may have to strip unwanted newlines to clean up the table.
mars_fact_html = mars_fact_html.replace('\n', '')


# In[183]:


mars_fact_html


# In[184]:


#You can also save the table directly to a file.
    #sample - df.to_html('table.html')
mars_fact.to_html('mars_fact.html')


# In[185]:


get_ipython().system('open mars_fact.html')


# ### Mars Hemispheres
# Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

# In[356]:


#https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    #You will need to click each of the links to the hemispheres
        #in order to find the image url to the full resolution image.
        
#set new browser
browsermh = Browser('chrome', **executable_path, headless=False)

#Tell the splinter browser to go to this website

urlmh = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browsermh.visit(urlmh)     
        


# In[299]:


# Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
#htmlmh = browsermh.html


# In[ ]:


#print(soupmh.prettify())


# In[ ]:


#Collect the link container

#resultsmh = soupmh.find_all('div', class_='description')
#resultsmh


# In[324]:


#define main url
main_page = "https://astrogeology.usgs.gov"
print(main_page)


# In[362]:


#create list called hemisphere_image_urls
hemisphere_image_urls = []
hemisphere_image_urls


# In[308]:


from time import sleep


# In[357]:


# Loop through returned results
for x in range(0, 4):
    
    sleep(2)
    
    # Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
    htmlmh = browsermh.html
    
    #Parse it to Beautiful Soup - makes the html searchable by tags
    soupmh = bs(htmlmh, 'html.parser')
    
    
    #Find the link container
    resultsmh = soupmh.find_all('div', class_='description')
    #print(resultsmh[x])
    
    
    #Retrieve the link container
    linkcontmh = resultsmh[x].a['href']
    #print(linkcontmh)
    
    #Retrieve header
    header = resultsmh[x].a.text
    print(header)
    print("--")
    
    
    #clicks on x link to go to next page
    browsermh.visit(main_page+linkcontmh)
    #browser.click_link_by_href('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')
    #browsernp.links.find_by_partial_text(linkcontmh)
    sleep(2)
    #print(browsermh.url)
    
    responsenp = requests.get(browsermh.url)
    soupnp = bs(responsenp.text, 'html.parser')
    
    #Collect np link container
    resultsnp = soupnp.find('div', class_='downloads')
    #print(resultsnp)
    
    
    #Find second li tag
    litag = resultsnp.find('img', class_='wide_image')
    
    ############THIS IS KILLING ME - WHY CAN I NOT GET THE INAGE SOURCE
    litag.get['src']
    
    

    
    #find image url
    #imgnplink = litag['src']
    #print(imgnplink)
    
          
    #imgnp_url = main_page+imgnplink
    #print(imgnp_url)
          
          
    print("--------")
          
 
   
    
    #Collect title and url into dictionary
    #for title, img_url in XXXXX:
    link_dict = {}
    link_dict["title"] = header
    link_dict["img_url"] = imgnp_url
        
    hemisphere_image_urls.append(link_dict)
    
    
    #Go back to main page
    browsermh.back()
    


# In[363]:


#temp solution
link_dict = {}
link_dict["title"] = 'Cerberus Hemisphere Enhanced'
link_dict["img_url"] = 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'
        
hemisphere_image_urls.append(link_dict)


# In[364]:


#Check list of dictionaries
hemisphere_image_urls


# ## Step 2 - MongoDB and Flask Application

# In[ ]:




