
import os
import argparse
import time
try:
    from geotext import GeoText
except:
    print("Install: pip install geotext")

def mapper(text):
    """ 
    Mapper function that emits geographic locations found in the text.
    
    :param text: str, a string containing the text to be processed
    :return: list of tuples, each tuple contains a geographic location and a count of 1
    """
    # Example set of geographic locations
    # Following are extracted using GeoText library from the target MD&A files.
    # Extracting countries and cities from the text
    geographic_locations = set(['Escondido', 'Fort Wayne', 'Of', 'Federal', 'Miami', 'Same', 'Canada', 'Bay', 'United States', 'McAllen', 'Australia', 'Spain', 'Northampton', 'Manchester', 'Calgary', 'Austin', 'China', 'Allen', 'March', 'Deal', 'Puerto Rico', 'United Kingdom', 'Harrisburg', 'Much', 'Irving', 'Texas', 'Venezuela', 'Fort Worth', 'Wuhan'])

    places = GeoText(text)

    geographic_locations = set()
    for city in places.cities:
        geographic_locations.add(city)

    for country in places.countries:
        geographic_locations.add(country)

    
    # Emit each geographic location found in the text
    return [(location, 1) for location in geographic_locations if location in text]



def reducer(mapped_data):
    """
    Reducer function that aggregates counts for each geographic location.
    
    :param mapped_data: list of tuples, output from the mapper function
    :return: dictionary, with geographic locations as keys and their aggregated counts as values
    """
    counts = {}
    for location, count in mapped_data:
        if location in counts:
            counts[location] += count
        else:
            counts[location] = count

    counts_tuples=[ (loc, counts[loc]) for loc in counts  ]
    

    return counts_tuples

def main():
    parser = argparse.ArgumentParser(description="Process a file.")
    parser.add_argument("file_path", type=str, help="The path to the file to process")

    args = parser.parse_args()


    file_path = args.file_path
    # print("Current File", file_path)
    with open(file_path) as f:
        mdna_text = f.read()
    st_time = time.time()
    map_data = mapper(mdna_text)
    end_time = time.time()

    map_time = end_time - st_time
    st_time = time.time()
    reduced_data = reducer(map_data)

    end_time = time.time()

    reduce_time = end_time - st_time

    print(reduced_data)
    print("Map time(sec):", map_time)
    print("Reduce time(sec):", reduce_time)    

if __name__ == "__main__":
    main()