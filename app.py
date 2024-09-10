# Import the dependencies.
from flask import Flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
@app.route("/")
def welcome():
    return (
        f"Welcome to your Climate App!<br/>"

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# The input for precipitation route, stations route, and tobs route:
@app.route("/")
def welcome():
    return (
        f"Precipitation Route"
        f"Stations Route"
        f"Tobs Route"
       )

#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    
