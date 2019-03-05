import os
import requests
import datetime
from dbmodels import City, WeatherAttributes, insert_city, insert_weather_event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
Perform a get request to the weather API, then load the results in the database
"""
cities = {
    'Austin': 4671654,
    'Boston': 4930956,
    'Chicago': 4887398,
    'Denver': 5419384,
    'Erie': 5188843,
    'New York': 5128581,
    'Pittsburgh': 5206379,
    'Raleigh': 4487042,
    'Tahoe': 5599665
    }


def retrieve_city_data(city_id=None, weather_api_key=None):
    # Get current weather event from API
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={weather_api_key}')
    weather_event = r.json()

    # Pass the weather event JSON into a city and weather object
    c = insert_city(weather_event)
    w = insert_weather_event(weather_event)

    # Unpack the weather event to create a weather database object
    new_weather = WeatherAttributes(**w.__dict__)
    new_city = City(**c.__dict__)

    return weather_event, new_weather, new_city


def commit_data(sesh=None, weather_event=None, new_weather=None, new_City=None):
    # Check if the current city is in the database, if it isn't, then add it in.
    city_already_added = sesh.query(City).filter_by(id=weather_event['id']).first()
    if not city_already_added:
        sesh.add(new_City)
    else:
        sesh.rollback()
    # Add the weather event into the database, then commit the object
    sesh.add(new_weather)
    sesh.commit()


def main():
    # Load API key and City_ID from environment variables
    weather_database = f"{os.path.abspath('.')}\weather.sqlite"
    WeatherApiKey = os.getenv('weather_api_key')
    #city_id = os.getenv('weather_api_my_city_id')

    # Create the engine to open the connection to the weather DB
    engine = create_engine(f'sqlite:///{weather_database}', echo=False)
    # Create a session with the database
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    for city, cityid in cities.items():
        print(f"Starting API GET request for {city}")
        try:
            newEvent, newWeather, newCity = retrieve_city_data(cityid, WeatherApiKey)
        except Exception as e:
            print(f'\t{e}')
        print(f"Starting SQL calls for {city}")
        try:
            commit_data(session, newEvent, newWeather, newCity)
        except Exception as e:
            print(f'\t{e}')


if __name__ == "__main__":
    main()