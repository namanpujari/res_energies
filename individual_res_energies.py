import numpy as np 
import os.path
import sys
import pandas as pd
import numpy as np

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
	
	def __init__(self, protein_data_file, output_pathname):
		sys.dont_write_bytecode = True
		self.original = protein_data_file # will be required in later methods
		#self.AMC = automate_object # reference to the automating class
		self.out_folder = output_pathname

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
		
		if not os.path.exists(self.out_folder):
			os.makedirs(self.out_folder)


		self.nocmts_filename = self.out_folder + '/data_no_comments.pdb'
		# saving pdb without comments
		write_data = file[is_atom[0]:(is_atom[-1] + 1)]
		out = open(self.nocmts_filename, 'w')
		out.write(''.join(write_data))
		out.close()

	def generate_res_files(self, masterfolder_destination):
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

		# new method using python inbuilt open function
		newpath = masterfolder_destination
		if not os.path.exists(newpath): # checks whether existing dir present
			os.makedirs(newpath)
		save_path = masterfolder_destination

		lines = open(self.nocmts_filename, 'r').readlines()
		for i in range(len(self.cutoff_list) - 1):
			outputData = lines[self.cutoff_list[i]:self.cutoff_list[i+1]]

			file_name = os.path.join(save_path, 'res' + str(i+1) + '.pdb')
			produced_pdb = open(file_name, 'w')
			#   produced_pdb = open('res' + str(i+1) + '.pdb', 'w') 	   
			produced_pdb.write(''.join(outputData))
			produced_pdb.close()
	
	def analyze_fort36(self, mcceres_location)
        	'''Goes into the results folder and extracts data
        	from fort.36 files for each residue (if present).
	        '''
	        masterfolder = mcceres_location  # preferably absolute path
	        fort36_list = []
	        subfolder_list = os.listdir(masterfolder) # this name will
	        # be changed according to the argument given by the
	        # user
	        energies = np.zeros((15, 1))
	        for subfolder_index in range(3):
	                subfolder_destination = masterfolder + '/' + subfolder_list[subfolder_index]
	                file_list = os.listdir(subfolder_destination)
	                for file_index in range(len(file_list)):
	                        if(file_list[file_index] == 'fort.36'):
	                                try:
	                                        df = pd.read_csv(subfolder_destination + '/' + file_list[file_index],
	                                                sep="\s+", header=None, usecols=[2, 6, 9],
	                                                names=['pH', 'E_type', 'E'] )
	                                except:
	                                        print( "Could not read the input \
	                                                file: " + file_list[file_index])
	
	                                AverE_df = df[df['E_type'] == 'Ave.']
	                                AverE_df_by_pH = AverE_df.groupby(['pH'], sort=False).mean().E
					df_savepath = self.out_folder + '/aveEnergies_for_each_residue'
					if not os.path.exists(df_savepath):
						os.makedirs(df_savepath)
					AverE_df_by_pH.to_csv(df_savepath + '/aveEnergy_res' + subfolder_index + '.csv')
	                                vals = AverE_df_by_pH.values.reshape(len(AverE_df_by_pH.values), 1)
        	                        energies = energies + vals

	        frame_to_write = pd.DataFrame(energies, index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
		frame_to_write.index.name = 'pH'
	        frame_to_write.columns = ['Energy']
	        frame_to_write.to_csv(self.out_folder + '/final_result.csv')

		
		
