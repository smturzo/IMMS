import pandas as pd, numpy as np

protein_list= pd.read_csv('start_relax',header=0,sep='\s+')['PDBID']

with open('relax_start','w+') as file_relax_start:
	for p, prot in enumerate(protein_list):
		file_relax_start.write('relax.linuxgccrelease -in:file:s '+str(prot)+' -in:file:fullatom -relax:quick -nstruct 1 -out:prefix r_ &\n')



