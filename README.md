# res_energies
Python programs that process pdb files to generate individual residue energies of an entire protein structure. Can be used in theory to calculate the energy of an unfolded protein.

### PLEASE NOTE
Added an elementary way of efficiently running the code. When first running, set the `mcce_result_present` status to `False`. A bunch of statements indicating that the residues have been sent to the cluster will appear. Check qstat multiple times and wait till all jobs are complete. Then change `mcce_result_present` to `True` and run the the thing again with the same command in terminal. Check the output folder. It should have everything.

#### Usage
---
Typing `python main.py --help` in the command line gives the following:
```
usage: main.py [-h] -pdb PDB_LOCATION -e MCCE_DIRECTORY -out OUTPUT_DIRECTORY
               [-s SUBMIT_JOB]

Run MCCE on multiple PDB files

optional arguments:
  -h, --help            show this help message and exit

Required arguments (please write absolute
                                                paths for all locations:
  -pdb PDB_LOCATION, --pdb_location PDB_LOCATION
                        Location where pdb (to be analysed is stored
  -e MCCE_DIRECTORY, --mcce_directory MCCE_DIRECTORY
                        Path to the directory where MCCE is installed.
  -out OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
                        Location where analysis will be stored

Optional arguments:
  -s SUBMIT_JOB, --submit_job SUBMIT_JOB
                        Flag whether to submit calculation for processing
                        through the server. Default is False, meaning the
                        machine will run it locally

```
Please note that `SUBMIT_JOB` is not implemented as of yet.

#### What it does
---

1. Grabs the targeted pdb, and strips it of comments (basically any line not classified) as `ATOM` or `HETATM`.
2. Using a splitting algorithm defined in `individual_res_energies.py` it produces all the residues as their own pdb files 
3. Using `automated_mcce.py`, it runs MCCE on each, individual residue.
4. Analyses all the fort.36 (wherever present) for all residue and finds average at each pH. Sums the values for all residues and provides a neat .csv for the final result. Csv files are also produced for each individual residues average energie for reference. 

#### Example
---
An example, and how the `out_gfp46` folder was created in this repository. 

1. Set `mcce_results_present` (in main.py) to `False`, then...
```
python main.py -pdb /home/naman/res_energies/gfp46.pdb -e /home/mcce/mcce3.5/ -out /home/naman/res_energies/out_gfp46
```
2. Wait till `qstat` returns nothing
3. Set `mcce_results_present` (in main.py) to `True`, then the same command as in step 1...
```
python main.py -pdb /home/naman/res_energies/gfp46.pdb -e /home/mcce/mcce3.5/ -out /home/naman/res_energies/out_gfp46
```

	


