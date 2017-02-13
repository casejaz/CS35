#
# starting examples for cs35, week2 "Web as Input"
#

import requests
import string
import json

######################################################################
#
#   How to run my program:
#   run main_pr1(), and "multicity_distances.html" will show in the 
#   same folder
#
#   I did extra credit:
#   1. I add appropriate columns, rows and html/css style to the table
#   2. I posted the table to github repo, see the link below:
#            
#
#######################################################################
"""
Examples you might want to run during class:

Web scraping, the basic command (Thanks, Prof. Medero!)

#
# basic use of requests:
#
url = "https://www.cs.hmc.edu/~dodds/demo.html"  # try it + source
result = requests.get(url)
text = result.text   # provides the source as a large string...

#
# try it for another site...
#

#
# let's demo the weather example...
#
url = 'http://api.wunderground.com/api/49e4f67f30adb299/geoloookup/conditions/q/Us/Ca/Claremont.json' # JSON!
       # try it + source
result = requests.get(url)
data = result.json()      # this creates a data structure from the json file!
# What type will it be?
# familiarity with dir and .keys() to access json data...

#
# let's try the Open Google Maps API -- also provides JSON-formatted data
#   See the webpage for the details and allowable use
#
# Try this one by hand - what are its parts?
# http://maps.googleapis.com/maps/api/distancematrix/json?origins=%22Claremont,%20CA%22&destinations=%22Seattle,%20WA%22&mode=%22walking%22
#
# Take a look at the result -- imagine the structure of that data... That's JSON! (Sketch?)
#
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Problem 1 starter code
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
#
#
def google_distances_api_scrape(filename_to_save="distances.json"):
    """ a short function that shows how
        part of Google Maps' API can be used to
        obtain and save a json file of distances data...
    """
    url="http://maps.googleapis.com/maps/api/distancematrix/json"

    city1="Claremont,CA"
    city2="Seattle,WA"
    my_mode="walking"

    inputs={"origins":city1,"destinations":city2,"mode":my_mode}

    result = requests.get(url,params=inputs)
    data = result.json()
    print("data is", data)

    # save this json data to file
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save, "written.")
    # no need to return anything, since we're better off reading it from file!
    return


def google_distances_api_process(filename_to_read = "distances.json"):
    """ a function with examples of how to manipulate json data --
        here the data is from the file scraped and saved by
        google_distances_api_starter()
    """
    f = open( filename_to_read, "r" )
    string_data = f.read()
    data = json.loads( string_data )
    print("data (not spiffified!) is\n\n", data, "\n")

    print("Accessing its components:\n")

    row0 = data['rows'][0]
    print("row0 is", row0, "\n")

    cell0 = row0['elements'][0]
    print("cell0 is", cell0, "\n")

    distance_as_string = cell0['distance']['text']
    print("distance_as_string is", distance_as_string, "\n")

    # here, we may want to continue operating on the whole json dictionary
    # so, we return it:
    return data


#
# multicity_distance_scrape
#
def multicity_distance_scrape( Origins, Dests, filename_to_save="multicity.json" ):
    """ a function with examples of how to manipulate json data --
        here the data is from the file scraped and saved by
        google_distances_api_starter()
    """
    url="http://maps.googleapis.com/maps/api/distancematrix/json"

    # parse the Origins and Dests
    Origins_s = ""
    Dests_s = ""
    for idx in range(len(Origins)):
        Origins_s += Origins[idx]
        if idx != (len(Origins) - 1):
            Origins_s += ' | '

    for idx in range(len(Dests)):
        Dests_s += Dests[idx]
        if idx != (len(Dests) - 1):
            Dests_s += ' | '
    print (Origins_s)
    print (Dests_s)
    # get data from API
    inputs={"origins":Origins_s, "destinations":Dests_s}

    result = requests.get(url,params=inputs)
    data = result.json()
    print (data)

    # save this json data to file
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save, "written.")

    multicity_distance_process()

    # no need to return anything, since we're better off reading it from file!
    return

#
# multicity_distance_process
#
def multicity_distance_process(filename_to_read = "multicity.json"):
    """ a function with examples of how to manipulate json data --
        here the data is from the file scraped and saved by
        multicity_distance_scrape()
    """
    f = open( filename_to_read, "r" )
    string_data = f.read()
    data = json.loads( string_data )
    print("data (not spiffified!) is\n\n", data, "\n")

    print("Accessing its components:\n")


    # first row
    html_string = '<table id="table1">\n'
    html_string += '<tr>\n'
    html_string += '<td> Origins <\td> \n'
    for dest in data['destination_addresses']:
        html_string += '<td>'
        html_string += dest
        html_string += '</td>\n'
    html_string += '</tr>\n'

    # following rows, one row per origin
    for idx in range(len(data['origin_addresses'])):
        html_string += '<tr>\n'
        html_string += '<td>'
        html_string += data['origin_addresses'][idx]
        html_string += '</td>\n'
        row = data['rows'][idx]
        for idx in range(len(data['destination_addresses'])):
            html_string += '<td>'
            dist = row['elements'][idx]['distance']['text']
            html_string += dist
            html_string += '</td>\n'
        html_string += '</tr>\n'

    # write the table into html
    decoration ="<style> \n table { \n color: black; \n font-family: arial, sans-serif; \n border-collapse: collapse; \n width: 100%;\n}\ntd, th {\n border: 1px solid #dddddd;\n text-align: left;\npadding: 8px;}\n"
    decoration += "tr:nth-child(even) {\nbackground-color: #dddddd;\n}\ntr:nth-child(even) {\nbackground-color: #dddddd;\n}\np {\ncolor: dimgray;\ntext-align: left;\n}\n</style>\n"
    html_string_new = decoration + html_string
    html_file = open("multicity_distances.html", "w")
    html_file.write(html_string_new)
    html_file.close()

    return data




#
# a main function for problem 1 (the multicity distance problem)
#
def main_pr1():
    """ a top-level function for testing things! """
    # these were the cities from class:
    # Origins = ['Pittsburgh,PA','Boston,MA','Seattle,WA']  # starts
    # Dests = ['Claremont,CA','Atlanta,GA']         # goals
    #
    # Origins are rows...
    # Dests are columns...
    Origins = ['Pittsburgh,PA','Boston,MA','Seattle,WA']
    Dests = ['Claremont,CA','Atlanta,GA']
    multicity_distance_scrape(Origins, Dests)
    pass
main_pr1()







# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Problem 3 -- please take a look at problem3_example.py for an example!
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#
# This problem is very scalable -- start with a small prediction task
#   (serious or not...) that involves analyzing at least two sites...
#
# Feel free to find your own json-based APIs -- or use raw webpages
#   and BeautifulSoup! (This is what the example does...)
#
