from individual_res_energies import *
from automated_mcce import * 
import sys
import time

def gather_args():
	'''Parses arguments to run the program
	Notes
	-----
	Inspired by the definition of parse_args() in automated_mcce.py
	'''
	parser = ArgumentParser(description='''Run MCCE on multiple PDB files''')
	required = parser.add_argument_group('''Required arguments (please write absolute
						paths for all locations''')
	required.add_argument('-pdb', '--pdb_location', required = True, type = str,
				help = '''Location where pdb (to be analysed is stored''')
	#required.add_argument('-i', '--res_input_directory', required = True,
	#			 type = str, help = '''The path where all
	#			 residue snippets will be stored. This is also
	#			 the input directory for the automation process.''')
	#required.add_argument('-d', '--automation_results_directory', required = True, 
	#			type=str, help = '''Path where all the results of
	#			automation will be stored''')				
	required.add_argument('-e', '--mcce_directory', required = True, type=str, 
				help='''Path to the directory where MCCE is installed.''')
	required.add_argument('-out', '--output_directory', required = True, type = str,
				help = '''Location where analysis will be stored''')
	optional = parser.add_argument_group('Optional arguments')
	optional.add_argument('-s', '--submit_job', required = False, type = bool, help =
				 '''Flag whether to submit calculation for processing through
				the server. Default is False, meaning the machine will
				run it locally''')
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	argument = gather_args()
	R = res_energies(argument.pdb_location, argument.output_directory)
	#R.generate_res_files(R.out_folder + '/generated_res/')
	#automated_run(argument.output_directory + '/generated_res/', 
	#		argument.output_directory + '/mcce_results/',
	#		argument.mcce_directory)
	R.analyze_fort36(R.out_folder + '/mcce_results/')

	
