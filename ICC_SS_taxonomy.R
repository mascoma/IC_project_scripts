library(plotrix)
library(RColorBrewer)
library(ggplot2)
library(reshape)
dir <- "/isi/olga/xin/Halophile_project/output/20160426/"
inputfile1 <- "ICC_SS_high_taxon.txt"
inputfile2 <- "IC37_genus_count.txt"
inputfile3 <- "SS37_genus_count.txt"
inputfile4 <- "IC37_phylum_count.txt"
inputfile5 <- "SS37_phylum_count.txt"
outputfile1 <- "IC_SS_phylum.jpeg"
outputfile2 <- "IC_SS_genus.jpeg"

input1 <- paste(dir, inputfile1, sep = '')
input2 <- paste(dir, inputfile2, sep = '')
input3 <- paste(dir, inputfile3, sep = '')
input4 <- paste(dir, inputfile4, sep = '')
input5 <- paste(dir, inputfile5, sep = '')
 

high.taxa <- read.delim2(input1, sep = '\t', header = T)
IC.genus <- read.delim2(input2, sep = '\t', header = F, as.is = T)
SS.genus <- read.delim2(input3, sep = '\t', header = F, as.is = T)
IC.phylum <- read.delim2(input4, sep = '\t', header = F, as.is = T)
SS.phylum <- read.delim2(input5, sep = '\t', header = F, as.is = T)
IC.total <- high.taxa[4, 2] + high.taxa[7, 2]
SS.total <- high.taxa[4, 3] + high.taxa[7, 3]

# dom summary

IC.taxa <- (high.taxa[1:6, 2]/IC.total)*100
SS.taxa <- (high.taxa[1:6, 3]/SS.total)*100
taxa.label <- high.taxa[1:6, 1]

IC.label = vector("character", length = 6)
for (i in 1: length(taxa.label)){
  IC.label[i] = paste(taxa.label[i]," (", round(IC.taxa[i], 2), "%)", sep ="")
}

SS.label = vector("character", length = 6)
for (i in 1: length(taxa.label)){
  SS.label[i] = paste(taxa.label[i]," (", round(SS.taxa[i], 2), "%)", sep ="")
}

mypalette<-brewer.pal(6,"Pastel2")

pie(IC.taxa ,labels = IC.label,col= mypalette, cex = 0.8,
    main="IC_37")
pie(DS2_2,labels = lbls2, col= mypalette,cex = 0.8,
    main="SS_37")

## phylum summary

IC.phylum.total <- sum(IC.phylum[, 2])   ## 0.6585981 reads assigned at phylum level
SS.phylum.total <- sum(SS.phylum[, 2])   ## 0.7655864 raeds assigned at phylum level

IC.phylum.other <- IC.phylum.total - sum(IC.phylum[1:3, 2])
SS.phylum.other <- SS.phylum.total - sum(SS.phylum[1:3, 2])
IC.phylum.short <- c(IC.phylum[1:3, 2], IC.phylum.other) 
SS.phylum.short <- c(SS.phylum[1:3, 2], SS.phylum.other)
IC.phylum.names <- c(IC.phylum[1:3, 1], 'others') 
SS.phylum.names <- c(SS.phylum[1:3, 1], 'others') 
IC.phylum.percent <- (IC.phylum.short / IC.phylum.total) * 100
SS.phylum.percent <- (SS.phylum.short / SS.phylum.total) * 100

IC.phylum.dat <- cbind(IC.phylum.names, IC.phylum.short, IC.phylum.percent, "IC37")
SS.phylum.dat <- cbind(SS.phylum.names, SS.phylum.short, SS.phylum.percent, "SS37")
IC.phylum.dat <- as.data.frame(IC.phylum.dat, stringsAsFactors = F)
SS.phylum.dat <- as.data.frame(SS.phylum.dat, stringsAsFactors = F)
names(IC.phylum.dat) <- names(SS.phylum.dat) <- c("phylum", "count", "percent", "group")
phylum.dat <- rbind(IC.phylum.dat, SS.phylum.dat) 
phylum.dat[, 3] <- as.numeric(as.character(phylum.dat[, 3]))
g <- ggplot(phylum.dat, aes(x = group, y = percent, fill = phylum)) +
  geom_bar(stat = "identity", color = "black", width = 0.3) + coord_flip() +
  theme(legend.text = element_text(size = 20),
        axis.text.x = element_text(size = 20), 
        text = element_text(size = 20)) +
  xlab("") + scale_fill_brewer(palette="Set2") 

g 
  
ggsave(path = dir, plot = g, file = outputfile1, device = "jpeg", 
       width = 15, height = 9)

## genus summary

IC.genus.total <- sum(IC.genus[, 2])   ## 0.5390568 reads assigned at genus level
SS.genus.total <- sum(SS.genus[, 2])   ## 0.6381729 raeds assigned at genus level

IC.genus.other <- IC.genus.total - sum(IC.genus[1:12, 2])
SS.genus.other <- SS.genus.total - sum(SS.genus[1:9, 2])
IC.genus.short <- c(IC.genus[1:12, 2], IC.genus.other) 
SS.genus.short <- c(SS.genus[1:9, 2], SS.genus.other)
IC.genus.names <- c(IC.genus[1:12, 1], 'others') 
SS.genus.names <- c(SS.genus[1:9, 1], 'others') 
IC.genus.percent <- (IC.genus.short / IC.genus.total) * 100
SS.genus.percent <- (SS.genus.short / SS.genus.total) * 100

IC.genus.dat <- cbind(IC.genus.names, IC.genus.short, IC.genus.percent, "IC37")
SS.genus.dat <- cbind(SS.genus.names, SS.genus.short, SS.genus.percent, "SS37")
IC.genus.dat <- as.data.frame(IC.genus.dat, stringsAsFactors = F)
SS.genus.dat <- as.data.frame(SS.genus.dat, stringsAsFactors = F)
names(IC.genus.dat) <- names(SS.genus.dat) <- c("genus", "count", "percent", "group")
genus.dat <- rbind(IC.genus.dat, SS.genus.dat) 
genus.dat[, 3] <- as.numeric(as.character(genus.dat[, 3]))
genera <- c(IC.genus[1:12, 1], SS.genus[1:9, 1], "others")
genus.name <- names(table(genera))
genus.color <- c(brewer.pal(12, "Paired"), "#2F4F4F", "#8B7500", "#666666")
names(genus.color) <- genus.name
g <- ggplot(genus.dat, aes(x = group, y = percent, fill = genus)) +
  geom_bar(stat = "identity", color = "black", width = 0.3) + coord_flip() +
  theme(legend.text = element_text(size = 20),
        axis.text.x = element_text(size = 20), 
        text = element_text(size = 20)) +
  xlab("") + scale_fill_manual(values = genus.color) 

g 

ggsave(path = dir, plot = g, file = outputfile2, device = "jpeg", 
       width = 15, height = 9)