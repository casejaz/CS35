#
# Questions:
# (1) a first-letter-counter that is weighted
# (2) a last-letter-counter that is weighted
# (3) a twice-letter-counter that is weighted
#
# How to run my project:
# main(), then "frequencies.csv" and "letter_frequencies.html" will show up in
# the folder.
#
# ECs:
# ****I wrote the whole page directly to a file using Python.
# 1. I added "letter_frequencies.html" file and the Python code that helped
#    create it to my repository. link: https://github.com/casejaz/CS35/hw1
# 2. I added the graphical elements - different colors for vowels and consonants
#
#
import csv
from collections import *
#
# readcsv is a starting point - it returns the rows from a standard csv file...
#
def readcsv( csv_file_name ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( csv_file_name, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []



#
# write_to_csv shows how to write that format from a list of rows...
#  + try   write_to_csv( [['a', 1 ], ['b', 2]], "smallfile.csv" )
#
def write_to_csv( list_of_rows, filename ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")
        for row in list_of_rows:
            filewriter.writerow( row )
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")


#
# csv_to_html_table
#
#   Shows off how to create an html-formatted string
#   Some newlines are added for human-readability...
#
def csv_to_html_table(csv_file_name):
    """ csv_to_html_table
           + a function that returns an html-formatted string
        Run with
           + result = csv_to_html_table( "example_chars.csv" )
        Then run
           + print(result)
    """
    all_rows = readcsv(csv_file_name)
    html_string = ''
    for item in all_rows:
        if len(item) == 1:
            if all_rows.index(item) == 0:
                title = '<p>' + item[0] + '</p>\n'
                html_string += title
                html_string += '<table>\n'    # start with the table tag
            else:
                html_string += '</table>\n'   # end of one table
                title = '<p>' + item[0] + '</p>\n'
                html_string += title
                html_string += '<table>\n'    # start with the table tag
        else:
            html_string += '<tr>\n'
            for cell in item:
                if item[0] in ['a','o','e','i','u']:
                    html_string += '<td style="color:red">'
                    html_string += cell
                    html_string += '</td>\n'
                else:
                    html_string += '<td style="color:blue">'
                    html_string += cell
                    html_string += '</td>\n'

            html_string += '</tr>\n'
    html_string += '</table>\n'
    return html_string

#
# weighted counting of first letters
#
def WCount():
    """ returns a list that contains results of
        weighted letter analysis counts from
        the file wds.csv
    """
    LoR = readcsv("wds.csv")  # List of rows
    #print ("LoR is", LoR)
    fcounts = defaultdict(int)
    lcounts = defaultdict(int)
    trcounts = defaultdict(int)
    for Row in LoR:
        word = str(Row[0])                # the word is at index 0
        num1 = float(Row[1])              # its num occurences is at index 1
        first_letter = word[0]            # the first letter of the word
        last_letter = word[-1]            # the last letter of the word

        # twice in a word
        tDict = {}                         # keep track of all letters in word
        letters = []                       # all letters that show up twice
        for letter in word:
            if letter.isalpha():
                if letter.lower() not in tDict:
                    tDict[letter.lower()] = 1
                else:
                    tDict[letter.lower()] += 1

        for key in tDict.keys():
            if tDict[key] == 2:
                letters.append(key)
        for tletter in letters:
            trcounts[tletter.lower()] += num1

        if first_letter.isalpha():
            # add the relative frequencies of words
            fcounts[first_letter.lower()] += num1
        if last_letter.isalpha():
            lcounts[last_letter.lower()] += num1
    content = []
    # first-letter frequency
    content.append(["first-letter frequency"])
    content1 = fcounts
    content1 = sorted(content1.items(), key = lambda k:k[0], reverse = False)
    for item1 in content1:
        content.append(item1)

    # last-letter frequency
    content.append(["last-letter frequency"])
    content2 = lcounts
    content2 = sorted(content2.items(), key= lambda k:k[0], reverse = False)
    for item2 in content2:
        content.append(item2)

    # twice-letter frequency
    content.append(["twice-letter frequency"])
    content3 = trcounts
    content3 = sorted(content3.items(), key= lambda k:k[0], reverse = False)
    for item3 in content3:
        content.append(item3)

    return content

#
# write_html
#
#   directly writes the information into html file "letter_frequencies.html"
#
def write_html(html_string):
    """write_html takes as
       +input: an html_string that contains the html
               information in string format
       Run with
       +write_html(html_string)
    """
    decoration ="<style> \n table { \n color: black; \n font-family: arial, sans-serif; \n border-collapse: collapse; \n width: 100%;\n}\ntd, th {\n border: 1px solid #dddddd;\n text-align: left;\npadding: 8px;}\n"
    decoration += "tr:nth-child(even) {\nbackground-color: #dddddd;\n}\ntr:nth-child(even) {\nbackground-color: #dddddd;\n}\np {\ncolor: dimgray;\ntext-align: left;\n}\n</style>\n"
    html_string_new = decoration + html_string
    html_file = open("letter_frequencies.html", "w")
    html_file.write(html_string_new)
    html_file.close()

#
# Run main() to execute my project!
#
def main():

    write_to_csv(WCount(), "frequencies.csv")
    write_html((csv_to_html_table("frequencies.csv")))

    return
main()
