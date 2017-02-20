#
# hw3pr2.py 
#
# Person or machine?  The rps-string challenge...
#
# This file should include your code for 
#   + extract_features( rps ),               returning a dictionary of features from an input rps string
#   + score_features( dict_of_features ),    returning a score (or scores) based on that dictionary
#   + read_data( filename="rps.csv" ),       returning the list of datarows in rps.csv
"""
How to run my program:
main()
Then the results will be updated in rps.csv

Short description 
(1) the features you compute for each rps-string 
	Feature 1: two same letters, "rr" "ss" and "pp"
	Feature 2: consecutive letters with length of at least 3 ('r' or 's' or 'p') * n, n>=3
	Feature 3: maximum deviation of each letter from the average. max(s_D, r_D, p_D)
    
(2) how you score those features and how those scores relate to "humanness" or "machineness"
	If humannness have higher scores:
	Feature 1: -20 each, since humans are less likely to press two same letters with high 
			   frequency
	Feature 2: +5 each, since machines are less likely to press a lot of same consecutive 
			   letters
	Feature 3: +100 each, since machines choose letter uniformly and randomly

~~~~~~~~~~~~~~~~I did extra credit~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(1) batch_play(rps1, rps2) function is Line 202
(2) rps string wins most is the 58th one 
sprsprsprsprpprsprprpsrpsprsprpsrpsprpsprsprpsrpsprsprpsprsprsprpsrpsprspsrppsrpsrpsprsprpsprsprpsprsprpsprpsprpsrpsprpsprsprpsrprpprsprprsprsprprspprprprpspspspprprpsprsprpsprpsprsprpsprpsrpsprpsprsprpspsrprpsrpprpsprspsrpsrpsrpsprppsrprsp 
(3) It is a human-generated according to my algorithm


"""


# Here's how to machine-generate an rps string.
# You can create your own human-generated ones!

import random
import csv
from collections import defaultdict


def gen_rps_string( num_characters ):
    """ return a uniformly random rps string with num_characters characters """
    result = ''
    for i in range( num_characters ):
        result += random.choice( 'rps' )
    return result

# Here are two example machine-generated strings:
rps_machine1 = gen_rps_string(200)
rps_machine2 = gen_rps_string(200)
# print those, if you like, to see what they are...

#
# extract_features( rps ):   extracts features from rps into a defaultdict
#
def extract_features(rps):
	"""
	- Takes in a single rps string named, naturally, rps
	- Creates a default dictionary that counts features
	- Return that dictionary of features

	"""

	# feature dictionary
	features_D = defaultdict(float)

	# Humans are less likely to give two same letters 
	number_of_ss_es = rps.count('ss')
	number_of_pp_es = rps.count('pp')
	number_of_rr_es = rps.count('rr')
	features_D['ss'] = number_of_ss_es
	features_D['pp'] = number_of_pp_es
	features_D['rr'] = number_of_rr_es

	# Machines are less likely to give long number of consectuive letters
	number_of_long_es = 0
	for count in range(3,10):
		longs = rps.count('s'*count)
		number_of_long_es += longs
		longr = rps.count('r'*count)
		number_of_long_es += longr
		longp = rps.count('p'*count)
		number_of_long_es += longp
	features_D['long'] = number_of_long_es

	# Machines choose letters uniformly and randomly
	number_of_s_es = rps.count('s')
	s_D = abs(number_of_s_es - len(rps)/3)
	number_of_r_es = rps.count('r')
	r_D = abs(number_of_r_es - len(rps)/3)
	number_of_p_es = rps.count('p')
	p_D = abs(number_of_p_es - len(rps)/3)
	features_D['deviation'] = max(s_D, r_D, p_D)

	return features_D



#
# score_features( dict_of_features ): returns a score based on those features
#
def score_features(dict_of_features):
    """ 
    - Takes in a dictionary of features
    - Returns a single floating-point number that "scores" how human-made or 
      how machine-made those features are.
	Algorithm: Humanness has higher scores
	two same letters: 
	-20 each, since humans are less likely to press two same letters 
	with high frequency

	consecutive letters with length of at least 3: 
	+5 each, since machines are less likely to press a lot of same 
	consecutive letters

	maximum deviation of each letter from the average:
	+100 each, since machines choose letter uniformly and randomly

    """
    d = dict_of_features
    score = 0.0

    # two same letters:
    score = (d['ss'] + d['rr'] + d['pp']) * (-20.0)

    # consecutive letters with length of at least 3
    score = d['long'] * 5.0

    # maximum deviation of each letter from the average
    score = d['deviation'] * 100.0

    return score   # return a humanness or machineness score

#
# read_data(filename="rps.csv"):   gets all of the data from "rps.csv"
#
def read_data(filename="rps.csv" ):
    """
    - open the file of filename and extracts all of its data
    - return a list of all of the rps strings in that csv file
    """
    # you'll want to look back at reading a csv file!
    List_of_rows = []   # for now...
    try:
        csvfile = open(filename, newline='' )        # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        				                            

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []

    for dpt in all_rows:
    	List_of_rows.append(dpt[3])

    return List_of_rows, all_rows

#
# write_data(filename="rps.csv", List_of_rows): write the result
#
def write_data(List_of_rows, all_rows,filename="rps.csv"):
	"""
	- takes in a list of all rps and all data
	- write the score and decision in target csv file
	"""
	scoreL = []
	decisionL = []

	# Calulate the scores
	for rps in List_of_rows:
		score = score_features(extract_features(rps))
		scoreL.append(score)

	# Write to the file
	with open(filename,"w", newline='') as datacsv:
		csvwriter = csv.writer(datacsv,dialect=("excel"))
		for row in all_rows:
			# write the score
			idx = all_rows.index(row)
			row[1] = scoreL[idx]

			# write the decision
			if scoreL[idx] > 1000:
				row[2] = 'human'
			else:
				row[2] = 'machine'
			csvwriter.writerow(row)


	return


def batch_play(rps1, rps2):

	"""
	Takes two rps-strings and "plays them against each other" by comparing the gestures
	Return 1 if rps1 wins more often, 2 if rps2 wins more often and 0 if it's a draw
	"""

	dicW = {'r':'s', 's':'p', 'p':'r'}
	rps1S = 0
	rps2S = 0
	for idx in range(min(len(rps1),len(rps2))):
		if rps1[idx] == rps2[idx]:
			None
		elif dicW[rps1[idx]] == rps2[idx]:
			rps1S += 1
		else:
			rps2S += 1
	if rps1S > rps2S:
		return 1
	elif rps1S < rps2S:
		return 2
	else:
		return 0

def win_Most(List_of_rows):
	scoreL = [0 for i in range(len(List_of_rows))]
	for p1 in range(len(List_of_rows)):
		for p2 in range(len(List_of_rows)):
			if batch_play(List_of_rows[p1], List_of_rows[p2]) == 1:
				scoreL[p1] += 1
	idx = scoreL.index(max(scoreL))
	return List_of_rows[idx], idx

def main():
	data = read_data()
	List_of_rows = data[0]
	all_rows = data[1]
	write_data(List_of_rows, all_rows)

	# find out the rps that wins most
	rps = (win_Most(List_of_rows))[0]
	score = score_features(extract_features(rps))
	print (score > 1000)

main()

