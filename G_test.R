library(dplyr)
library(Deducer)
library(RVAideMemoire)
#ICC_reads = read.delim("/Users/Xin/Desktop/IC_project/output/Jan272016/ICC_CLC_readslist.csv", header = F)
inputfile1 <- "/Users/Xin/Desktop/projects/IC_project/output/reads_assignment_new/ICC_assignment_new.csv"
inputfile2 <- "/Users/Xin/Desktop/projects/IC_project/output/20160122/resource_tables/ICC_DS2_1_unmapped_genus_count.csv"
inputfile3 <- "/Users/Xin/Desktop/projects/IC_project/output/20160122/resource_tables/ICC_DS2_2_unmapped_genus_count.csv"
inputfile4 <- "/Users/Xin/Desktop/projects/IC_project/output/reads_assignment_new/ICC_genus_assignment.csv"
ICC.assigned.taxa <- read.delim(inputfile1, header = T, sep = ",", as.is = TRUE)
ICC.assigned.genus <- read.delim(inputfile4, header = T, sep = ",", as.is = TRUE)
#ICC_DS2_1_taxa = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/resource_tables/ICC_DS2_1_unmapped_taxa_count.csv", header = T, sep = ",")
ICC.DS2_1.genus <- read.delim2(inputfile2, header = F, sep = ",", as.is = TRUE)
names(ICC.DS2_1.genus) <- c("taxa", "count")
names(ICC.assigned.genus) <- c("read", "taxa")
g.sum1 <- matrix(NA, nrow = 10, ncol = 3)
for (i in 1:10){
  rnum <- sample(1: length(ICC.assigned.taxa[, 1]), 78580)
  subreads <- ICC.assigned.taxa[rnum, ]
  #reads_overlap = inner_join(subreads_assigned, ICC_DS2_1_taxa)
  reads.overlap1 <- inner_join(subreads, ICC.assigned.genus, by = "read")
  sim.read.genus <- reads.overlap1[, 3]
  sim.read.genus.count <- table(sim.read.genus)
  sim.genus.name <- names(sim.read.genus.count)
  sim.read.genus.all <- cbind(sim.read.genus.count, sim.genus.name)
  sim.read.genus.all <- as.data.frame(sim.read.genus.all)
  names(sim.read.genus.all) <- c("count", "taxa")
  sim.read.genus.all[, 1] <- as.numeric(as.character(sim.read.genus.all[, 1]))
  reads_overlap2 <- inner_join(sim.read.genus.all, ICC.DS2_1.genus, by = "taxa")
  percent.obv <- (reads_overlap2[, 1]/sum(reads_overlap2[, 1])) 
  percent.sim <- (reads_overlap2[, 3]/sum(reads_overlap2[, 3])) 
  reads_overlap2 <- cbind(reads_overlap2, percent.obv, percent.sim)
  sum <- G.test(reads_overlap2[, 1], p = reads_overlap2[, 5])
  g.sum1[i, ] <- c(sum$statistic,sum$parameter, sum$p.value)
}

ICC_DS2_2.genus <- read.delim2(inputfile3, header = F, sep = ",", as.is = TRUE)
names(ICC_DS2_2.genus) <- c("taxa", "count")
g.sum2 <- matrix(NA, nrow = 10, ncol = 3)
for (i in 1:10){
  rnum <- sample(1: length(ICC.assigned.taxa[, 1]), 80403)
  subreads <- ICC.assigned.taxa[rnum, ]
  #reads_overlap = inner_join(subreads_assigned, ICC_DS2_1_taxa)
  reads.overlap1 <- inner_join(subreads, ICC.assigned.genus, by = "read")
  sim.read.genus <- reads.overlap1[, 3]
  sim.read.genus.count <- table(sim.read.genus)
  sim.genus.name <- names(sim.read.genus.count)
  sim.read.genus.all <- cbind(sim.read.genus.count, sim.genus.name)
  sim.read.genus.all <- as.data.frame(sim.read.genus.all)
  names(sim.read.genus.all) <- c("count", "taxa")
  sim.read.genus.all[, 1] <- as.numeric(as.character(sim.read.genus.all[, 1]))
  reads_overlap2 <- inner_join(sim.read.genus.all, ICC.DS2_2.genus, by = "taxa")
  percent.obv <- (reads_overlap2[, 1]/sum(reads_overlap2[, 1])) 
  percent.sim <- (reads_overlap2[, 3]/sum(reads_overlap2[, 3])) 
  reads_overlap2 <- cbind(reads_overlap2, percent.obv, percent.sim)
  sum <- G.test(reads_overlap2[, 1], p = reads_overlap2[, 5])
  g.sum2[i, ] <- c(sum$statistic,sum$parameter, sum$p.value)
}
write.table(g.sum1, file = "/Users/Xin/Desktop/projects/IC_project/output/20160509/G_test_ICC_DS2_1.txt", sep = '\t')
write.table(g.sum2, file = "/Users/Xin/Desktop/projects/IC_project/output/20160509/G_test_ICC_DS2_2.txt", sep = '\t')
