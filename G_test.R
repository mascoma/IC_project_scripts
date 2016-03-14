library(dplyr)
library(Deducer)
library(RVAideMemoire)
#ICC_reads = read.delim("/Users/Xin/Desktop/IC_project/output/Jan272016/ICC_CLC_readslist.csv", header = F)
ICC_assigned = read.delim("/Users/Xin/Desktop/IC_project/output/01142016/reads_assignment_new/ICC_assignment_new.csv", header = T, sep = ",")
#ICC_DS2_1_taxa = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/resource_tables/ICC_DS2_1_unmapped_taxa_count.csv", header = T, sep = ",")
ICC_DS2_1_genus = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/resource_tables/ICC_DS2_1_unmapped_genus_count.csv", header = F, sep = ",")
names(ICC_DS2_1_genus) = c("taxa", "count")
g_sum1 = matrix(NA, nrow = 10, ncol = 3)
for (i in 1:10){
  rnum = sample (1: length(ICC_assigned[,1]), 78580)
  subreads =  ICC_assigned[rnum,]
  subreads = as.data.frame(subreads)
  #reads_overlap = inner_join(subreads_assigned, ICC_DS2_1_taxa)
  reads_overlap2 = inner_join(subreads_assigned, ICC_DS2_1_genus)
  #reads_overlap = cbind(reads_overlap, reads_overlap[, 2]/sum(reads_overlap[, 2]))
  reads_overlap2 = cbind(reads_overlap2, reads_overlap2[, 2]/sum(reads_overlap2[, 2]))
  #G.test(reads_overlap[,3], p = reads_overlap[,4])
  sum = G.test(reads_overlap2[,3], p = reads_overlap2[,4])
  g_sum1[i, ] = c(sum$statistic,sum$parameter, sum$p.value)
}

ICC_DS2_2_genus = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/resource_tables/ICC_DS2_1_unmapped_genus_count.csv", header = F, sep = ",")
names(ICC_DS2_2_genus) = c("taxa", "count")
g_sum2 = matrix(NA, nrow = 10, ncol = 3)
for (i in 1:10){
  rnum = sample (1: length(ICC_assigned[,1]), 80403)
  subreads =  ICC_assigned[rnum,]
  subreads = as.data.frame(subreads)
  #reads_overlap = inner_join(subreads_assigned, ICC_DS2_1_taxa)
  reads_overlap2 = inner_join(subreads_assigned, ICC_DS2_2_genus)
  #reads_overlap = cbind(reads_overlap, reads_overlap[, 2]/sum(reads_overlap[, 2]))
  reads_overlap2 = cbind(reads_overlap2, reads_overlap2[, 2]/sum(reads_overlap2[, 2]))
  #G.test(reads_overlap[,3], p = reads_overlap[,4])
  sum = G.test(reads_overlap2[,3], p = reads_overlap2[,4])
  g_sum2[i, ] = c(sum$parameter, sum$p.value)
}
g_sum2



#subreads_assigned = tally(group_by(subreads, taxa), sort =T)
#taxalist1 = as.data.frame(subreads_assigned[, 1]) # taxa assigned to randaom sampling group
#taxalist2 = as.data.frame(ICC_DS2_1_taxa[, 1]) # taxa assigned to ICC_DS2_1 unmapped group
  

#G = 2*sum(reads_overlap[,3]*log(reads_overlap[,3]/reads_overlap[,2])) # G test G =  2*lnL = obv1*ln(obv1/exp1) + obv2*ln(obv2/exp2) +... 
#G2 = 2*sum(reads_overlap2[,3]*log(reads_overlap2[,3]/reads_overlap2[,2])) # G test G =  2*lnL = obv1*ln(obv1/exp1) + obv2*ln(obv2/exp2) +... 


