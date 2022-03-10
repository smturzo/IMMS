import pandas as pd, numpy as np, seaborn as sns
from matplotlib import rcParams
import matplotlib
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['font.family']='serif'
import matplotlib.pyplot as plt
from scipy import stats
plt.switch_backend('agg')

rs_all_scores  =[]
im_all_scores_0,im_all_scores_15,im_all_scores_30=[],[],[]

all_rmsds_0,all_rmsds_15,all_rmsds_30=[],[],[]
all_tmscore_0,all_tmscore_15,all_tmscore_30=[],[],[]

noise_0_data =pd.read_csv('./FIGS3/ideal_60_protein_rescore_csv_list_noise_0')['FINALSCFILE']
noise_15_data=pd.read_csv('./FIGS3/ideal_60_protein_rescore_csv_list_noise_15')['FINALSCFILE']
noise_30_data=pd.read_csv('./FIGS3/ideal_60_protein_rescore_csv_list_noise_30')['FINALSCFILE']

with open('./FIGS3/score_and_noise.csv','w+') as all_score_noise:
	all_score_noise.write('IM-SCORE,NOISE\n')

	for i, data_file in enumerate(noise_0_data):
		file_data_noise_0  = pd.read_csv(str(noise_0_data[i]),header=0)
		file_data_noise_15 = pd.read_csv(str(noise_15_data[i]),header=0)
		file_data_noise_30 = pd.read_csv(str(noise_30_data[i]),header=0)
	
		im_noise_0_score = file_data_noise_0['IM_Sc']
		im_noise_15_score = file_data_noise_15['IM_Sc']
		im_noise_30_score = file_data_noise_30['IM_Sc']

		rmsds_noise_0 = file_data_noise_0['Decoy_RMSD']
		rmsds_noise_15 = file_data_noise_15['Decoy_RMSD']
		rmsds_noise_30 = file_data_noise_30['Decoy_RMSD']

		tmsc_noise_0 = file_data_noise_0['Decoy_TMsc']
		tmsc_noise_15 = file_data_noise_15['Decoy_TMsc']
		tmsc_noise_30 = file_data_noise_30['Decoy_TMsc']

		for j, dat_points in enumerate(im_noise_0_score):
			im_all_scores_0.append(im_noise_0_score[j])
			all_rmsds_0.append(rmsds_noise_0[j])
			all_tmscore_0.append(tmsc_noise_0[j])

			im_all_scores_15.append(im_noise_15_score[j])
			all_rmsds_15.append(rmsds_noise_15[j])
			all_tmscore_15.append(tmsc_noise_15[j])

			im_all_scores_30.append(im_noise_30_score[j])
			all_rmsds_30.append(rmsds_noise_30[j])
			all_tmscore_30.append(tmsc_noise_30[j])

			all_score_noise.write(str(im_noise_0_score[j])+',0\n')
			all_score_noise.write(str(im_noise_15_score[j])+',15\n')
			all_score_noise.write(str(im_noise_30_score[j])+',30\n')

plt.figure()
plt.scatter(all_tmscore_0,im_all_scores_0,s=120,color='skyblue',marker='o',alpha=0.55)
plt.xlabel('TM-Score',fontsize=10)
plt.ylabel(r'$IM_{Score}$',fontsize=10)
plt.tight_layout()
plt.savefig('./FIGS3/a_i.png',dpi=1200)
plt.close()
plt.figure()
plt.scatter(all_tmscore_15,im_all_scores_15,s=120,color='darkorange',marker='o',alpha=0.55)
plt.xlabel('TM-Score',fontsize=10)
plt.ylabel(r'$IM_{Score}$',fontsize=10)
plt.tight_layout()
plt.savefig('./FIGS3/a_ii.png',dpi=1200)
plt.close()
plt.figure()
plt.scatter(all_tmscore_30,im_all_scores_30,s=120,color='mediumaquamarine',marker='o',alpha=0.55)
plt.xlabel('TM-Score',fontsize=10)
plt.ylabel(r'$IM_{Score}$',fontsize=10)
plt.tight_layout() 
plt.savefig('./FIGS3/a_iii.png',dpi=1200)
plt.close()
noise_data = pd.read_csv('./noise_data_for_ideal_dataset.csv')
plt.figure()
ax= sns.violinplot(x="Noise",y="IM-TMScore",data=noise_data,split=True,cut=0,inner="box")#
ax.set(xlabel='')
ax.set(ylabel='')
plt.ylabel(r"TM-Score of predicted structures",fontsize=10)
plt.xlabel(r"% Noise simulated for ideal IM data",fontsize=10)
plt.xticks()
plt.yticks()
plt.tight_layout()
plt.savefig('./FIGS3/b.png',dpi=1200)
plt.close()
