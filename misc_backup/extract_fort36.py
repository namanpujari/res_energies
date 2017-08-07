import os
import numpy as np
import pandas as pd

def analyze_fort36():
	'''Goes into the results folder and extracts data
	from fort.36 files for each residue (if present). 
	'''
	masterfolder = 'result' # preferably absolute path
	fort36_list = []
	subfolder_list = os.listdir(result) # this name will
	# be changed according to the argument given by the 
	# user
	for subfolder in subfolder_list:
		file_list = os.listdir(masterfolder + '/' + subfolder)
		for file_index in range(len(file_list)):
			if(file_list[file_index].endswith('.36'):
				fort36_list.append(file+'_res'+file_index)
	return fort36_list

if __name__ == '__main__':
	x = analyze_fort36()
	print(x)

				
		
		
	
