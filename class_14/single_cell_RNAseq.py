#!/usr/bin/env python

"""
Usage: ./single_cell_RNAseq
"""

import numpy as np
import sys
import scanpy.api as sc
sc.settings.autoshow = False
import matplotlib
matplotlib.use("Agg")

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.tl.pca(adata)
sc.pl.pca(adata, save="unfiltered.png")


filtered = sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=True)

filtered_PCA = sc.tl.pca(filtered)
sc.pl.pca(filtered, save="filtered.png")

sc.pp.neighbors(filtered,n_neighbors=15, n_pcs=50)
sc.tl.louvain(filtered)

sc.tl.tsne(filtered)
sc.pl.tsne(filtered, save="tsne.png")
sc.tl.umap(filtered)
sc.pl.umap(filtered, save="umap.png")

sc.tl.rank_genes_groups(filtered, groupby="louvain", method = "t-test")
sc.pl.rank_genes_groups(filtered, save = "t_test.png")
sc.tl.rank_genes_groups(filtered, groupby="louvain", method = "logreg")
sc.pl.rank_genes_groups(filtered, save = "logreg.png")

sc.tl.tsne(filtered)
sc.pl.tsne(filtered, color = ["louvain", "Igfbpl1"], save="Cluster_0.png")
sc.pl.tsne(filtered, color = ["louvain", "Nrxn3"], save="Cluster_1.png")
sc.pl.tsne(filtered, color = ["louvain", "Tmsb4x"], save="Cluster_2.png")
sc.pl.tsne(filtered, color = ["louvain", "Mdk"], save="Cluster_3.png")
sc.pl.tsne(filtered, color = ["louvain", "Gria2"], save="Cluster_4.png")
sc.pl.tsne(filtered, color = ["louvain", "Tubb3"], save="Cluster_5.png")
sc.pl.tsne(filtered, color = ["louvain", "Stmn2"], save="Cluster_6.png")
sc.pl.tsne(filtered, color = ["louvain", "Dbi"], save="Cluster_7.png")
sc.pl.tsne(filtered, color = ["louvain", "mt-Atp6"], save="Cluster_8.png")
sc.pl.tsne(filtered, color = ["louvain", "Meg3"], save="Cluster_9.png")



