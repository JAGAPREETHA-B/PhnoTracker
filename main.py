import phonenumbers
import opencage
import folium
from testing import num

from phonenumbers import geocoder
cy_number=phonenumbers.parse(num, "CH")
location=geocoder.description_for_number(cy_number, "en")
print(location)

from phonenumbers import carrier
service_num=phonenumbers.parse(num,"RO")
print(carrier.name_for_number(service_num, "en"))

from opencage.geocoder import OpenCageGeocode
key= '32c*******'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mytracker.html")

