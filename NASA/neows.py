import requests
import pandas as pd 

url = 'https://api.nasa.gov/neo/rest/v1/feed'

# Request parameters
params = {
    "start_date": "2024-03-01",
    "end_date": "2024-03-07",
    "api_key": "Of6yxD2w6qv9Oty85r0kgvtahWLEKSe9bPCZwXNa"
}

# Authenticated API request
response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json() # Grab the json data

    neos = data['near_earth_objects']

    # print(neos)
    print(neos.keys())
    print(neos['2024-03-05'])
    print(neos['2024-03-05'][0].keys())

    # id = 
    # name = 
    # absolute_magnitude_h = 
    # ed_km_min = 
    # ed_km_max = 
    # ed_miles_min = 
    # ed_miles_max = 
    # ed_ft_min = 
    # ed_ft_max = 
    # hazardous = 
    # close_approach_date = 












