import os
import requests
import datetime
from dbmodels import City, WeatherAttributes, insert_city, insert_weather_event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
Perform a get request to the weather API, 
then load the results in the database
"""
def main():
    # Load API key and City_ID from environment variables
    weather_database = f"{os.path.abspath('.')}\weather.sqlite"
    weather_api_key = os.getenv('weather_api_key')
    city_id = os.getenv('weather_api_my_city_id')

    # Create the engine to open the connection to the weather DB
    engine = create_engine(f'sqlite:///{weather_database}', echo=False)

    # Get current weather event from API
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={weather_api_key}')
    weather_event = r.json()

    # Pass the weather event JSON into a city and weather object
    c = insert_city(weather_event)
    w = insert_weather_event(weather_event)

    # Unpack the weather event to create a weather database object
    newEvent = WeatherAttributes(**w.__dict__)

    # Create a session with the database
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # Check if the current city is in the database, if it isn't, then add it in.
    city_already_added = session.query(City).filter_by(id=weather_event['id']).first()
    if not city_already_added:
        newCity = City(**c.__dict__)
        session.add(newCity)
    else:
        session.rollback()
    # Add the weather event into the database, then commit the object
    session.add(newEvent)
    session.commit()


if __name__ == "__main__":
    main()