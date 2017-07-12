from individual_res_energies import *
from automated_mcce import * 



def do_automation():
	arguments = parse_args()
	automated_run(arguments.input_directory,
		 arguments.destination_directory,
		 arguments.mcce_directory)


if __name__ == '__main__':
	R = res_energies('kevin_original.pdb')
	R.generate_res_files()
	do_automation()

	
