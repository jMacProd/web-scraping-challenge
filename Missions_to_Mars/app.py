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
# Database Setup
#################################################

#conn = 'mongodb://localhost:27017'
#client = PyMongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
#db = client.marsDB

# Declare the collection
#marscollection = db.marsDB

#################################################
# Flask Setup
#################################################
#https://flask-pymongo.readthedocs.io/en/latest/

app = Flask(__name__)

#example:app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    # the last bit of the uri link creates the database I think
app.config["MONGO_URI"] = 'mongodb://localhost:27017/marsDB'
mongo = PyMongo(app)
#client = PyMongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
#db = mongo.marsDB

# Declare the collection
marscollection = mongo.db.marscollection


#################################################
# scrape -Test
#################################################

#@app.route('/')
#def home():
#    return "App is working perfectly"


#################################################
# Flask Routes- Is this call to the database
#   empty before I run the scrape path?
#################################################

#https://www.quora.com/How-can-I-print-the-contents-of-mongoDB-in-a-HTML-page-using-Python

@app.route("/")
def index():
#Needed to make this "index" to pick up index.html file 
#    print("Server received request for 'Home' page...")
    #return "App is working perfectly"
    
    marsquery = marscollection.find_one()

    #https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e
    return render_template("index.html", marsquery=marsquery)
    
    
    #This tested that each component could be called individually
    #return (
        #marsquery["news_title"][0]
        #marsquery["paragraph_text"][0]
        #marsquery["featured_image_url"]
        #marsquery["mars_table"]
        #marsquery["hemheader"][0]
        #marsquery["hemisphere_image_urls"][0]
        #marsquery["hemheader"][1]}
        #marsquery["hemisphere_image_urls"][1]}
        #marsquery["hemheader"][2]
        #marsquery["hemisphere_image_urls"][2]
        #marsquery["hemheader"][3]
        #marsquery["hemisphere_image_urls"][3]
        #)

    # query the  collection
    #cursor = marscollection.find() 
    #for record in cursor: 
    #    print(record)

    #example: classroom = db.classroom.find()

#    my_data = marscollection.find_one()

    #return my_data
    #return "App is working perfectly"
    #return render_template("index.html", data=my_data)
#    return jsonify(my_data)



#################################################
# scrape
#################################################

@app.route("/scrape")
def scrape():
#    print("Server received request for 'scrape' page...")
#
#   #call scrape function
    mars_scrape = scrape_mars.scrape()

    #confirming scrape worked
    #return jsonify(mars_scrape)

    # Insert the dictionary into Mongo
    marscollection.update({}, mars_scrape, upsert=True)
    
    #After loading the data go back to the home route
        #which will then display the data
    return redirect("/")




    #returning the dictionary to check correctly collected
    #return jsonify(mars_scrape)
    #Returned the dictionary
    


#    return redirect("/")







#################################################
# End
#################################################1
if __name__ == "__main__":
    app.run(debug=True)

