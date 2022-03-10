import pandas as pd, numpy as np, seaborn as sns
from matplotlib import rcParams
import matplotlib
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['font.family']='serif'
import matplotlib.pyplot as plt
plt.switch_backend('agg')
protein_data= pd.read_csv('./protein_data_exp.csv',header=0)
mark_dict={'HM':'o','Abinitio':'^'}
buff_dict={'He':'crimson','N2':'powderblue'}
methods = protein_data['METHOD']
rs_rmsd = protein_data['RS-RMSD']
im_rmsd = protein_data['IM-RMSD']
rs_tmscore = protein_data['RS-TMScore']
im_tmscore = protein_data['IM-TMScore']
rg_rmsd    = protein_data['MinRG-RMSD']
rg_tmscore = protein_data['MinRG-TMScore']
buffer_gas = protein_data['Buffer-Gas']

plt.figure()
for m, method in enumerate(methods):
	plt.scatter(rs_rmsd[m],im_rmsd[m],color=buff_dict.get(buffer_gas[m]),marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
plt.plot(rs_rmsd,rs_rmsd,color='black',linewidth=3,alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"RMSD w/ IM score function ($\AA$)",fontsize=10)
plt.xlabel(r"RMSD w/ RS score function ($\AA$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG5/b_i.png',dpi=1200)
plt.close()

plt.figure()
for m, method in enumerate(methods):
        plt.scatter(rs_tmscore[m],im_tmscore[m],color=buff_dict.get(buffer_gas[m]),marker=mark_dict.get(method),s=100,edgecolor='black',alpha=0.65)
plt.plot(rs_tmscore,rs_tmscore,color='black',linewidth=3,alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"TM-Score w/ IM score function",fontsize=10)
plt.xlabel(r"TM-Score w/ RS score function",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG5/b_ii.png',dpi=1200)
plt.close()

plt.figure()
plt.plot(rg_rmsd,rg_rmsd,color='dimgray',alpha=1.0)
for m, method in enumerate(methods):
        plt.scatter(rg_rmsd[m],im_rmsd[m],color=buff_dict.get(buffer_gas[m]),marker=mark_dict.get(method),edgecolor='black',alpha=0.75,s=100)
plt.ylabel(r"RMSD w/ IM score function ($\AA$)",fontsize=10)
plt.xlabel(r"RMSD w/ RG score function ($\AA$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG5/a_i.png',dpi=1200)
plt.close()

plt.figure()
plt.plot(rg_tmscore,rg_tmscore,color='dimgray',alpha=1.0)
for m, method in enumerate(methods):
        plt.scatter(rg_tmscore[m],im_tmscore[m],color=buff_dict.get(buffer_gas[m]),alpha=0.75,s=100,edgecolor='black',marker=mark_dict.get(method))
plt.ylabel(r"TM-Score w/ IM score function",fontsize=10)
plt.xlabel(r"TM-Score w/ RG score function",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG5/a_ii.png',dpi=1200)
plt.close()
