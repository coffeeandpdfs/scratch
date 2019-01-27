# Scratch
Small projects or scratch applications.

## Weather Project
The weather folder contains an app to create a database to store weather events.  After the database is created, an another program will retrieve weather events via GET requests to a weather API, transorm the JSON objects, then insert the data into the database.  weather_models.py will need to be run first to create the database.  weather_api_request.py can then be run to grab the data.  A windows batch file can be paired with  Windows task scheduler to automate kicking off the API requests.

The iPython notebook was the first scratch file for the project.  The code was then moved to the individual files for practice.

Next steps/enhancements:
 - Log duplicate entries, successful requests, and failed requests
    - Can be in the SQL database and/or a simple log file
 - Use Alembic for SQL migrations
 - Visualize the weather event data
 - Move the API to a Linux AWS instance
    - Use CRON instead of a bat file and task scheduler
 - Move the project into a Flask environment to manage the project
    - Data feed into the database
    - Data retrieval for displaying events over a web page
    - Add additional event entries besides weather requests