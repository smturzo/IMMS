import pandas as pd, numpy as np, seaborn as sns
from scipy import stats
from matplotlib import rcParams
import matplotlib
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['font.family']='serif'
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ccs_time_data_parcs_impact = pd.read_csv('./FIG2/impact_parcs_ccs_time.csv',header=0)
parcs_ccs  = ccs_time_data_parcs_impact['PARCS-CCS']
impact_ccs = ccs_time_data_parcs_impact['IMPACT-CCS']
impact_time= ccs_time_data_parcs_impact['IMPACT-Time']
parcs_time = ccs_time_data_parcs_impact['PARCS-Time']
parcs_ccs_std_data = pd.read_csv('./FIG2/std_dev_ccsparcs_randrot.csv', header=0)

plt.figure()
plt.scatter(impact_ccs,parcs_ccs,marker='o',s=100,color='crimson',alpha=0.35)
plt.xticks()
plt.yticks()
plt.ylabel(r"$CCS_{PARCS}$ ($\AA^2$)",fontsize=10)
plt.xlabel(r"$CCS_{IMPACT}$ ($\AA^2$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG2/b.png',dpi=1200)
plt.close()

percent_diff_list= (abs( parcs_ccs - impact_ccs )/ impact_ccs)*100
avg_percent_diff = np.mean( np.array(percent_diff_list) )
print('AVG PERCENT DIFF FOR IMPACT: ',str(avg_percent_diff))

slope, intercept, r_value, p_value, std_err = stats.linregress(impact_ccs,parcs_ccs)
print('R2 of IMPACT and PARCS:',r_value**2)
rmse = ( np.mean((parcs_ccs - impact_ccs)**2) ) **0.5
print('RMSE of IMPACT and PARCS',rmse)

plt.figure()
plt.scatter(impact_ccs,impact_time,marker='o',s=100,color='lightskyblue',alpha=0.25)
plt.scatter(parcs_ccs,parcs_time,marker='o',s=100,color='violet',alpha=0.35)
plt.hlines(1.0, 0 , max(parcs_ccs)+100, colors='black', linestyles='dashed')
plt.xlim(min(parcs_ccs)-90,max(parcs_ccs)+90)
plt.ylabel(r"Time (s)",fontsize=10)
plt.xlabel(r"$CCS_{Predicted}$ ($\AA^2$)",fontsize=10)
plt.xticks()
plt.yticks()
plt.tight_layout()
plt.savefig('./FIG2/d.png',dpi=1200)
plt.close()

exp_ccs_parcs_ccs_data = pd.read_csv('./FIG2/parcs_pred_exp_ccs.csv',header=0)
exp_ccs_im    = exp_ccs_parcs_ccs_data['CCS_IM']
exp_ccs_parcs = exp_ccs_parcs_ccs_data['CCS_PARCS']
buffer_gas    = exp_ccs_parcs_ccs_data['Buffer-Gas']
buff_gas_dict = {'He':'red','N2':'deepskyblue'}
plt.figure()
plt.plot(exp_ccs_im,exp_ccs_im,color='black')
for i, bg in enumerate(buffer_gas):
	plt.scatter(exp_ccs_im[i],exp_ccs_parcs[i],color=buff_gas_dict.get(bg),s=100,edgecolor='black',alpha=0.55)

plt.xticks()
plt.yticks()
plt.xlabel("Random Rotations",fontsize=10)
plt.ylabel(r"$CCS_{PARCS}$ ($\AA^2$)",fontsize=10)
plt.xlabel(r"$CCS_{IM}$ ($\AA^2$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG2/c.png',dpi=1200)
plt.close()

percent_diff_list= (abs( exp_ccs_parcs - exp_ccs_im )/ exp_ccs_im)*100
avg_percent_diff = np.mean( np.array(percent_diff_list) )
print('AVG PERCENT DIFF FOR IM: ',str(avg_percent_diff))

slope, intercept, r_value, p_value, std_err = stats.linregress(exp_ccs_im,exp_ccs_parcs)
print('R2 of IM and PARCS:',r_value**2)



plt.figure()
ax= sns.violinplot(x="rot",y="std100ccs",data=parcs_ccs_std_data,split=True,cut=0,inner="box")#
ax.set(xlabel='')
ax.set(ylabel='')
plt.xlabel("Random Rotations",fontsize=10)
plt.ylabel(r"Std"+"."+" dev of $CCS_{PARCS}$ ($\AA^2$)",fontsize=10)
plt.tight_layout()
plt.savefig('./FIG2/a.png',dpi=1200)
plt.close()

