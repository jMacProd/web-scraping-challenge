def scrape():

    #!/usr/bin/env python
    # coding: utf-8

    # # Mission to Mars
    # * Developing the webscraping code to be used in a Flask web app.
    # * Using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

    # In[1]:


    # Dependencies
    import os
    import pandas as pd

    #enables to read and search html
    from bs4 import BeautifulSoup as bs

    #allows Python to reach out to the internet 
    import requests
    from time import sleep


    # In[2]:


    #splinter actications
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # ### NASA Mars News
    # * Scraping the [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text.

    # In[3]:


    #Tell the splinter browser to go to this website
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[4]:


    # Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
    html = browser.html
    soup = bs(html, 'html.parser')


    # In[5]:


    #Collect the image container

    results = soup.find('li', class_='slide')


    # In[6]:


    #Assign the text to variables that you can reference later

    news_title = []
    paragraph_text = []

    sleep(1)

    # Retrieve the news item title
    #title = results.find('div', class_='content_title')
    title = results.find('div', class_='list_text')
        
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


    # In[7]:


    # Check news_title
    #news_title


    # In[8]:


    # Check paragraph text
    #paragraph_text


    # In[9]:


    # Close the browser after scraping
    browser.quit()


    # ### JPL Mars Space Images - Featured Image
    # *  Using splinter to navigate the site and collect the image url for the current Featured Mars Image.

    # In[10]:


    #set new browser
    browserfi = Browser('chrome', **executable_path, headless=False)

    #Tell the splinter browser to go to this website

    urlfi = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    browserfi.visit(urlfi + 'index.html')


    # In[11]:


    # Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
    htmlfi = browserfi.html
    soupfi = bs(htmlfi, 'html.parser')


    # In[12]:


    #print(soupfi.prettify())


    # In[13]:


    #Collect the image container

    resultsfi = soupfi.find('div', class_='floating_text_area')


    # In[14]:


    #resultsfi


    # In[15]:


    # Assign the url string to a variable called `featured_image_url`.

    link = resultsfi.a['href']
    featured_image_url = urlfi + link


    # In[16]:


    #Check image url
    #featured_image_url


    # In[17]:


    browserfi.quit()


    # ### Mars Facts Table
    # * Using Pandas to scraping the table containing facts about the planet including Diameter, Mass, etc from the [Mars Facts webpage](https://space-facts.com/mars/). 

    # In[18]:


    #Visit the Mars Facts webpage [here](https://space-facts.com/mars/)
    urlmf = 'https://space-facts.com/mars/'


    # In[19]:


    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
        # Use Panda's `read_html` to parse the url

    tables = pd.read_html(urlmf)
    #tables


    # In[20]:


    mars_fact = tables[0]
    #mars_fact


    # In[21]:


    #reset index
    mars_fact.set_index(0, inplace=True)


    # In[22]:


    # Check table
    #mars_fact


    # In[23]:


    #remove index label
    mars_fact.index.names = ['']
    #mars_fact


    # In[24]:


    #reset columns
    mars_fact.columns = ['Mars']


    # In[25]:


    # Check mars_fact
    #mars_fact


    # In[26]:


    #Use Pandas to convert the data to a HTML table string.
    mars_fact_html = mars_fact.to_html()
    #mars_fact_html


    # In[27]:


    #You may have to strip unwanted newlines to clean up the table.
    mars_fact_html = mars_fact_html.replace('\n', '')


    # In[28]:


    #mars_fact_html


    # ### Mars Hemispheres
    # Visiting the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

    # In[29]:


    #from time import sleep

    #set new browser
    browsermh = Browser('chrome', **executable_path, headless=False)

    #Tell the splinter browser to go to this website

    urlmh = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browsermh.visit(urlmh)     
            


    # In[30]:


    #define main url
    main_page = "https://astrogeology.usgs.gov"
    #print(main_page)


    # In[31]:


    #create list called hemisphere_image_urls

    hemheader = []
    hemisphere_image_urls = []


    # In[32]:


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


    # In[33]:


    #check lists
    #hemheader


    # In[34]:


    #hemisphere_image_urls


    # In[35]:


    # Module used to connect Python with MongoDb
    import pymongo
    # The default port used by MongoDB is 27017
    # https://docs.mongodb.com/manual/reference/default-mongodb-port/
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Define the 'classDB' database in Mongo
    db = client.marsDB


    # In[36]:


    # THIS CODE APPEARS IN THE SOURCE JUPYTER NOTEBOOK - TO BE DELETED IN THIS FILE
    #db.marscollection.insert_one(
    #    {
    #        "news_title": ["Please press the Scrape New Data button to refresh"],
    #        "paragraph_text": [""],
    #        "featured_image_url": "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg",
    #        "mars_table":"",
    #        "hemheader": ['Cerberus Hemisphere Enhanced',
    #                    'Schiaparelli Hemisphere Enhanced',
    #                    'Syrtis Major Hemisphere Enhanced',
    #                    'Valles Marineris Hemisphere Enhanced'],
    #        "hemisphere_image_urls": ['https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg',
    #                                'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg',
    #                                'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg',
    #                                'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg']
    #    }
    #)


    #Insert dictionary code
    marsdict = {
        "news_title": news_title,
        "paragraph_text": paragraph_text,
        "featured_image_url": featured_image_url,
        "mars_table":mars_fact_html,
        "hemheader": hemheader,
        "hemisphere_image_urls": hemisphere_image_urls
        }

    #Insert return dictionay function
    return marsdict

