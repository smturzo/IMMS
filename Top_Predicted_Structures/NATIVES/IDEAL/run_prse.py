import pandas as pd, numpy as np

def run_prse():
        per_res_solv_expo = 'per_residue_solvent_exposure.linuxgccrelease -sphere_method -in:file:s ../'
        f = open('./native_p/native_p_run_prse.in','w')
        path='/home/cbc-lindert-group1/data/turzo.1/CCS/CATH/NEW_IDEAL_DATASET/PROTEINS/BEST_PREDS/NATIVES/IDEAL/'
        print(str(path))
        pdblist= pd.read_csv(str(path)+'pdblist2',header=None)[0]
        for pdb, pdbs in enumerate(pdblist):
                f.write('cd '+str(path)+'native_p/ && '+str(per_res_solv_expo)+str(pdbs)+' > '+str(path)+'native_p/'+str(pdbs.split('_')[1][0:4])+'.per_res_solv_expo\n')
        f.close()

run_prse()
