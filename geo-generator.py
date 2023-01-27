from opencage.geocoder import OpenCageGeocode

key = 'bcd6b1bdf8694408b584ba1132a42fad'

geocoder = OpenCageGeocode(key)
query = 'San Fransico, California'
results = geocoder.geocode(query)

print(results)



