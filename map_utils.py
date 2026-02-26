import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="travel_planner")

def get_coordinates(place):
    try:
        location = geolocator.geocode(place)
        return (location.latitude, location.longitude)
    except:
        return None

def create_map(destinations):

    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

    coords_list = []

    for place in destinations:
        coords = get_coordinates(place)
        if coords:
            coords_list.append(coords)
            folium.Marker(coords, popup=place).add_to(m)

    # Draw route line
    if len(coords_list) > 1:
        folium.PolyLine(coords_list, color="blue", weight=3).add_to(m)

    return m