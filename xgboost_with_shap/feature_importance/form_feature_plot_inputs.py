import pdb 
import pandas as pd
import numpy as np

data=open("FeatureSHAP.tsv",'r').read().strip().split('\n')
data_dict=dict()
for line in data[1::]:
    tokens=line.split('\t')
    feature=tokens[0]
    meanshap=tokens[1]
    substrate=tokens[2]
    if feature not in data_dict:
        data_dict[feature]=dict()
    data_dict[feature][substrate]=float(meanshap)
data=pd.DataFrame(data_dict)
data=data.transpose()
data[pd.isna(data)]=0
data=data/np.sum(data,axis=0)
data=data*100
mean_impact=data.mean(axis=1)
std_impact=data.std(axis=1)
data['MeanImpact']=mean_impact
data['StdImpact']=std_impact
data['Rank']=data['MeanImpact'].rank(ascending=False)
data.to_csv('FeatureRanksByShap.tsv',sep='\t',index=True)



