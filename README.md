# sqlalchemy-challenge

* Please note that I was not able to complete the 2nd part of the assigment regarding Designing Your Own Climate App. It became a bit overwhelming to navigate this section of the assignment and was ultimately not able to establish a successful Flask application with functional routes.

# SQLAlchemy Homework - Surfs Up!

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## Part 1 - Climate Analysis and Exploration

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

* Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.

* Use the SQLAlchemy 'create_engine()' function to connect to your SQLite database.

* Use the SQLAlchemy 'automap_base()' function to reflect your tables into classes, and then save references to the classes named station and measurement.

* Link Python to the database by creating a SQLAlchemy session.
  
* Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

### Precipitation Analysis

* Find the most recent date in the dataset.

* Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

* Select only the "date" and "prcp" values.

* Load the query results into a Pandas DataFrame. Explicitly set the column names.

* Sort the DataFrame values by "date".

* Plot the results by using the DataFrame plot method, as the following image shows:
  
* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations (that is, the stations that have the most rows). To do so, complete the following steps:

  * List the stations and observation counts in descending order.

  * Answer the following question: which station id has the greatest number of observations?

* Design a query to retrieve the last 12 months of temperature observation data (tobs). To do so, complete the following steps:

  * Filter by the station that has the greatest number of observations.
    
  * Query the previous 12 months of TOBS data for that station.

  * Plot the results as a histogram with bins=12, as the following image shows:
 
  * Close your session.

- - -

## Part 2 - Design Your Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use FLASK to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
