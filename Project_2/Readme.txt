README.txt for MapReduce Script
--------------------------------

Description:
------------
This Python script processes a text file to identify and count geographic locations mentioned in the text. It uses the MapReduce programming model, with a 'mapper' function to emit geographic locations and a 'reducer' function to aggregate these locations and their counts. 

Requirements:
-------------
- Python 3.x
- geotext library

Installation:
-------------
Ensure that Python 3 is installed on your system. You can download it from https://www.python.org/downloads/.

The script requires the 'geotext' library. To install this library, run the following command:
    pip install geotext

Usage:
-----
To run the script, use the following command in the terminal or command prompt:

    python mapreduce.py [file_path]

Replace [file_path] with the path to the text file you want to process. For example:

    python mapreduce.py data/fraud/KHC_MDNA.txt

The script will process the specified file and output the identified geographic locations along with their counts. It will also display the execution time for the mapping and reducing phases.

Output:
-------
The script outputs a list of tuples, each containing a geographic location identified in the text and its count. It also prints the time taken for the map and reduce operations in seconds for statistics.

Example output:
[('United Kingdom', 1), ('Puerto Rico', 1), ...]
Map time(sec): 0.002089
Reduce time(sec): 0.0000031






intel;arch;chsh -s bash; source ~/.bash_profile; conda activate dev
cd /Users/pranayspeed/Downloads/Bhavna-Milmile/
ls
python mapreduce.py
python mapreduce.py data/fraud/KHC_MDNA.txt
python mapreduce.py data/fraud/TANDY_LEATHER_FACTORY_INC.txt