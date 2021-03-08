# web-scraping-challenge

Building a Flask web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page on a users local server. 

The HTML page initially shows static contents. Click the "Scrape New Data" button to populate the content via the web scrape.

## Status
Project is finalised

## Navigating the repository
### Directory: **Mission_to_Mars**
* Contains following documents:
    * mission_to_mars.ipynb
    * scrape_mars.py
    * app.py

    ### Subdirectory: **templates**
    * Contains following documents:
        * index.html

## Running order and notes
### Step 1 - Scraping
**Run: mission_to_mars.ipynb**
* To develop the webscraping code - using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter
* Code to be used in the scrape_mars.py file.
* Scraping the [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text.
* Using splinter to navigate [JPL Mars Space Images - Featured Image]((https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html)) and collect the image url for the current Featured Mars Image.
* Using Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc from the [Mars Facts webpage](https://space-facts.com/mars/). 
* Visiting the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
* Includes code to establish the mondoDB "marsDB" and to insert a static document into the collection "marscollection" as jinja templating within the index.html requires data to initially display the html in a web browser.  

###  Step 2 - Convert Jupyter notebook into Python script
**Execute in Mac OS Terminal**
* Command: jupyter nbconvert --to script mission_to_mars.ipynb
* Rename python file to scrape_mars.py

### Step 3 - Define a function for the the scraping code and capture data in a dictionary
**Add following code to the py file:**

    def scrape():

        #Python code here

        #Insert dictionary code
        marsdict = {
        "news_title": news_title,
        "paragraph_text": paragraph_text,
        "featured_image_url": featured_image_url,
        "mars_table":mars_fact_html,
        "hemheader": hemheader,
        "hemisphere_image_urls": hemisphere_image_urls
        }

            #Insert retun dictionay function
            return marsdict 

**Remove following code:**

    db.marscollection.insert_one(
                {...
                }
            )

### Step 4 - Launching html page
**Run: app.py fom Terminal**
* Visit http://127.0.0.1:5000/ in web browser

## Final Output
![Mission to Mars HTML Screenshot](https://github.com/jMacProd/web-scraping-challenge/blob/main/Missions_to_Mars/final_Screenshot/mission_to_mars_html_screenshot.png)

## Notes
**Jupyter Notebook: mission_to_mars.ipynb**
* Commented out data checks, such as print soup requests and dataframes, to reduce  the content displayed in the githib repository. When running, you can uncomment to display data checks if you feel it is required.
* included code to establish the mondoDB "marsDB" and to insert a document into the collection "marscollection" as jinja templating within the index.html required data to initially display the html in a web browser. 

**scrape_mars.py**
* Code to establish the mondoDB "marsDB" and to insert a document into the collection "marscollection" needs to be deleted so the scrape function doesn't insert a new document each time it is run.

## Technologies
* Python ersion 3.6
* Jupyter Notebok
* Pandas
* beautifulsoup 4
* Splinter
* PyMongo
* Flask
* Jinja


## Resources
* https://nbconvert.readthedocs.io/en/latest/usage.html
    Using as a command line tool to convert jupyter notebook to a python file.

* https://medium.com/@gokulprakash22/getting-started-with-flask-pymongo-d6326db2a9a7

* https://problemsolvingwithpython.com/07-Functions-and-Modules/07.05-Calling-Functions-from-Other-Files/

* https://www.quora.com/How-can-I-print-the-contents-of-mongoDB-in-a-HTML-page-using-Python

* https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e

* https://overiq.com/flask-101/basics-of-jinja-template-language/
    Info on how to make jinja template render html tags correctly-->


## Contact
Created by https://github.com/jMacProd - feel free to contact me!
