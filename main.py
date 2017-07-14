from individual_res_energies import *
from automated_mcce import * 
import sys

def gather_args():
	'''Parses arguments to run the program
	Notes
	-----
	Inspired by the definition of parse_args() in automated_mcce.py
	'''
	parser = ArgumentParser(description='''Run MCCE on multiple PDB files''')
	required = parser.add_argument_group('''Required arguments (please write absolute paths for all locations''')
	required.add_argument('-pdb', '--pdb_location', required = True, type = str,
				help = '''Location where pdb (to be analysed is stored''')
	required.add_argument('-i', '--res_input_directory', required = True,
				 type = str, help = '''the path where all
				 residue snippets will be stored. This is also
				 the input directory for the automation process.''')
	required.add_argument('-d', '--automation_results_directory', required = True, 
				type=str, help = '''Path where all the results of
				automation will be stored''')				
	required.add_argument('-e', '--mcce_directory', required = True, type=str,
                          help='''path to the directory where MCCE is installed.''')
	optional = parser.add_argument_group('Optional arguments')
	optional.add_argument('-s', '--submit_job', required = False, type = bool, help =
				 '''Flag whether to submit calculation for processing through
				the server. Default is False, meaning the machine will
				run it locally''')
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	sys.dont_write_bytecode = True
	argument = gather_args()
	R = res_energies(argument.pdb_location)
	R.generate_res_files(argument.res_input_directory)
	automated_run(argument.res_input_directory, 
			argument.automation_results_directory,
			argument.mcce_directory)
	R.analyze_fort36(argument.automation_results_directory)

	
