# IMMS
## Supplementary data for the paper: Protein shape sampled by ion mobility mass spectrometry consistently improves protein structure prediction
### Authors: SM Bargeen Alam Turzo, Justin T. Seffernick, Amber D. Rolland, Micah T. Donor, Sten Heinze, James S. Prell,  View ORCID ProfileVicki Wysocki,  View ORCID ProfileSteffen Lindert

#### The folders within this directory contains:
#####	**NC\_DATA** : This directory contains all the output files from the per\_residue\_solvent\_exposure application\.
#####	**Paper\_Figures** : This directory contains all the scripts neccessary to regenerate the figures in the paper mention above\.
#####	**Top\_Predicted\_Structures** : This directory contains all the top predicted structures from AlphaFold2, RoseTTAFold, Ion-Mobility Score Function, Rosetta Score Function, and  Proxy Score Function\.
#####   **Example_Commands** : This directory contains example scripts that were used to run AlphaFold2, RoseTTAFold, and Rosetta (ab initio and comparative modleing) 
#####   **Example_Data** : This directory contains the example data (zipped) for 3A1Y (PDB ID from the ideal dataset) on which rescoring with IM can be performed for reproducibility. 

## **NC\_DATA**
##### This directory has the folders and file
- CCS\_0percent\_reduced\_NC: Output files containing the neighbor count (NC) results for models predicted with the IM score function when CCS\_Ideal was used\.
- CCS\_2percent\_reduced\_NC: Output files containing the neighbor count (NC) results for models predicted with the IM score function when CCS\_Ideal was reduced by 2%\.
- CCS\_5percent\_reduced\_NC: Output files containing the neighbor count (NC) results for models predicted with the IM score function when CCS\_Ideal was reduced by 5%\.
- CCS\_10percent\_reduced\_NC: Output files containing the neighbor count (NC) results for models predicted with the IM score function when CCS\_Ideal was reduced by 10%\.
- CCS\_20percent\_reduced\_NC: Output files containing the neighbor count (NC) results for models predicted with the IM score function when CCS\_Ideal was reduced by 20%\.
- CCS\_30percent\_reduced\_NC: Output files containing the neighbor count (NC) results for models predicted with the IM score function when CCS\_Ideal was reduced by 30%\.
- native\_neighbor\_count: Output files containing the neighbor count (NC) results for the native crystal structures\.
- All output files from per\_residue\_solvent\_exposure application are named as XXXX\.per\_res\_solv\_expo, where XXXX is the pdb id of the protein from the ideal dataset\.

- The file rgs\_with\_reduced\_ccs\_data\_and\_of\_native is a comma separated file containg the radius of gyration for all the models predicted with IM for the 60 proteins in the Ideal dataset when the CCS was not reduced (0), and when it was reduced by 2%, 5%, 10%, 20%, and 30%. It also contains the radius of gyration for the native crstal structures\.

## **Paper\_Figures**
- This directory has the all the python scripts to regenerate Figures 2-6 and Figures S1-S3 in their appropriate directory\.
	- figure2\.py : This script will re-generate Fig 2a, 2b, 2c, 2d in the directory FIG2.
		- The FIG2 directory has the files : 
			- impact_parcs_ccs_time.csv : This file contains CCS and Timing data of PARCS and IMPACT\.
			- parcs_pred_exp_ccs.csv : This file contains predicted CCS from PARCS and experimental CCS for proteins in the experimental dataset\.
			- std_dev_ccsparcs_randrot.csv : This file contains the average standard deviation data from varying random rotations for the PARCS evaluation dataset\.
	- figure3_figure4\.py : This script will regenerate Fig 3 a(i), a(ii), b(i), b(ii) in the directory FIG3. It will also regenerate Fig 4 a(i), a(ii) and c in FIG4 directory.
		- The FIG3 directory also has:
			- Blender images of native 2ZZQ, 3KYJ and 3VZ9 aligned to proxy score function predicted model, Rosetta score function predicted model and IM predicted model\. These images corresponds to panel c in Fig 3\.
		- The FIG4 directory also has:
			- Blender images of native 3ENI aligned to AF predicted model and IM predicted model\. It also has Blender images of 4D6F aligned to RF predicted model and IM predicted model. All of these corresponds to panel b in Fig 4\.
	-figure5\.py : This script will re-generate Fig 5 a(i), a(ii), b(i) and b(ii) in the directory FIG5\.
		- The FIG5 directory also has:
			- Blender images of native 1QOY, 1VXG, and 1YTQ aligned their respective predicted model from proxy score function, Rosetta score function and IM score function. This images are used in panel c of Fig 5\.
- Furthermore this directory has the directory Exp\_Score\_File\_Pnear\_Results and Ideal\_Score\_File\_Pnear\_Results\. 
	- These two folders contain all raw data from structure prediction results for both the experimental and ideal dataset\.
	- These two folders also contains the RG scores from the proxy score functions for both the experimental and ideal dataset\.  
	
##	**Top\_Predicted\_Structures**
- This directory has the folders containing top predicted structures from Alphafold2 (AF), RoseTTAFold (RF), Rosetta Score Function (RS), Ion\-Mobility Score Function (IM), Proxy Score Function (RG) as well as the native crystal structures as reference in the folder NATIVES
	- IM : This folder is subdivided into 2 folders. One containing top IM score predicted structures for experimental dataset (EXP) and the other for ideal dataset (IDEAL)
	- RS : This folder is subdivided into 2 folders. One containing top RS score predicted structures for experimental dataset (EXP) and the other for ideal dataset (IDEAL)
	- RG : This folder is subdivided into 2 folders. One containing top RG score predicted structures for experimental dataset (EXP) and the other for ideal dataset (IDEAL)
	- RF : This folder is subdivided into 2 folders. One containing top RF predicted structures for experimental dataset (EXP) and the other for ideal dataset (IDEAL)
	- AF : This folder is subdivided into 2 folders. One containing top AF predicted structures for experimental dataset (EXP) and the other for ideal dataset (IDEAL)
	- AF : This folder is subdivided into 2 folders. One containing top AF predicted structures for experimental dataset (EXP) and the other for ideal dataset (IDEAL)
	- NATIVES : This folder is subdivided into 2 folders. One containing native crystal structures for experimental dataset (EXP) and the other for ideal dataset (IDEAL)

##   **Example_Data**

##   **Example_Commands**

##	**Instruction to run PARCS and IM Score function**
##### Note 1: These instruction can also be found in the SI our paper "Protein shape sampled by ion mobility mass spectrometry consistently improves protein structure prediction"
##### Note 2: Since PARCS (for predicting collision cross section in Rosetta) and IM (score structures with IM data) are new implementation of Rosetta, the users have access to these code through the developer agreement license of Rosetta. These implementations will also be available with the next version release of Rosetta\.