import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Float, ForeignKey
from sqlalchemy.orm import sessionmaker
from dataclasses import dataclass


# where to store the database
path = os.path.abspath('.')
weather_database = f'{path}\weather.sqlite'

# Create the database engine and SQLAlchemy base
engine = create_engine(f'sqlite:///{weather_database}', echo=False)
Base = declarative_base()


# Create Python data classes to make it easier/cleaner to put data 
# into SQLAlchemy objects.  Currently have a City and Weather Attribute class
"""
Database Objects
"""
@dataclass
class City(Base):
    __tablename__ = 'city'
    
    #id = Column(Integer, Sequence('city_id_seq'), primary_key=True)
    id = Column(Integer, primary_key=True)
    city_name = Column(String(50))
    country_name = Column(String(50))
    longitude = Column(Float)
    latitude = Column(Float)

@dataclass
class WeatherAttributes(Base):
    __tablename__ = 'weatherattributes'
    
    id = Column(Integer, Sequence('weather_id_seq'), primary_key=True)
    city_id = Column(Integer, ForeignKey("city.id"))
    
    dt = Column(Integer)
    sunrise_dt = Column(Integer)
    sunset_dt = Column(Integer)
    temp_current = Column(Float)
    temp_max = Column(Float)
    temp_min = Column(Float)
    humidity = Column(Integer)
    visibility = Column(Float)
    pressure = Column(Integer)
    wind_deg = Column(Integer)
    wind_spd = Column(Float)
    clouds = Column(Integer)
    snow_1h = Column(Float)
    snow_3h = Column(Float)
    rain_1h = Column(Float)
    rain_3h = Column(Float)


"""
Python Classes to be unpacked into database objects
"""
@dataclass
class insert_city:
    """
    Create an instance of a city.  Can be unpacked into a City database object.
    Input: A JSON dictionary of a weather API call
    """
    def __init__(self, weather_dict):
        self.city_name = weather_dict['name']
        self.id = weather_dict['id']
        self.country_name = weather_dict['sys']['country']
        self.longitude = weather_dict['coord']['lon']
        self.latitude = weather_dict['coord']['lat']
    
@dataclass
class insert_weather_event:
    """
    Create an instance of a weather event.
    Input: A JSON dictionary of a weather API call
    """
    def __init__(self, weather_dict):
        self.dt = weather_dict.get('dt')
        self.city_id = weather_dict.get('id')
        self.sunrise_dt = weather_dict.get('sys').get('sunrise')
        self.sunset_dt = weather_dict.get('sys').get('sunset')
        self.visibility = weather_dict.get('visibility')
        self.humidity = weather_dict.get('main').get('humidity')
        self.pressure = weather_dict.get('main').get('pressure')
        self.temp_current = weather_dict.get('main').get('temp')
        self.temp_max = weather_dict.get('main').get('temp_min')
        self.temp_min = weather_dict.get('main').get('temp_max')
        self.wind_deg = weather_dict.get('wind').get('deg')
        self.wind_spd = weather_dict.get('wind').get('speed')
        self.clouds = weather_dict.get('clouds').get('all')
        if isinstance(weather_dict.get('snow'), dict):
            self.snow_1h = weather_dict.get('snow').get('1h')
            self.snow_3h = weather_dict.get('snow').get('3h')
        if isinstance(weather_dict.get('rain'), dict):
            self.rain_1h = weather_dict.get('rain').get('1h')
            self.rain_3h = weather_dict.get('rain').get('3h')


#Base.metadata.create_all(engine)

# Run this .py script to create the database if it doesn't already exist
def main():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()
