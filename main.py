from individual_res_energies import *
from automated_mcce import * 

if __name__ == '__main__':
	AMC = MCCEParams('.', calculation_type = 'quick')
	R = res_energies('kevin_original.pdb', AMC)
	#R.generate_res_files()
	R.remove_comments()
	R.generate_res_files()
