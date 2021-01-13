from math import radians, cos, sin, asin, sqrt, ceil

from aiogram import types

from data.locations import Shops
from utils.misc import show_on_gmaps

R = 6378.1


def calc_distance(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return ceil(km)


def choose_shortest(location: types.Location):
    distances = list()
    for shop_name, shop_location in Shops:
        distances.append((shop_name,
                          calc_distance(location.latitude, location.longitude,
                                        shop_location["lat"], shop_location["lon"]),
                          show_on_gmaps.show(**shop_location),
                          shop_location
                          ))
    return sorted(distances, key=lambda x: x[1])[:2]
