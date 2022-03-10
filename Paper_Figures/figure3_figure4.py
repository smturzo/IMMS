import pandas as pd, numpy as np, seaborn as sns
from matplotlib import rcParams
import matplotlib
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['font.family']='serif'
import matplotlib.pyplot as plt
plt.switch_backend('agg')
protein_data= pd.read_csv('./protein_data_ideal.csv',header=0)
mark_dict={'HM':'o','Abinitio':'^'}
methods = protein_data['METHOD']

rs_rmsd = protein_data['RS-RMSD']
im_rmsd = protein_data['IM-RMSD']

rs_tmscore = protein_data['RS-TMScore']
im_tmscore = protein_data['IM-TMScore']

rg_rmsd    = protein_data['MinRG-RMSD']
rg_tmscore = protein_data['MinRG-TMScore']

af_rmsd    = protein_data['AF-RMSD']
af_tmscore = protein_data['AF-TMSCORE']

rf_rmsd    = protein_data['RF-RMSD']
rf_tmscore = protein_data['RF-TMSCORE']

af_ccs = protein_data['UR-AF-CCS']
rf_ccs = protein_data['UR-RF-CCS']

im_ccs     = protein_data['IM-CCS']
rs_ccs     = protein_data['RS-CCS']

native_ccs = protein_data['R-NATIVE-CCS']
seq_length = protein_data['Seq-Length']

abs_delta_af_ccs_norm = abs(af_ccs - native_ccs)/seq_length
abs_delta_rf_ccs_norm = abs(rf_ccs - native_ccs)/seq_length
abs_delta_rs_ccs_norm = abs(rs_ccs - native_ccs)/seq_length
abs_delta_im_ccs_norm = abs(im_ccs - native_ccs)/seq_length

plt.figure()
plt.scatter(af_tmscore,abs_delta_af_ccs_norm,marker='D',s=100,color='crimson',label='AF',edgecolor='black',alpha=0.95)
plt.scatter(rf_tmscore,abs_delta_rf_ccs_norm,marker='h',s=100,color='lightcyan',label='RF',edgecolor='black',alpha=0.85)
plt.legend()
plt.xticks()
plt.yticks()
plt.xlabel(r"TM-Score",fontsize=10)
plt.ylabel(r"Normalized $\Delta$CCS",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG4/c.png',dpi=1200)
plt.close()

plt.figure()
for m, method in enumerate(methods):
	plt.scatter(rs_rmsd[m],im_rmsd[m],color='crimson',marker=mark_dict.get(method),s=100,edgecolor='crimson',alpha=0.65)
plt.plot(rs_rmsd,rs_rmsd,color='black',linewidth=3,alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"RMSD w/ IM score function ($\AA$)",fontsize=10)
plt.xlabel(r"RMSD w/ RS score function ($\AA$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG3/b_i.png',dpi=1200)
plt.close()

plt.figure()
for m, method in enumerate(methods):
        plt.scatter(rs_tmscore[m],im_tmscore[m],color='crimson',marker=mark_dict.get(method),s=100,edgecolor='crimson',alpha=0.65)
plt.plot(rs_tmscore,rs_tmscore,color='black',linewidth=3,alpha=0.70)
plt.xticks()
plt.yticks()
plt.ylabel(r"TM-Score w/ IM score function",fontsize=10)
plt.xlabel(r"TM-Score w/ RS score function",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG3/b_ii.png',dpi=1200)
plt.close()

plt.figure()
plt.plot(rg_rmsd,rg_rmsd,color='dimgray',alpha=1.0)
for i, method in enumerate(methods):
        plt.scatter(rg_rmsd[i],im_rmsd[i],color='indianred',marker=mark_dict.get(method),alpha=0.75,s=100)
plt.ylabel(r"RMSD w/ IM score function ($\AA$)",fontsize=10)
plt.xlabel(r"RMSD w/ RG score function ($\AA$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG3/a_i.png',dpi=1200)
plt.close()

plt.figure()
plt.plot(rg_tmscore,rg_tmscore,color='dimgray',alpha=1.0)
for i, method in enumerate(methods):
        plt.scatter(rg_tmscore[i],im_tmscore[i],color='indianred',alpha=0.75,s=100,marker=mark_dict.get(method))
plt.ylabel(r"TM-Score w/ IM score function",fontsize=10)
plt.xlabel(r"TM-Score w/ RG score function",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG3/a_ii.png',dpi=1200)
plt.close()

conv = pd.read_csv('./ideal_rmsd_tmscore_for_violins', sep='\s+', header=0)
plt.figure()
ax= sns.violinplot(x="METHOD",y="RMSD",data=conv,split=True,cut=0,inner="box")#
ax.set(xlabel='')
ax.set(ylabel='')
plt.ylabel(r"RMSD ($\AA$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG4/a_i.png',dpi=1200)
plt.close()

plt.figure()
ax= sns.violinplot(x="METHOD",y="TMSCORE",data=conv,split=True,cut=0,inner="box")#
ax.set(xlabel='')
ax.set(ylabel='')
plt.ylabel(r"TM-Score",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG4/a_ii.png',dpi=1200)
plt.close()

a= noise_data.groupby('Noise', as_index=False)['IM-RMSD'].mean()
b= noise_data.groupby('Noise', as_index=False)['IM-TMScore'].mean()
print(a)
print(b)

c= conv.groupby('METHOD', as_index=False)['RMSD'].mean()
d= conv.groupby('METHOD', as_index=False)['TMSCORE'].mean()
print(c)
print(d)
