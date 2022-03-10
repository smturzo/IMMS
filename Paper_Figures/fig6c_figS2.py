import pandas as pd, numpy as np, seaborn as sns
from matplotlib import rcParams
import matplotlib
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['font.family']='serif'
import matplotlib.pyplot as plt
from scipy import stats
plt.switch_backend('agg')
protein_data_ideal= pd.read_csv('./protein_data_ideal.csv',header=0)
mark_dict={'HM':'o','Abinitio':'^'}
methods_ideal = protein_data_ideal['METHOD']

im_rmsd_ideal = protein_data_ideal['IM-RMSD']
im_tmscore_ideal = protein_data_ideal['IM-TMScore']
#IM-Confident,VoronotaMQ,P3CMQA
im_score_conf_ideal = protein_data_ideal['IM-Confident']
im_min_ideal = min(im_score_conf_ideal)
im_max_ideal = max(im_score_conf_ideal)
voronota_score_conf_ideal = protein_data_ideal['VoronotaMQ']
voro_max_ideal = max(voronota_score_conf_ideal)
voro_min_ideal = min(voronota_score_conf_ideal)
p3cmqa_score_conf_ideal   = protein_data_ideal['P3CMQA']
p3cmqa_max_ideal = max(p3cmqa_score_conf_ideal)
p3cmqa_min_ideal = min(p3cmqa_score_conf_ideal)

im_score_score_norm_ideal     = im_score_conf_ideal/im_min_ideal
voro_score_score_norm_ideal   = voronota_score_conf_ideal
p3cmqa_score_score_norm_ideal = p3cmqa_score_conf_ideal

im_voro_dist_ideal = np.sqrt( (im_score_score_norm_ideal - voro_score_score_norm_ideal)**2 )
im_p3cmqadist_ideal= np.sqrt( (im_score_score_norm_ideal - p3cmqa_score_score_norm_ideal)**2 )

mean_im_voro_dist_ideal = np.around(np.mean(im_voro_dist_ideal),3)
mean_im_p3cmqadist_ideal= np.around(np.mean(im_p3cmqadist_ideal),3)

protein_data_exp= pd.read_csv('./protein_data_exp.csv',header=0)
mark_dict={'HM':'o','Abinitio':'^'}
methods_exp = protein_data_exp['METHOD']

im_rmsd_exp = protein_data_exp['IM-RMSD']
im_tmscore_exp = protein_data_exp['IM-TMScore']
#IM-Confident,VoronotaMQ,P3CMQA
im_score_conf_exp = protein_data_exp['IM-Confident']
im_min_exp = min(im_score_conf_exp)
im_max_exp = max(im_score_conf_exp)
voronota_score_conf_exp = protein_data_exp['VoronotaMQ']
voro_max_exp = max(voronota_score_conf_exp)
voro_min_exp = min(voronota_score_conf_exp)
p3cmqa_score_conf_exp   = protein_data_exp['P3CMQA']
p3cmqa_max_exp = max(p3cmqa_score_conf_exp)
p3cmqa_min_exp = min(p3cmqa_score_conf_exp)


im_score_score_norm_exp     = im_score_conf_exp/im_min_exp
im_score_score_norm_exp[0] = 0.0
voro_score_score_norm_exp   = voronota_score_conf_exp
p3cmqa_score_score_norm_exp = p3cmqa_score_conf_exp


im_voro_dist_exp = np.sqrt( (im_score_score_norm_exp - voro_score_score_norm_exp)**2 )
im_p3cmqadist_exp= np.sqrt( (im_score_score_norm_exp - p3cmqa_score_score_norm_exp)**2 )

mean_im_voro_dist_exp = np.around(np.mean(im_voro_dist_exp),3)
mean_im_p3cmqadist_exp= np.around(np.mean(im_p3cmqadist_exp),3)

