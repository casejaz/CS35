#
# hw3pr3.py 
#
# Visualizing your own data with matplotlib...
#
# Here, you should include functions that produce two visualizations of data
#   of your own choice. Also, include a short description of the data and
#   the visualizations you created. Save them as screenshots or as saved-images,
#   named datavis1.png and datavis2.png in your hw3.zip folder.
# 
# Gallery of matplotlib examples:   http://matplotlib.org/gallery.html
#
# List of many large-data sources:    https://docs.google.com/document/d/1dr2_Byi4I6KI7CQUTiMjX0FXRo-M9k6kB2OESd7a2ck/edit    
#     and, the birthday data in birth.csv is a reasonable fall-back option, if you'd like to use that...
#          you could create a heatmap or traditional graph of birthday frequency variations over the year...
#

"""
Short description of the two data visualizations...


    1. Visualize the birthday data in a heated map.
    2. Visualize the battle values, ID and types of Pokemon


"""
import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib
import matplotlib.patches as mpatches
import csv
"""
From: birth.csv given in the starter files
"""
def birthvis():
	"""
	Visualize the birthday data in a heated map.
	"""
	# read in the birth data
	filename = "births.csv"
	try:
		csvfile = open(filename, newline='' )        # open for reading
		csvrows = csv.reader( csvfile )              # creates a csvrows object
		numberL = []

		for row in csvrows:                          # into our own Python data structure
			if 'month' not in row[0]:
				numberL.append(float(row[2]))
		del csvrows                                  # acknowledge csvrows is gone!
		csvfile.close()                              # and close the file
	except FileNotFoundError as e:
		print("File not found: ", e)
		return []
	# monthL = monthL[1:]
	# dayL = dayL[1:]
	# numberL = numberL[1:]

	column_lables = [x for x in range(1,32)]
	row_lables = [y for y in range(1,13)]

	# data matrix
	data = np.matlib.zeros((12,31))
	data = data.tolist()
	fig, ax = plt.subplots()


	# write the data
	idx = 0
	for month in range(12):
		for day in range(31):
			data[month][day] = numberL[idx]
			idx += 1
	data = np.array(data)
	heatmap = ax.pcolor(data, cmap=plt.cm.Blues, alpha=10000)

	# Format
	fig = plt.gcf()
	fig.suptitle('Birthday Heated Map', fontsize=16, fontweight='bold')
	fig.set_size_inches(20, 8)

	ax.set_yticks(np.arange(data.shape[0])+1, minor=False)
	ax.set_xticks(np.arange(data.shape[1])+1, minor=False)

	# Plot the heated map
	plt.show()



"""
From: pokemon.csv http://srea64.github.io/msan622/project/dataset.html
"""

def pokemonvis():
	"""
	Visualize the race values and categories of Pokemon
	"""
	filename = "pokemon.csv"

	# the color dictionary
	colorD = {}
	colorD['grass'] = '#52BE80'
	colorD['poison'] = '#6C3483'
	colorD['fire'] = '#E74C3C'
	colorD['flying'] = '#2874A6'
	colorD['dragon'] = '#154360'
	colorD['water'] = '#5DADE2'
	colorD['bug'] = '#82E0AA'
	colorD['normal'] = '#EDBB99'
	colorD['electric'] = '#F4D03F'
	colorD['ground'] = '#9C640C'
	colorD['fairy'] = '#F5B7B1'
	colorD['fighting'] = '#A93226'
	colorD['psychic'] = '#BB8FCE'
	colorD['rock'] = '#A04000'
	colorD['ice'] = '#AED6F1'
	colorD['ghost'] = '#BB8FCE'
	colorD['dark'] = '#273746'
	colorD['steel']= '#34495E'
	fig = plt.figure()
	keys = list(colorD.keys())
	handles = []
	for i in range(len(keys)):
		color1 = colorD[keys[i]]
		key = keys[i]
		handle = mpatches.Patch(color = color1, label = key)
		handles.append(handle)
	try:
		csvfile = open(filename, newline='' )        # open for reading
		csvrows = csv.reader( csvfile )              # creates a csvrows object
		idL = []
		totalvL = []
		colorL = []
		for row in csvrows:                          # into our own Python data structure
			if 'id' not in row[0]: 
				idL.append(int(row[0]))
				totalvL.append(int(row[3]))
				color = (row[2].split())[0]
				colorL.append(colorD[color.lower()])
			if len(idL) > 721:
				break
		del csvrows                                  # acknowledge csvrows is gone!
		csvfile.close()                              # and close the file
	except FileNotFoundError as e:
		print("File not found: ", e)

	axes = plt.gca()
	axes.set_xlim([0, 900])
	plt.scatter(idL, totalvL, s = 21, c = colorL)


	handle1 = handles[0]
	handle2 = handles[1]
	handle3 = handles[2]
	handle4 = handles[3]
	handle5 = handles[4]
	handle6 = handles[7]
	handle7 = handles[8]
	handle8 = handles[9]
	handle9 = handles[10]
	handle10 = handles[11]
	handle11 = handles[12]
	handle12 = handles[13]
	handle13 = handles[14]
	handle14 = handles[15]
	handle15 = handles[16]
	handle16 = handles[17]

	fig.suptitle('Pokemon Total Battle Value, ID and Types', fontsize=16, fontweight='bold')
	plt.xlabel('Pokemon ID')
	plt.ylabel('Total Battle Value')
	plt.legend(handles = [handle1, handle2, handle3, handle4, handle5, handle6, handle7, handle8, handle9, handle10, handle11, handle12, handle13, handle14, handle15, handle16])
	plt.show()



birthvis()
#pokemonvis()
