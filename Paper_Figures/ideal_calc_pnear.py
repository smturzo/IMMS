import numpy as np, matplotlib.pyplot as plt, glob, pandas as pd,math
from scipy import stats
def calc_PNear(rmsds, scores,kbT,lam):
        num_sum = 0.0
        denom_sum = 0.0
        for i, score in enumerate(scores):
                rmsd = rmsds[i]
                num_sum += math.exp( -(rmsd**2) / (lam**2) ) * math.exp( -(score)/kbT)
                denom_sum += math.exp( -(score)/kbT)
        if denom_sum != 0.0:
                return num_sum / denom_sum
        else:
                return 0.0

def calc_pnear_of_protein(protein_file,rgscore_file):
	protein_data = pd.read_csv('./Ideal_Score_File_Pnear_Results/'+str(protein_file),header=0)
	rg_data      = pd.read_csv('./Ideal_Score_File_Pnear_Results/'+str(rgscore_file),header=0)
	rg_score = list(rg_data['RG_SCORE'])
	rs_score = list(protein_data['Rosetta_Sc'])
	im_score = list(protein_data['IM_Sc'])
	rmsds    = list(protein_data['Decoy_RMSD'])
	protein_name  = str(protein_file).split('_')[0]
	rs_rmsd_pnear = calc_PNear(rmsds, rs_score, 10, 1) 
	im_rmsd_pnear = calc_PNear(rmsds, im_score, 10, 1)
	rg_rmsd_pnear = calc_PNear(rmsds, rg_score, 10, 1)
	rmsd_pnear_im_by_rs = np.around(im_rmsd_pnear/rs_rmsd_pnear,3)
	rmsd_pnear_im_by_rg = np.around(im_rmsd_pnear/rg_rmsd_pnear,3)
	print(protein_name+','+str(rmsd_pnear_im_by_rs)+','+str(rmsd_pnear_im_by_rg))
	return [rmsd_pnear_im_by_rs,rmsd_pnear_im_by_rg]

file_list   = pd.read_csv('./Ideal_Score_File_Pnear_Results/file_list',header=0)['FILES']
rgfile_list = pd.read_csv('./Ideal_Score_File_Pnear_Results/rgscore_file_list',header=0)['FILES']
rmsd_pnear_rs, rmsd_pnear_rg =[],[]
for i, protein_file in enumerate(file_list):
	calc_pnear = calc_pnear_of_protein(file_list[i],rgfile_list[i])
	pnear_rs   = calc_pnear[0]
	pnear_rg   = calc_pnear[1]
	rmsd_pnear_rs.append(float(pnear_rs))
	rmsd_pnear_rg.append(float(pnear_rg))
rs_rmsd_pnear_avg = np.around(np.mean(np.array(rmsd_pnear_rs)),3)
rg_rmsd_pnear_avg = np.around(np.mean(np.array(rmsd_pnear_rg)),3)
print('AVG-RS-PNEAR,AVG-RG-PNEAR')
print(rs_rmsd_pnear_avg,rg_rmsd_pnear_avg)