plt.figure()
for m, method in enumerate(methods_exp):
        plt.scatter(im_score_conf_exp[m],im_rmsd_exp[m],color='teal',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
for m, method in enumerate(methods_ideal):
        plt.scatter(im_score_conf_ideal[m],im_rmsd_ideal[m],color='slategrey',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
plt.axvline(-2.54, color="black", linestyle="-",alpha=0.70)
plt.axhline(5.5, color="black", linestyle="dotted",alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"RMSD ($\AA$)",fontsize=10)
plt.xlabel(r"IM Confidence Score",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG6/c_i_imconf.png',dpi=1200)
plt.close()

plt.figure()
for m, method in enumerate(methods_exp):
        plt.scatter(im_score_conf_exp[m],im_tmscore_exp[m],color='teal',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
for m, method in enumerate(methods_ideal):
        plt.scatter(im_score_conf_ideal[m],im_tmscore_ideal[m],color='slategrey',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)        
plt.axvline(-2.54, color="black", linestyle="-",alpha=0.70)
plt.axhline(0.5, color="black", linestyle="dotted",alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"TM-Score",fontsize=10)
plt.xlabel(r"IM Confidence Score",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG6/c_ii_imconf.png',dpi=1200)
plt.close()

plt.figure()
for m, method in enumerate(methods_exp):
        plt.scatter(voronota_score_conf_exp[m],im_rmsd_exp[m],color='teal',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
for m, method in enumerate(methods_ideal):
        plt.scatter(voronota_score_conf_ideal[m],im_rmsd_ideal[m],color='slategrey',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)        
plt.axhline(5.5, color="black", linestyle="dotted",alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"RMSD ($\AA$)",fontsize=10)
plt.xlabel(r"Voronota",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG6/c_i_voronota.png',dpi=1200)
plt.close()

plt.figure()
for m, method in enumerate(methods_exp):
        plt.scatter(voronota_score_conf_exp[m],im_tmscore_exp[m],color='teal',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
for m, method in enumerate(methods_ideal):
        plt.scatter(voronota_score_conf_ideal[m],im_tmscore_ideal[m],color='slategrey',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
plt.axhline(0.5, color="black", linestyle="dotted",alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"TM-Score",fontsize=10)
plt.xlabel(r"Voronota",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG6/c_ii_voronota.png',dpi=1200)
plt.close()

plt.figure()
for m, method in enumerate(methods_exp):
        plt.scatter(p3cmqa_score_conf_exp[m],im_rmsd_exp[m],color='teal',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
for m, method in enumerate(methods_ideal):
        plt.scatter(p3cmqa_score_conf_ideal[m],im_rmsd_ideal[m],color='slategrey',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
plt.axhline(5.5, color="black", linestyle="dotted",alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"RMSD ($\AA$)",fontsize=10)
plt.xlabel(r"P3CMQA",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG6/c_i_p3cmqa.png',dpi=1200)
plt.close()

plt.figure()
for m, method in enumerate(methods_exp):
        plt.scatter(p3cmqa_score_conf_exp[m],im_tmscore_exp[m],color='teal',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
for m, method in enumerate(methods_ideal):
        plt.scatter(p3cmqa_score_conf_ideal[m],im_tmscore_ideal[m],color='slategrey',marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
plt.axhline(0.5, color="black", linestyle="dotted",alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"TM-Score",fontsize=10)
plt.xlabel(r"P3CMQA",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG6/c_ii_p3cmqa.png',dpi=1200)
plt.close()


plt.figure()
plt.scatter(im_rmsd_ideal,im_score_score_norm_ideal,s=100,marker='^',edgecolor='black',color='red',alpha=0.85,label='IM')
plt.scatter(im_rmsd_ideal,voro_score_score_norm_ideal,s=100,marker='d',edgecolor='black',color='gold',alpha=0.55,label='Voronota')
plt.scatter(im_rmsd_ideal,p3cmqa_score_score_norm_ideal,s=100,marker='o',edgecolor='black',color='skyblue',alpha=0.35,label='P3CMQA')
plt.scatter(im_rmsd_exp,im_score_score_norm_exp,s=100,marker='^',edgecolor='black',color='red',alpha=0.85,label='IM')
plt.scatter(im_rmsd_exp,voro_score_score_norm_exp,s=100,marker='d',edgecolor='black',color='gold',alpha=0.55,label='Voronota')
plt.scatter(im_rmsd_exp,p3cmqa_score_score_norm_exp,s=100,marker='o',edgecolor='black',color='skyblue',alpha=0.35,label='P3CMQA')
plt.xlabel(r"RMSD",fontsize=10)
plt.ylabel(r"Model Quality Score",fontsize=10)
plt.tight_layout()
plt.savefig('./FIGS2/b_i.png',dpi=1200)
plt.close()

plt.figure()
plt.scatter(im_tmscore_ideal,im_score_score_norm_ideal,s=100,marker='^',edgecolor='black',color='red',alpha=0.85,label='IM')
plt.scatter(im_tmscore_ideal,voro_score_score_norm_ideal,s=100,marker='d',edgecolor='black',color='gold',alpha=0.75,label='Voronota')
plt.scatter(im_tmscore_ideal,p3cmqa_score_score_norm_ideal,s=100,marker='o',edgecolor='black',color='skyblue',alpha=0.65,label='P3CMQA')
plt.scatter(im_tmscore_exp,im_score_score_norm_exp,s=100,marker='^',edgecolor='black',color='red',alpha=0.85,label='IM')
plt.scatter(im_tmscore_exp,voro_score_score_norm_exp,s=100,marker='d',edgecolor='black',color='gold',alpha=0.75,label='Voronota')
plt.scatter(im_tmscore_exp,p3cmqa_score_score_norm_exp,s=100,marker='o',edgecolor='black',color='skyblue',alpha=0.65,label='P3CMQA')
plt.xlabel(r"TM-Score",fontsize=10)
plt.ylabel(r"Model Quality Score",fontsize=10)
plt.tight_layout()
plt.savefig('./FIGS2/b_ii.png',dpi=1200)
plt.close()

sampling_data = pd.read_csv('./summary_of_sampling_ideal',header=0)
x_decoys_list        = sampling_data['No_Decoys']
mean_im_rmsd_list    = sampling_data['IMScore_AvgRMSD']
mean_im_tmscore_list = sampling_data['IMScore_AvgTMScore']

plt.figure()
plt.plot(x_decoys_list,mean_im_rmsd_list,linewidth=3,color='royalblue',alpha=0.80)
plt.xticks()
plt.yticks()
plt.xlabel(r"Number of models generated",fontsize=10)
plt.ylabel(r"Avg RMSD w/ IM score function ($\AA$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIGS2/a_i.png',dpi=1200)
plt.close()

plt.figure()  
plt.plot(x_decoys_list,mean_im_tmscore_list,linewidth=3,color='royalblue',alpha=0.80)
plt.xticks()
plt.yticks()
plt.xlabel(r"Number of models generated",fontsize=10)
plt.ylabel(r"Avg TM-Score w/ IM score function",fontsize=10)
plt.tight_layout()
plt.savefig('./FIGS2/a_ii.png',dpi=1200)
plt.close()