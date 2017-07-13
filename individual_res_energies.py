import numpy as np 
import os.path

class res_energies(object):
	''' Class that calculated the energies of individial residues of a given protein

	Parameters
	----------
	protein_data : str 
		A file name representing all the values contained within a protein pdb
		file. Will be used to slice the data according to where the residues
		end
	automate_object : 'MCCEParams' object
		Inherited object that allows access to the automate_mcce.py methods. 

	Notes
	-----
	The class inherits automate_mcce.py by Kamran Haider. The primary purpose 
	of this inheritance is to run the MCCE program through the hundreds and 
	hundreds of individual res_x.pdb files. MCCE usually provides a file named
	fort36 which displays the energies of a proton at different pH configurations.
	The average energies at all the pHs will be combined for all residues, and will
	be stored in a master_fort36.txt file. 
	'''
	
	def __init__(self, protein_data_file):
		self.original = protein_data_file # will be required in later methods
		#self.AMC = automate_object # reference to the automating class

	def remove_comments(self):
		'''Grabs a pdb file and analyzes it, removing all comments and producing
		a pdb file starting with the first atom and ending with the last. 
		'''
		words = []
		file = open(self.original, 'r').readlines() # creates a list of all lines
		for line in file:
			to_append = [word for word in line.split()]
			words.append(to_append) # enumerates as a multidimensional list containing
			# lines and all words in those lines
		# advantage here is that the word 'ATOM' will always be the first word in 
		# all of the lines
		i = 0 # iterator along lines
		is_atom = []
		for i in range(len(file)):
			if(words[i][0] == 'ATOM'):
				is_atom.append(i)

		self.nocmts_filename = 'data_no_comments.pdb'
		# saving pdb without comments
		write_data = file[is_atom[0]:(is_atom[-1] + 1)]
		out = open(self.nocmts_filename, 'w')
		out.write(''.join(write_data))
		out.close()

	def generate_res_files(self):
		''' Enumerates self.cutoff_list, which is used in later methods to 
			generate res_x.pdb files

		Notes
		-----
		Utilises a small utility function that is located at the end of the 
		class definition.
		'''
		self.remove_comments()
		self.data = np.genfromtxt(self.nocmts_filename, dtype = int, usecols = (5))
		self.cutoff_list = [0] # initialize the cutoff list with the first line

		for i in range(len(self.data) - 1):
			current_res = self.data[i]
			#print('current residue number is ' + str(self.data[i]))
			if(self.data[i+1] != current_res):
				#print('the next residue number is ' + str(self.data[i+1]))
				self.cutoff_list.append(i+1)
		self.cutoff_list.append(len(self.data))

		# using the cutoff list, a folder called "Generated Residues" is created.
		# This hold all of the individual resX.pdb files which will be later
		# processed using MCCE.

		# new method using python inbuilt open function
		import os.path
		newpath = "generated_residues"
		if not os.path.exists(newpath): # checks whether existing dir present
			os.makedirs(newpath)
		save_path = "generated_residues"

		lines = open(self.nocmts_filename, 'r').readlines()
		for i in range(len(self.cutoff_list) - 1):
			outputData = lines[self.cutoff_list[i]:self.cutoff_list[i+1]]

			file_name = os.path.join(save_path, 'res' + str(i+1) + '.pdb')
			produced_pdb = open(file_name, 'w')
			#   produced_pdb = open('res' + str(i+1) + '.pdb', 'w') 	   
			produced_pdb.write(''.join(outputData))
			produced_pdb.close()
	

		
		
