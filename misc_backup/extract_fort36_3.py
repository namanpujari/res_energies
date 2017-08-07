import os
import numpy as np
import pandas as pd

def analyze_fort36():
        '''Goes into the results folder and extracts data
        from fort.36 files for each residue (if present).
        '''
        masterfolder = 'results_mcce' # preferably absolute path
        fort36_list = []
        subfolder_list = os.listdir(masterfolder) # this name will
        # be changed according to the argument given by the
        # user
	energies = np.zeros(15, 1)
        for subfolder_index in range(10):
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
                                ph_index = AverE_df_by_pH.index
                                #print('>>>>>>>>>>>>>>>>>>>THIS IS FOR ' + subfolder_list[subfolder_index])
                                #print(AverE_df_by_pH)
                                #print(AverE_df_by_pH.values)
                                vals = AverE_df_by_pH.values.reshape(len(AverE_df_by_pH.values), 1)
				energies = energies + vals






if __name__ == '__main__':
        analyze_fort36()

