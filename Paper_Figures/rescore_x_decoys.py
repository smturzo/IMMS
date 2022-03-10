import pandas as pd, numpy as np, matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['font.family']='serif'
plt.switch_backend('agg')

def get_lowest_scoring_metric(score,metric):
        return metric[score.index(min(score))]

def get_rmsd_tmsc_of_x_decoys(dataset,protein_list,x_decoys_list):
	print('Protein_Name,Rosetta_Lscore_RMSD,IM_Lscore,RMSD,Rosetta_Lscore_TMscore,IM_Lscore_TMscore,X_Decoys')
	mean_r_rmsd_list, mean_im_rmsd_list    = [], []
	mean_r_tmscore_list, mean_im_tmscore_list = [], [] 
	for x, x_decoys in enumerate(x_decoys_list):
		x_decoys = int(x_decoys)
		rmsd_r_list, rmsd_im_list       = [], []
		tmscore_r_list, tmscore_im_list = [], []
		for p, prot in enumerate(protein_list):
			prot_file = pd.read_csv(str(prot),sep=',',header=0)
			r_score    = list(prot_file['Rosetta_Sc'][0:x_decoys]) 
			im_r_score = list(prot_file['IM_Sc'][0:x_decoys])
			rmsds      = list(prot_file['Decoy_RMSD'][0:x_decoys])
			tmscores   = list(prot_file['Decoy_TMsc'][0:x_decoys])
			protf      = str(prot.split('/')[-1].split('_')[0])
			r_lowest_scoring_rmsd     = get_lowest_scoring_metric(r_score,rmsds)
			im_lowest_scoring_rmsd    = get_lowest_scoring_metric(im_r_score,rmsds)
			r_lowest_scoring_tmscore  = get_lowest_scoring_metric(r_score,tmscores)
			im_lowest_scoring_tmscore = get_lowest_scoring_metric(im_r_score,tmscores)
			rmsd_r_list.append(r_lowest_scoring_rmsd)
			rmsd_im_list.append(im_lowest_scoring_rmsd)
			tmscore_r_list.append(r_lowest_scoring_tmscore)
			tmscore_im_list.append(im_lowest_scoring_tmscore)
			print(protf,',',str(r_lowest_scoring_rmsd),',',str(im_lowest_scoring_rmsd),',',str(r_lowest_scoring_tmscore),',',str(im_lowest_scoring_tmscore),',',str(x_decoys))
		mean_r_rmsd     = np.mean(np.array(rmsd_r_list))
		mean_im_rmsd    = np.mean(np.array(rmsd_im_list))
		mean_r_tmscore  = np.mean(np.array(tmscore_r_list))
		mean_im_tmscore = np.mean(np.array(tmscore_im_list))
		mean_r_rmsd_list.append(mean_r_rmsd)
		mean_im_rmsd_list.append(mean_im_rmsd)
		mean_r_tmscore_list.append(mean_r_tmscore)
		mean_im_tmscore_list.append(mean_im_tmscore)
	with open(f'./summary_of_sampling_{dataset}','w+') as samplingsummary:
		samplingsummary.write('No_Decoys,RScore_AvgRMSD,IMScore_AvgRMSD,RScore_AvgTMScore,IMScore_AvgTMScore\n')
		for d, decoy in enumerate(x_decoys_list):
			samplingsummary.write(f'{decoy},{mean_r_rmsd_list[d]},{mean_im_rmsd_list[d]},{mean_r_tmscore_list[d]},{mean_im_tmscore_list[d]}\n')

ideal_path = pd.read_csv('./Ideal_Score_File_Pnear_Results/file_list',header=0)['FILES']
x_decoys_list = np.linspace(100,10000,100)
get_rmsd_tmsc_of_x_decoys('ideal',ideal_path,x_decoys_list)





