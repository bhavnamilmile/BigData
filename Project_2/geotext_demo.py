
import os
from geotext import GeoText


dir_loc = "data/fraud"
dir_files = os.listdir(dir_loc)
print(dir_files)

cities = set()
country= set()
for dir_file in dir_files:
    file_full = os.path.join(dir_loc, dir_file)
    print(dir_file)
    with open(file_full) as f:
        sample_text = f.read()

        places = GeoText(sample_text)
        # print("\t\tcities",places.cities)
        # print("\t\tcountry",places.countries)

        for city in places.cities:
            cities.add(city)
        for cntry in places.countries:
            country.add(cntry)


all_loc = cities
for cntry in country:
    all_loc.add(cntry)
print(all_loc)