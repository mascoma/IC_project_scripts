library("Hmisc")
readlen1 = read.table("DS2_1_merged_length.txt", sep = '\t')
readtag1 = read.table("DS2_1_merged_tag.txt", sep = '\t')
readlen2 = read.table("DS2_1_R1_length.txt", sep = '\t')
readtag2 = read.table("DS2_1_R1_paired_tag.txt", sep = '\t')
readlen3 = read.table("DS2_1_R2_length.txt", sep = '\t')
readtag3 = read.table("DS2_1_R2_paired_tag.txt", sep = '\t')
readlen1 = as.matrix(readlen1)
readtag1 = as.matrix(readtag1)
readlen2 = as.matrix(readlen2)
readtag2 = as.matrix(readtag2)
readlen3 = as.matrix(readlen3)
readtag3 = as.matrix(readtag3)

readsum1 = readlen1
rownames(readsum1) = readtag1[, 1]
range(readsum1[,1])
length(readsum1) 

readsum2 = readlen2
rownames(readsum2) = readtag2[, 1]
range(readsum2[,1])
length(readsum2) 

readsum3 = readlen3
rownames(readsum3) = readtag3[, 1]
range(readsum3[,1])
length(readsum3) 


h1 = hist(readsum1[, 1], breaks = 60)
h1$density = h1$counts/sum(h1$counts)*100
h2 = hist(readsum2[, 1], breaks =30)
h2$density = h2$counts/sum(h2$counts)*100
h3 = hist(readsum3[, 1], breaks = 30)
h3$density = h3$counts/sum(h3$counts)*100

color = c(rgb(0,0,0,1/4), rgb(1,0,0,1/4), rgb(0,0,1,1/4))

png(filename="DS2_1_length.png") 
plot(h1,col=rgb(0,0,0,1/4), freq=F, xlim = c(0, 500), ylim = c(0, 20), xlab = "Length of reads", ylab = "Percentage", main = "DS2_1_length_distribution")
plot(h2,freq=F, col=rgb(1,0,0,1/4), add = T)
plot(h3,freq=F, col=rgb(0,0,1,1/4), add = T)
legend(400 ,20, c("merged", "paired_R1", "paired_R2"), pch = 15, col = color, cex = 1)
dev.off()
 
t.test(readsum1[, 1], readsum2[, 1])
t.test(readsum1[, 1], readsum3[, 1]) 
 


 