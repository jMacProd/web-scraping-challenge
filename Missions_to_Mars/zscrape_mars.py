def scrape():

    #!/usr/bin/env python
    # coding: utf-8

    # In[528]:


    # Dependencies
    import os
    import pandas as pd

    #enables to read and search html
    from bs4 import BeautifulSoup as bs

    #allows Python to reach out to the internet 
    import requests


    # In[529]:


    #splinter actications
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager

#def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # ### NASA Mars News

    # In[530]:


    #Tell the splinter browser to go to this website
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[531]:


    # Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
    html = browser.html
    soup = bs(html, 'html.parser')


    # In[532]:


    #print(soup.prettify())
    #now the full html has appeared


    # In[533]:


    #Collect the latest News Title and Paragraph Text
        # Examine the results, then determine element that contains sought info
        # results are returned as an iterable list
    results = soup.find_all('li', class_='slide')


    # In[534]:


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
        
        
        #print("")
        #print(title_text)
        #print("--")
        #print(article_teaser_text)
        #print("--------------------")


    # In[535]:


    # Close the browser after scraping
    browser.quit()


    # ### JPL Mars Space Images - Featured Image

    # In[536]:


    #set new browser
    browserfi = Browser('chrome', **executable_path, headless=False)

    #Tell the splinter browser to go to this website

    urlfi = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    browserfi.visit(urlfi + 'index.html')


    # In[537]:


    # Create BeautifulSoup object; parse with 'html.parser' - using the splinter browser
    htmlfi = browserfi.html
    soupfi = bs(htmlfi, 'html.parser')


    # In[538]:


    #print(soupfi.prettify())


    # In[539]:


    #Collect the image container

    resultsfi = soupfi.find('div', class_='floating_text_area')


    # In[540]:


    #resultsfi


    # In[541]:


    # Assign the url string to a variable called `featured_image_url`.

    link = resultsfi.a['href']
    featured_image_url = urlfi + link

    #featured_image_url


    # In[542]:


    browserfi.quit()


    # ### Mars Facts Table

    # In[543]:


    #Visit the Mars Facts webpage [here](https://space-facts.com/mars/)
    urlmf = 'https://space-facts.com/mars/'


    # In[544]:


    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
        # Use Panda's `read_html` to parse the url

    tables = pd.read_html(urlmf)
    #tables


    # In[545]:


    mars_fact = tables[0]
    #mars_fact


    # In[546]:


    #reset index
    mars_fact.set_index(0, inplace=True)


    # In[547]:


    #mars_fact


    # In[548]:


    #remove index label
    mars_fact.index.names = ['']
    #mars_fact


    # In[549]:


    #reset columns
    mars_fact.columns = ['Mars']
    #mars_fact


    # In[550]:


    #Use Pandas to convert the data to a HTML table string.
    mars_fact_html = mars_fact.to_html()
    #mars_fact_html


    # In[551]:


    #You may have to strip unwanted newlines to clean up the table.
    mars_fact_html = mars_fact_html.replace('\n', '')


    # In[552]:


    #mars_fact_html


    # In[553]:


    #You can also save the table directly to a file.
        #sample - df.to_html('table.html')
    mars_fact.to_html('mars_fact.html')


    # ### Mars Hemispheres
    # Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

    # In[554]:


    from time import sleep

    sleep(1)

    #set new browser
    browsermh = Browser('chrome', **executable_path, headless=False)

    #Tell the splinter browser to go to this website

    urlmh = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browsermh.visit(urlmh)     
            


    # In[555]:


    #define main url
    main_page = "https://astrogeology.usgs.gov"
    #print(main_page)


    # In[556]:


    #create list called hemisphere_image_urls

    hemheader = []
    hemisphere_image_urls = []


    # In[557]:


    # Loop through returned results
    for x in range(0, 4):
        
        sleep(1)
        
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
        #print(header)
        #print("--")
        
        
        #clicks on x link to go to next page
        browsermh.visit(main_page+linkcontmh)
        
        sleep(1)
        #print(browsermh.url)
        
        htmlnp = browsermh.html
        soupnp = bs(htmlnp, 'html.parser')
        
        #Collect np link container
        resultsnp = soupnp.find('div', class_='wide-image-wrapper')
        #print(resultsnp)
        
        
        find_images = resultsnp.find_all('img')[1]
        
        
        #Find second li tag
        litag = find_images['src']
        

        
            
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



    # Store data in a dictionary
    marsdict = {
        "news_title": news_title,
        "paragraph_text": paragraph_text,
        "featured_image_url": featured_image_url,
        "hemheader": hemheader,
        "hemisphere_image_urls": hemisphere_image_urls
    }



    # Return results
    return marsdict

#scrape()

    # In[560]:


    #check lists
    #hemheader


    # In[561]:


    #hemisphere_image_urls


    # In[ ]:




