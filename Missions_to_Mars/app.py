#################################################
# Dependancies
#################################################

#https://medium.com/@gokulprakash22/getting-started-with-flask-pymongo-d6326db2a9a7
from flask import Flask, jsonify, request, redirect, render_template
from flask_pymongo import PyMongo

#https://problemsolvingwithpython.com/07-Functions-and-Modules/07.05-Calling-Functions-from-Other-Files/
#from scrape_mars import scrape

#Another way to import this function in 
import scrape_mars
#scrape_mars.scrape <- do this in the scrape route

#################################################
# Flask Setup
#################################################
#https://flask-pymongo.readthedocs.io/en/latest/

app = Flask(__name__)


#################################################
# Database Setup
#################################################

#example:app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    # the last bit of the uri link creates the database I think
app.config["MONGO_URI"] = 'mongodb://localhost:27017/marsDB'
mongo = PyMongo(app)

# Declare the collection
marscollection = mongo.db.marscollection


#Need to populate the database so jinja template doesn't intially error
marscollection.insert(
    {"news_title": ["Please press the Scrape New Data button to refresh"],
    "paragraph_text": [""],
    "featured_image_url": "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg",
    "mars_table":"",
    "hemheader": ['Cerberus Hemisphere Enhanced',
    'Schiaparelli Hemisphere Enhanced',
    'Syrtis Major Hemisphere Enhanced',
    'Valles Marineris Hemisphere Enhanced'],
    "hemisphere_image_urls": ['https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg',
 'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg',
 'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg',
 'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg']
    }
    )

#################################################
# scrape -Test
#################################################

#@app.route('/')
#def home():
#    return "App is working perfectly"


#################################################
# Flask Routes
#################################################

#https://www.quora.com/How-can-I-print-the-contents-of-mongoDB-in-a-HTML-page-using-Python

@app.route("/")
def index():
#Needed to make this "index" to pick up index.html file 
#    print("Server received request for 'Home' page...")

    marsquery = marscollection.find_one()

    #https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e
    return render_template("index.html", marsquery=marsquery)


#################################################
# scrape
#################################################

@app.route("/scrape")
def scrape():
#    print("Server received request for 'scrape' page...")

    #call scrape function
    mars_scrape = scrape_mars.scrape()

    #confirming scrape worked
    #return jsonify(mars_scrape)

    # Insert the dictionary into Mongo
    marscollection.update({}, mars_scrape, upsert=True)
    
    #After loading the data go back to the home route
        #which will then display the data
    return redirect("/")

#################################################
# End
#################################################1
if __name__ == "__main__":
    app.run(debug=True)
