Landscape Code Health: [![Code Health](https://landscape.io/github/namanpujari/res_energies/master/landscape.svg?style=flat)](https://landscape.io/github/namanpujari/res_energies/master)

# res_energies
Python programs that process pdb files to generate individual residue energies of an entire protein structure. Can be used in theory to calculate the energy of an unfolded protein.

### PLEASE NOTE
DUE TO THE FACT THAT THE ANALYSIS RUNS IMMEDIATELY AFTER MCCE AUTOMATION IS SUBMITTED, BUT NOT COMPLETE (COMPLETE MEANS FINISHING THE RUN OF MCCE ON EACH RESIDUE), THERE IS OFTEN AN ERROR THAT IS ALWAYS THE RESULT OF THE ANALYSIS NOT GIVING TIME FOR THE AUTOMATION TO FULLY PROVIDE ITS RESULTS FOR EACH RESIDUE FILE. A QUICK SOLUTION TO THIS IS TO ADD A `time.sleep(30)` LINE IN THE SCRIPT OF MAIN.PY (INCLUDED) BETWEEN THE MCCE AUTOMATION AND ANALYSIS. 

#### Usage
---
Typing `python main.py --help` in the command line gives the following:
```
usage: main.py [-h] -pdb PDB_LOCATION -i RES_INPUT_DIRECTORY -d
               AUTOMATION_RESULTS_DIRECTORY -e MCCE_DIRECTORY -out
               OUTPUT_DIRECTORY [-s SUBMIT_JOB]

Run MCCE on multiple PDB files

optional arguments:
  -h, --help            show this help message and exit

Required arguments (please write absolute paths for all locations:
  -pdb PDB_LOCATION, --pdb_location PDB_LOCATION
                        Location where pdb (to be analysed is stored
  -i RES_INPUT_DIRECTORY, --res_input_directory RES_INPUT_DIRECTORY
                        the path where all residue snippets will be stored.
                        This is also the input directory for the automation
                        process.
  -d AUTOMATION_RESULTS_DIRECTORY, --automation_results_directory AUTOMATION_RESULTS_DIRECTORY
                        Path where all the results of automation will be
                        stored
  -e MCCE_DIRECTORY, --mcce_directory MCCE_DIRECTORY
                        path to the directory where MCCE is installed.
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
An example, and how the `generated_residue`, `mcce_results`, and `analysis` folders were created in this repository. 

`python main.py -pdb /home/naman/res_energies/gfp46.pdb -i /home/naman/res_energies/generated_residues -d /home/naman/res_energies/mcce_results -e /home/mcce/mcce3.5/ -out /home/naman/res_energies/analysis`

	


