from argparse import ArgumentParser
from decimal import *
import pandas as pd
import numpy as np
import os
import sys

def fort36Ave_condensed(fort36_file, out_location):
	df = pd.read_csv(fort36_file,
		sep = "\s+", header = None, usecols = [2, 6, 9],
		names = ['pH', 'E_type', 'E'])
	#print(df)
	AverE_df = df[ df['E_type'] == 'Ave.' ]

	# the agg.function is used on groupby objects and allows for users
	# to combine multiple statistics. For example, we can get values for 
	# both mean and std, grouped by pH, in one line.
	_res = AverE_df.groupby(['pH'], sort=False).agg( ['mean', 'std'] )
	file_location = out_location
	if not os.path.exists(file_location):
		os.makedirs(file_location)
	
	file_name = 'fort.36_condensed.csv'
	
	to_write = os.path.join(file_location, file_name)
	_res.to_csv(to_write)


def fort36Conformers_std(fort36_file):#, out_location):
	#getcontext().prec = 2
	master_df = pd.DataFrame()

	df = pd.read_csv(fort36_file,
		sep = "\s+", header = None, usecols = [0, 1, 2],
		names = ['pH', 'Conformer', 'Occ'])
	
	conformers = set([true_conformer if true_conformer != '=' for true_conformer in df['Conformer'].values])
	df['Occ'] = [float(string[4:len(string) + 1]) if string[0:3] == 'occ'
		else float(string) for string in df['Occ'].values]
 
	for conformer in sorted(conformers):
		df_conformer = df[ df['Conformer'] == str(conformer) ]
		to_write = df_conformer.groupby(['pH'], 
			sort = False).agg('mean')
		to_write.columns = [str(conformer)]

		print(to_write)
		to_write[conformer] = ['%.3f' % round(val,3) for val in 
			to_write[conformer]]
	
		master_df = master_df.join(pd.DataFrame(to_write), 
			how = 'right')

	master_df.index.name = 'ph'
	
	master_df.transpose().to_csv('fort99', sep = ' ')
	
	# IMPROVEMENTS NEEDED: CONVERT ALL FLOATS TO 2 DECIMAL PLACES
	# THIS WILL IMPROVE THE CLEANLINESS OF THE FILE

	

def ask_arguments():
	parser = ArgumentParser(description = '''Analyze values in fort36, 
		calculates mean of energies at each pH by default. Can
		process more values by if required by user''')
	required = parser.add_argument_group('''Required arguments
		please enter absolute paths where possible''')
	# required arguments below:
	required.add_argument('-f', '--fort36_location', required = True, 
		type = str, help = '''Location of fort36 file to be 
		analyzed''')
	required.add_argument('-out', '--output_location', required = True,
		type = str, help = '''Location of FOLDER containing output
		csv files''')
	# optional arguments below:
	optional = parser.add_argument_group('''Optional arguments''')
	optional.add_argument('-stdev', '--standard_deviation', 
		required = False, type = bool, help = '''Flag indicating
		whether stdev should be calculated. False by default''')
	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = ask_arguments()
	#fort36Ave_condensed(args.fort36_location, args.output_location)
	fort36Conformers_std(args.fort36_location)



