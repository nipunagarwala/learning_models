#!/usr/bin/python
import sys
import re 
import numpy as np
np.set_printoptions(threshold='nan')

""" This is the main run method for calling the different machine 
	learning algorithms. This file parses the input file to separate
	the features from the responses and then allows for pre-processing
	in case cross validation is needed.

Usage: python main.py [train_set_file_name] [length_of_train_response_vector]
		[test_set_file_name] [length_of_test_response_vector]

Output: The result of the algorithm chosen (still in progress)

"""


def main():
	args = sys.argv
	trainName = args[1]
	testName = args[3]
	numElemInFeat = int(args[2])
	numElemInResp = int(args[4])
	print "Loading Train file into the program......."
	trainFile= loadData(trainName, numElemInFeat)
	print "Finished loading Train file into the program......."
	print "Loading Test file into the program......."
	testFile = loadData(testName, numElemInResp)
	print "Finished loading Test file into the program......."



""" This method handle the loading of the data from the given file and
	then uses the user defined input to parse the responses from
	the features as separate vectors and matrices, respectively. The
	result is a tuple of (feature,response).
"""
def loadData(fileName, numElem):
	features = []
	response = []
	with open(fileName) as f:
		numLines,count = 0, 0
		for line in f:
			if not numLines:
				try:
					count = int(line)
				except ValueError:
					count = max(len(line.split(' ')),len(line.split(',')))
					print count
			else:
				line = line.replace(',', ' ')
				lineParse = [int(s) for s in line.split(' ')]
				x = lineParse[numElem:count]
				y = lineParse[0:numElem]
				features.append(x)
				response.append(y)

			numLines += 1


	features = np.matrix(features,dtype=int)
	response = np.matrix(response,dtype=int)
	return (features,response)



""" This method can be modified and called upon to do some special
	pre-processing, custom to user needs. As of now, it trivially returns
	the tuple data passed in.
"""
def processData(data):
	return data



if __name__ == "__main__":
    main()

