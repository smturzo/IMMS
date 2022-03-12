# IMMS
## Supplementary data for the paper: Protein shape sampled by ion mobility mass spectrometry consistently improves protein structure prediction
### Authors: SM Bargeen Alam Turzo, Justin T. Seffernick, Amber D. Rolland, Micah T. Donor, Sten Heinze, James S. Prell,  View ORCID ProfileVicki Wysocki,  View ORCID ProfileSteffen Lindert

#### The folders within this directory contains:
#####	**NC\_DATA** : This directory contains all the output files from the per\_residue\_solvent\_exposure application\.
#####	**Paper\_Figures** : This directory contains all the scripts neccessary to regenerate the figures in the paper mention above\.
#####	**Top\_Predicted\_Structures** : This directory contains all the top predicted structures from AlphaFold2, RoseTTAFold, Ion-Mobility Score Function, Rosetta Score Function, and  Proxy Score Function\.

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
##### This directory has the all the python scripts to regenerate Figures 2-6 and Figures S1-S3 in their appropriate directory\.
	
##	**Top\_Predicted\_Structures**