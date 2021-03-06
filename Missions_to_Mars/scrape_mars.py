def scrape():

    #!/usr/bin/env python
    # coding: utf-8

    # # Mission to Mars
    # * Developing the webscraping code to be used in a Flask web app.
    # * Using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

    # In[33]:


    # Dependencies
    import os
    import pandas as pd

    #enables to read and search html
    from bs4 import BeautifulSoup as bs

    #allows Python to reach out to the internet 
    import requests


    # In[34]:


    #splinter actications
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # ### NASA Mars News
    # * Scraping the [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text.

    # In[35]:


    #Tell the splinter browser to go to this website
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[36]:


    # Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
    html = browser.html
    soup = bs(html, 'html.parser')


    # In[37]:


    #Collect the image container

    results = soup.find('li', class_='slide')


    # In[38]:


    #Assign the text to variables that you can reference later

    news_title = []
    paragraph_text = []

    
    # Retrieve the news item title
    title = results.find('div', class_='content_title')
        
    # Access the titles text content
    title_text = title.a.text
        
    # Retrieve the Paragraph Text
    article_teaser = results.find('div', class_='article_teaser_body')
        
    # Access the paragraphs's text content
    article_teaser_text = article_teaser.text
        
    #Append the lists
    news_title.append(title_text)
    paragraph_text.append(article_teaser_text)
        
        
    #print("")
    #print(title_text)
    #print("--")
    #print(article_teaser_text)
    #print("--------------------")


    # In[39]:


    # Check news_title
    #news_title


    # In[40]:


    # Check paragraph text
    #paragraph_text


    # In[41]:


    # Close the browser after scraping
    browser.quit()


    # ### JPL Mars Space Images - Featured Image
    # *  Using splinter to navigate the site and collect the image url for the current Featured Mars Image.

    # In[42]:


    #set new browser
    browserfi = Browser('chrome', **executable_path, headless=False)

    #Tell the splinter browser to go to this website

    urlfi = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    browserfi.visit(urlfi + 'index.html')


    # In[43]:


    # Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
    htmlfi = browserfi.html
    soupfi = bs(htmlfi, 'html.parser')


    # In[44]:


    #print(soupfi.prettify())


    # In[45]:


    #Collect the image container

    resultsfi = soupfi.find('div', class_='floating_text_area')


    # In[46]:


    #resultsfi


    # In[47]:


    # Assign the url string to a variable called `featured_image_url`.

    link = resultsfi.a['href']
    featured_image_url = urlfi + link


    # In[48]:


    #Check image url
    #featured_image_url


    # In[49]:


    browserfi.quit()


    # ### Mars Facts Table
    # * Using Pandas to scraping the table containing facts about the planet including Diameter, Mass, etc from the [Mars Facts webpage](https://space-facts.com/mars/). 

    # In[50]:


    #Visit the Mars Facts webpage [here](https://space-facts.com/mars/)
    urlmf = 'https://space-facts.com/mars/'


    # In[51]:


    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
        # Use Panda's `read_html` to parse the url

    tables = pd.read_html(urlmf)
    #tables


    # In[52]:


    mars_fact = tables[0]
    #mars_fact


    # In[53]:


    #reset index
    mars_fact.set_index(0, inplace=True)


    # In[54]:


    # Check table
    #mars_fact


    # In[55]:


    #remove index label
    mars_fact.index.names = ['']
    #mars_fact


    # In[56]:


    #reset columns
    mars_fact.columns = ['Mars']


    # In[57]:


    # Check mars_fact
    #mars_fact


    # In[58]:


    #Use Pandas to convert the data to a HTML table string.
    mars_fact_html = mars_fact.to_html()
    #mars_fact_html


    # In[59]:


    #You may have to strip unwanted newlines to clean up the table.
    mars_fact_html = mars_fact_html.replace('\n', '')


    # In[60]:


    #mars_fact_html


    # ### Mars Hemispheres
    # Visiting the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

    # In[61]:


    from time import sleep

    #set new browser
    browsermh = Browser('chrome', **executable_path, headless=False)

    #Tell the splinter browser to go to this website

    urlmh = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browsermh.visit(urlmh)     
            


    # In[62]:


    #define main url
    main_page = "https://astrogeology.usgs.gov"
    #print(main_page)


    # In[63]:


    #create list called hemisphere_image_urls

    hemheader = []
    hemisphere_image_urls = []


    # In[64]:


    # Loop through returned results
    for x in range(0, 4):
        
        sleep(1)
        
        # converting splinter browser to html.
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
        #print(header)
        #print("--")
        
        
        #clicks on x link to go to next page
        browsermh.visit(main_page+linkcontmh)
        
        sleep(1)
        #print(browsermh.url)
        
        #Create a new html splinter browser and parse into beautifulsoup
        htmlnp = browsermh.html
        soupnp = bs(htmlnp, 'html.parser')
        
        #Collect np link container
        resultsnp = soupnp.find('div', class_='wide-image-wrapper')
        #print(resultsnp)
        
        #Find the second img - which is the fullsized inmage that is not he download version
        find_images = resultsnp.find_all('img')[1]
        
        
        #collect the src link
        litag = find_images['src']
        

        #Create complete link to image          
        imgnp_url = main_page+litag
        #print(imgnp_url)
            
        #print("--------")
            
    
    
        #Append the lists
        hemheader.append(header)
        hemisphere_image_urls.append(imgnp_url)
        
        
            
        #hemisphere_image_urls.append(link_dict)
        
        
        #Go back to main page
        browsermh.back()

    browsermh.quit()    


    # In[65]:


    #check lists
    #hemheader


    # In[66]:


    #hemisphere_image_urls


    # ### Next steps
    # * convert jupyter notebook to python - executed in Mac OS Terminal with following command:
    #     * jupyter nbconvert --to script mission_to_mars.ipynb
    #     * Source: https://nbconvert.readthedocs.io/en/latest/usage.html
    # * Renamed python file to scrape_mars.py
    # * Use the scraping code to define a function in the scrape_mars.py file

    # In[ ]:

    # Store data in a dictionary
    marsdict = {
        "news_title": news_title,
        "paragraph_text": paragraph_text,
        "featured_image_url": featured_image_url,
        "mars_table":mars_fact_html,
        "hemheader": hemheader,
        "hemisphere_image_urls": hemisphere_image_urls        
    }



    # Return results
    return marsdict    

#scrape()




