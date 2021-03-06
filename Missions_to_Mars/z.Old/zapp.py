
from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo
#https://problemsolvingwithpython.com/07-Functions-and-Modules/07.05-Calling-Functions-from-Other-Files/
import scrape_mars




#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Mongo Connection 
#################################################
# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


##SAMPLE
# Declare the database
#db = client.fruits_db
# Declare the collection
#fruits = db.fruits_db


# Declare the database
db = client.mars_db

# Declare the collection
marsdata = db.mars_db




#################################################
# Flask Routes
#################################################

@app.route("/")
def home():

    # Return template
    return render_template("index.html")


#################################################
# Scrape
#################################################
# Create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function
@app.route("/api/v1.0/scrape")

def scrape():

    # Run the scrape function and save the results to a variable
    dict = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    #mars_data.update({}, scraped_data, upsert=True)

    # Insert the document into the database
    # The database and collection, if they don't already exist, will be created at this point.
    marsdata.insert_one(dict)

    # Redirect to the scraped data page
    return redirect("/data")





    if __name__ == "__main__":
    app.run(debug=True)
