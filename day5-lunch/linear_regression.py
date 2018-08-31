#!/usr/bin/env python3
""""
usage: ./linear_regression.py <ctab_file> <H3K27ac.tab>	<H3K27me3.tab>	<H3K4me1.tab>	<H3K4me3.tab>	<H3K9ac.tab> 

"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

ctab=sys.argv[1]

d={}
names=[]

df = pd.read_csv(ctab,index_col="t_name")

for tab in sys.argv[2:]:
    filename = tab + ".tab"
    df2=pd.read_csv(filename,sep="\t",index_col=0)
    d[tab]=df2.iloc[:,4]
    names.append(tab)

means_df=pd.DataFrame(d) #add dictionary to data frame

means_df["t_name"]=means_df.index #change column head so we can merge based on t_name

result = pd.merge(df, means_df,on="t_name") #merge data frames


tab_string = " + ".join(names)

form = "male_10 ~ " + tab_string

regression = sm.ols(formula=form,data=result)
res = regression.fit()

#print (res.summary()) for question 4


fig,ax = plt.subplots()
ax.set_xlim(left=-100,right=300)
plt.hist(res.resid,bins=1000)
ax.set_title("Residuals for male_10")
ax.set_xlabel("residual value")
ax.set_ylabel("number of transcripts")
fig.savefig("linear_regression.png")
plt.close()


# compute pearson correlation
# pearson_corr = df.corr(method="pearson")
#
# fig,ax = plt.subplots()
# ax.set_title("Pairwise Pearson Corr. of FPKMs")
# im = ax.pcolor(pearson_corr, cmap="bone")
# fig.colorbar(im,ax=ax)
# ax.set_xlabel("Samples")
# ax.set_ylabel("Samples")
# fig.savefig("pearson_corr.png")
# plt.close()

