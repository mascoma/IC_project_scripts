library(Deducer)
library(ade4)
taxalist = read.delim("/Users/Xin/Desktop/IC_project/output/Jan272016/ICC_unmapped_com.csv", header = T, sep = ",")
taxa1 = taxalist[,1:2]
taxa2 = taxalist[,3:4]
percent1 = taxa1[,2]/sum(taxa1[,2])
percent2 = taxa2[,2]/sum(taxa2[,2])
taxa1_exp = sum(taxa1[,2]) * percent2
taxa1 = cbind(taxa1, percent1, taxa1_exp)
taxa2 = cbind(taxa2, percent2)

likelihood.test(taxa1[,2], taxa1[,4], conservative = T)
G = 2*sum(taxa1[,2]*log(taxa1[,2]/taxa1[,4]))
t1 = taxa1[,3]*100
t2 = taxa2[,3]*100
t1 = as.matrix(t1)
t2 = as.matrix(t2)
mantel.rtest(dist(t1), dist(t2), nrepet = 9999)
