# How to run my project:
# 1. Have "annotation.csv" in the folder.
# 2. run main(), "annotations.html" will show up in the folder.
# 
# 3. In "annotations.html", above is the annotated version with annotated 
# words in red, and below is the substituted version with substituted words in 
# blue. 
#
# ECs:
#  
#  
#  I did extra credit and submitted hw1ec.txt. 
#  github link: https://github.com/casejaz/CS35/hw1
#
#
import csv
from collections import *

text = """
Do not go gentle into that good night,
Old age should burn and rave at close of day;
Rage, rage against the dying of the light.

Though wise men at their end know dark is right,
Because their words had forked no lightning they
Do not go gentle into that good night.

Good men, the last wave by, crying how bright
Their frail deeds might have danced in a green bay,
Rage, rage against the dying of the light.

Wild men who caught and sang the sun in flight,
And learn, too late, they grieved it on its way,
Do not go gentle into that good night.

Grave men, near death, who see with blinding sight
Blind eyes could blaze like meteors and be gay,
Rage, rage against the dying of the light.
And you, my father, there on the sad height,

Curse, bless, me now with your fierce tears, I pray.
Do not go gentle into that good night.
Rage, rage against the dying of the light.
"""

#
# readcsv returns the rows from a standard csv file...
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
# annotate_dictionary_creator
#
#    Create a word by word annotation dictionary by reading csv file
#
#
def annotate_dictionary_creator(csv_file_name):
    """ annotate_dictionary_creator takes as
        + input: csv_file_name, the name of a csv file
        and returns:
        + annotations, a word by word annotation dictionary
    """
    annotations = defaultdict(str)
    all_rows = readcsv(csv_file_name)
    for item in all_rows:
        annotations[item[0]] = item[1]
    return annotations



#
# annotate_text
#
#   A word-by-word text-annotater and annotates a dictionary
#
#
def annotate_text( text, annotations ):
    """ this is a word-by-word text-annotater. It annotates the dictionary
        according to an annotation csv. It changes "\n" to "<br>" and alters
        the color of annotated word.
        annotate_text takes as:
            + input: text (a string), annotations (an annotation dictionary);
        and returns an html_string
    """
    new_html_string = "<p> Annotated </p> \n"
    text = text.split()
    for word in text:    # word-by-word
        if (not word[-1].isalpha()) and word[0].lower(): # handle new lines...
            # we use Python's cool "text-formatting" ability...
            new_w = word + "<br>"
        elif word in annotations.keys():  # handle annotations
            new_w = '<span style="color:{0}; title = "{2}""">{1}</span>'.format("red", word, annotations[word])
        else:
            new_w = word

        # add the new word, new_w
        new_html_string += new_w
        new_html_string += " "
    new_html_string += "<p> Substituted </p> \n"
    for word in text:    # word-by-word
        if (not word[-1].isalpha()) and word[0].lower(): # handle new lines...
            # we use Python's cool "text-formatting" ability...
            new_w = word + "<br>"
        elif word in annotations.keys():  # handle annotations
            new_w = '<span style="color:{0}; title = "{2}""">{2}</span>'.format("blue", word, annotations[word])
        else:
            new_w = word
        # add the new word, new_w
        new_html_string += new_w
        new_html_string += " "

    # finished!
    return new_html_string
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
    decoration = "<title>Do not go gentle into that good night</title>"
    html_string_new = decoration + html_string
    html_file = open("annotation", "w")
    html_file.write(html_string_new)
    html_file.close()

#
# Run main() to execute my project!
#
def main():
    annotations = annotate_dictionary_creator("annotation.csv")
    html_string = annotate_text(text, annotations)
    write_html(html_string)
    return

main()
