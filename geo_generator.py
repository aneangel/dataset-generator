from opencage.geocoder import OpenCageGeocode
from apiKey import API_Key
# import time


geoCoder = OpenCageGeocode(API_Key)

cities_dict = {'cities': ['San Jose', 'San Francisco', 'Sunnyvale', 'Campbell','Berkeley', 'Oakland',
                          'Saratoga', 'Cupertino', 'Palo Alto', 'Los Altos', 'Milpitas', 'Fremont', 'Santa Clara',
                          'San Mateo', 'Alameda', 'Walnut Creek', 'Fremont', 'Sacramento', 'Los Angeles', 'Santa Cruz',
                          'Gilroy', 'Daly city', 'Concord', 'Stockton', 'Dublin', 'Danville', 'Hayward', 'Glroy', 'Lafayette',
                          'Livermore', 'Menlo Park', 'Los Gatos', 'Moraga', 'Mountain View', 'Morgan Hill', 'Pleasant Hill',
                          'Richmond', 'Redwood City', 'San Bruno', 'Pleasanton', 'Piedmont', 'Sonoma', 'Union City', 'Los Altos Hills',
                          'Dixon', 'Dublin', 'Half Moon Bay', 'Burlingame', 'Antioch', 'Atherton']}

list_lat = []
list_long = []

counter = 0

# results = geocoder.geocode(query)
# print(results)

coordList = []

for city in cities_dict['cities']:
    counter += 1
    query = city + ',' + 'California'
    results = geoCoder.geocode(query)
    coordList.append(results[0]['geometry'])
    print('{0} found location data'.format(city))


print(coordList)
print(coordList[0])
