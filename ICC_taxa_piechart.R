library(plotrix)
library(RColorBrewer)
library(ggplot2)
library(reshape)
inputdir <- "/isi/olga/xin/Halophile_project/output/20160426/"
inputfile1 <- "ICC_SS_high_taxon.txt"
inputfile2 <- "IC37_genus_count.txt"
 
input1 <- paste(inputdir, inputfile1, sep = '')
input2 <- paste(inputdir, inputfile2, sep = '') 

high.taxa <- read.delim2(input1, sep = '\t', header = T)
IC.genus <- read.delim2(input2, sep = '\t', header = F, as.is = T)
IC.total <- high.taxa[4, 2] + high.taxa[7, 2]
IC.genus.sum <- sum(IC.genus[, 2]) 
IC.unassigned <- high.taxa[4, 2]
IC.nongenus.sum <- high.taxa[7, 2] - IC.genus.sum 
IC.cat <- c(IC.unassigned, IC.genus.sum, IC.nongenus.sum)
IC.cat.percent <- (IC.cat/IC.total)*100
IC.label <- vector("character", length = 3)
taxa.label <- c("unassigned", "assigned at genus level", 
                "assigned above genus level")
for (i in 1: length(taxa.label)){
  IC.label[i] = paste(taxa.label[i], '\n', " (", 
                      round(IC.cat.percent[i], 2), "%)", sep ="")
}

mypalette<-brewer.pal(3, "Pastel2")

pie(IC.cat, labels = IC.label, col= mypalette, cex = 1.2)
 