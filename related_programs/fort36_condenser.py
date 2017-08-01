from argparse import ArgumentParser
import pandas as pd
import numpy as np
import os
import sys

def fort36Ave_condensed(fort36_file, out_location):
	df = pd.read_csv(fort36_file,
		sep = "\s+", header = None, usecols = [2, 6, 9],
		names = ['pH', 'E_type', 'E'])
	AverE_df = df[ df['E_type'] == 'Ave.' ]
	#_res = AverE_df.groupby(['pH'], sort=False).agg( {"E": {"mean": np.mean, "stdev": np.std}} )

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

def fort36Conformers_std(fort36_file, out_location):
	pass

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
	fort36Ave_condensed(args.fort36_location, args.output_location)
