library(ShortRead)
library(ggplot2)
inputdir <- "/isi/olga/xin/Halophile_project/output/20160413/"
inputfile1 <- "ICC_DS2_2_unmapped_assigned_taxa.fa"
inputfile2 <- "ICC_DS2_2_unmapped_unassigned_taxa.fa"
inputfa1 <- paste(inputdir, inputfile1, sep = '')
inputfa2 <- paste(inputdir, inputfile2, sep = '')
outputdir <- "/isi/olga/xin/Halophile_project/output/20160413/"
outputfile <- "ICC_DS2_2_assigned_unassigned.jpeg"

fa1 <- readFasta(inputfa1)
alf1 <- alphabetFrequency(sread(fa1), as.prob = TRUE, collapse = TRUE)
sum(alf1[c("G", "C")])  #0.6017527
alf1_1 <- alphabetFrequency(sread(fa1), as.prob=TRUE)
fa1_GCdist <- (alf1_1[, "G"] + alf1_1[, "C"]) *100
fa1_GCdist <- as.data.frame(fa1_GCdist)
fa1_GCdist <- cbind(fa1_GCdist, "assigned")
colnames(fa1_GCdist) <- c("GC", "name") 

fa2 <- readFasta(inputfa2)
alf2 <- alphabetFrequency(sread(fa2), as.prob = TRUE, collapse = TRUE)
sum(alf2[c("G", "C")])  #0.5418941
alf2_2 <- alphabetFrequency(sread(fa2), as.prob=TRUE)
fa2_GCdist <- (alf2_2[,"G"] + alf2_2[,"C"]) *100
fa2_GCdist <- as.data.frame(fa2_GCdist)
fa2_GCdist <- cbind(fa2_GCdist, "unassigned")
colnames(fa2_GCdist) <- c("GC", "name") 
fa12 <- rbind(fa1_GCdist, fa2_GCdist)

g <- ggplot(fa12, aes(x = GC, colour = name)) + 
	geom_line(stat = "density", size = 2) + xlab("GC content (%)") + 
	ylab("Density") + ggtitle("ICC_DS2_2") + 
  	theme(legend.text = element_text(size = 14), text = element_text(size = 14)) +
  	scale_colour_manual( name = "", values = c("mediumorchid1", "rosybrown1"))
g
ggsave(path = outputdir, plot = g, file = outputfile, device = "jpeg", 
	width = 13, height = 9)