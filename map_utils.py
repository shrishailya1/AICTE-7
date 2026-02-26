from geopy.geocoders import Nominatim
import pandas as pd
import time

def get_coordinates(city_list):

    geolocator = Nominatim(user_agent="travel_planner")
    locations = []

    for city in city_list:
        try:
            location = geolocator.geocode(city)
            if location:
                locations.append({
                    "latitude": location.latitude,
                    "longitude": location.longitude
                })
                time.sleep(1)
        except:
            pass

    return pd.DataFrame(locations)
