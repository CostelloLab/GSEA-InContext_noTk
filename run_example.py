import gsea_incontext_notk
import sys, logging

rnk = "GSE4773_DEG_Expt1_Control_vs_Group1_gene.rnk"

# Run GSEA preranked - Hallmarks
#prerank_results = gsea_incontext_notk.prerank(
#	rnk='data/rnk_lists/' + rnk,
#	gene_sets='data/gene_sets/hallmarks.gmt',
#	outdir='out/Prerank_Hallmarks/' + rnk[:-4],
#	permutation_num=100,
#	processes=4
#)

# Run GSEA-InContext - Hallmarks
gseapen_results = gsea_incontext_notk.incontext(
	rnk='data/rnk_lists/' + rnk,
	gene_sets='data/gene_sets/hallmarks.gmt',
	background_rnks='data/bg_rnk_lists/all_442_lists_permuted_x100.csv',
	outdir='out/InContext_Hallmarks/' + rnk[:-4],
	permutation_num=100,
	processes=4
)

print('Done!')
