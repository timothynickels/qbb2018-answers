#!/usr/bin/env python3

""""
Usage:
"""
import sys
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import scipy.cluster.vq as vac
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind

file1=open(sys.argv[1])

#create dataframe
dataFrame = pd.read_table(file1, sep="\t", header = 0, index_col =0)
array = dataFrame.values

transposed_array = np.transpose(array)
transposed_dataframe = dataFrame.transpose()

Z = linkage(transposed_array,'ward')

cell_name= leaves_list(Z)
cell_names_ordered = transposed_dataframe.index.values[cell_name]

#plot dendrogram by cell type
fig, ax = plt.subplots(figsize=(10,5))
plt.title("Dendrogram")
plt.xlabel("Cell")
plt.ylabel("Distance")
dendrogram(
    Z,
    show_leaf_counts=False,
    leaf_rotation = 90,
    leaf_font_size=8,
    show_contracted=True,
    labels = cell_names_ordered
)
plt.tight_layout()
fig.savefig("dendrogram_by_cell.png")
plt.close(fig)

#heat map

cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)
ax1 = sns.clustermap(transposed_dataframe, metric='euclidean', cmap=cmap)
ax1.savefig("heatmap.png")


#k-means clustering
centroids, labels=vac.kmeans2(array, 4)
data, moreLabels=vac.vq(array,centroids)

##plot CFU and poly
fig2, ax2 = plt.subplots()
plt.title('K-means clustering of CFU and Poly')
plt.scatter(centroids[:,0], centroids[:,1], c='red', marker='x')
plt.scatter(array[data==0,0], array[data==0,1], c='blue', marker='o')
plt.scatter(array[data==1,0], array[data==1,1], c='black', marker ='o')
fig2.savefig("kmeans.png")
plt.close(fig2)

#differentially expressed genes

early = ["CFU", "mys"]
late = ["poly", "unk"]

t_stat, p_val = ttest_ind(dataFrame[early], dataFrame[late], axis = 1)
dataFrame["p_value"] = p_val

dataFrame = dataFrame.mask(dataFrame["p_value"] > 0.05).dropna(how = "any").sort_values ("p_value")

#list of differentially expressed genes
print(dataFrame.ix[:,4].to_csv(sep='\t'))

#names for panther
print(dataFrame.index)

