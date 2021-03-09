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
