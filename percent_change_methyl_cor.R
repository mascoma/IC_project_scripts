library(RColorBrewer)
library(ggplot2)
library(reshape)
library(dplyr)

dir <- "/isi/olga/xin/Halophile_project/output/20160429/"
dir2 <- "/isi/olga/xin/Halophile_project/output/20160509/"
inputfile1 <- "ICC_DS2_1_unmapped_genus_count.txt"
inputfile2 <- "ICC_DS2_2_unmapped_genus_count.txt"
inputfile3 <- "ICC_genus_count.txt"
inputfile4 <- "Halophile_mathyltransferases.txt"

outdir <- "/isi/olga/xin/Halophile_project/output/20160510/"
outputfile1 <- "percent_change_r2.jpeg"
outputfile2 <- "CTAG_status_r2.jpeg"
outputfile3 <- "GTCGAC_status_r2.jpeg"
outputfile4 <- "genus_change_r1.jpeg"

input1 <- paste(dir, inputfile1, sep = '')
input2 <- paste(dir, inputfile2, sep = '')
input3 <- paste(dir, inputfile3, sep = '')
input4 <- paste(dir2, inputfile4, sep = '')
 
unmapped.r1 <- read.delim2(input1, sep = '\t', header = F, as.is = T)
unmapped.r2 <- read.delim2(input2, sep = '\t', header = F, as.is = T)
all <- read.delim2(input3, sep = '\t', header = F, as.is = T)
methy <- read.delim2(input4, sep = '\t', header = T, as.is = T)
unmapped.r1 <- unmapped.r1[order(unmapped.r1[, 2], decreasing = T), ]
unmapped.r2 <- unmapped.r2[order(unmapped.r2[, 2], decreasing = T), ]
all <- all[order(all[, 2], decreasing = T), ]
percent.ur1 <- (unmapped.r1[, 2]/sum(unmapped.r1[, 2]))*100
percent.ur2 <- (unmapped.r2[, 2]/sum(unmapped.r2[, 2]))*100
percent.all <- (all[, 2]/sum(all[, 2])*100)
unmapped.r1.p <- cbind(unmapped.r1, percent.ur1)
unmapped.r2.p <- cbind(unmapped.r2, percent.ur2)
all.p <- cbind(all, percent.all)
names(unmapped.r1.p) <- c("taxa", "count", "percent")
names(unmapped.r2.p) <- c("taxa", "count", "percent")
names(all.p) <- c("taxa", "count", "percent")

#### replicate 1####
r1.all <- inner_join(unmapped.r1.p, all.p, by = "taxa")
dpercent <- r1.all[, 3] - r1.all[, 5]
r1.all <- cbind(r1.all, dpercent)
r1.dp <- r1.all[, c(1, 6)]
r1.dp <- r1.dp[order(r1.dp[, 2], decreasing = T), ]


methy.genera <- names(table(methy[, 1]))
motif.freq <- matrix(NA, length(methy.genera), ncol = 3)
for (i in 1:length(methy.genera)){
  methy.genus <- methy[methy[, 1] == methy.genera[i], ]
  methy.species.all <- names(table(methy.genus[, 2]))
  methy.genus.m1 <- methy.genus[methy.genus[, 4] == "CTAG", ]
  methy.genus.m2 <- methy.genus[methy.genus[, 4] == "GTCGAC", ]
  methy.species.m1 <- names(table(methy.genus.m1[, 2]))
  methy.species.m2 <- names(table(methy.genus.m2[, 2]))
  motif1.p <- length(methy.species.m1) /length(methy.species.all) ## calculate how many species in one genus have motif 1
  motif2.p <- length(methy.species.m2) /length(methy.species.all)
  motif.freq[i, ] <- c(methy.genera[i], motif1.p, motif2.p)
}


motif.freq <- as.data.frame(motif.freq)

names(motif.freq) <- c("taxa", "CTAG", "GTCGAC")

 
methy.dp.r1 <- inner_join(motif.freq, r1.dp, by = "taxa")
group <- vector(mode = "character", length = length(methy.dp.r1[, 4]))

for (j in 1 : length(methy.dp.r1[, 4])){
  if (methy.dp.r1[j, 4] > 0){
    group[j] = "P"
  }
  if(methy.dp.r1[j, 4] < 0){
    group[j] = "N"
  }
}
methy.dp.r1 <- cbind(methy.dp.r1, group)
methy.dp.r1[, 2] <- as.numeric(as.character(methy.dp.r1[, 2]))
methy.dp.r1[, 3] <- as.numeric(as.character(methy.dp.r1[, 3]))
methy.dp.r1 <- methy.dp.r1[order(methy.dp.r1[, 4], decreasing = T), ]


####replicate 2 #####
r2.all <- inner_join(unmapped.r2.p, all.p, by = "taxa")
dpercent <- r2.all[, 3] - r2.all[, 5]
r2.all <- cbind(r2.all, dpercent)
r2.dp <- r2.all[, c(1, 6)]
r2.dp <- r2.dp[order(r2.dp[, 2], decreasing = T), ]
methy.genera <- names(table(methy[, 1]))
motif.freq <- matrix(NA, length(methy.genera), ncol = 3)
for (i in 1:length(methy.genera)){
  methy.genus <- methy[methy[, 1] == methy.genera[i], ]
  methy.species.all <- names(table(methy.genus[, 2]))
  methy.genus.m1 <- methy.genus[methy.genus[, 4] == "CTAG", ]
  methy.genus.m2 <- methy.genus[methy.genus[, 4] == "GTCGAC", ]
  methy.species.m1 <- names(table(methy.genus.m1[, 2]))
  methy.species.m2 <- names(table(methy.genus.m2[, 2]))
  motif1.p <- length(methy.species.m1) /length(methy.species.all) ## calculate how many species in one genus have motif 1
  motif2.p <- length(methy.species.m2) /length(methy.species.all)
  motif.freq[i, ] <- c(methy.genera[i], motif1.p, motif2.p)
}


motif.freq <- as.data.frame(motif.freq)

names(motif.freq) <- c("taxa", "CTAG", "GTCGAC")


methy.dp.r2 <- inner_join(motif.freq, r2.dp, by = "taxa")
group <- vector(mode = "character", length = length(methy.dp.r2[, 4]))

for (j in 1 : length(methy.dp.r2[, 4])){
  if (methy.dp.r2[j, 4] > 0){
    group[j] = "P"
  }
  if(methy.dp.r2[j, 4] < 0){
    group[j] = "N"
  }
}
methy.dp.r2 <- cbind(methy.dp.r2, group)
methy.dp.r2[, 2] <- as.numeric(as.character(methy.dp.r2[, 2]))
methy.dp.r2[, 3] <- as.numeric(as.character(methy.dp.r2[, 3]))
methy.dp.r2 <- methy.dp.r2[order(methy.dp.r2[, 4], decreasing = T), ]



g1 <- ggplot(methy.dp.r2, aes(x = reorder(taxa, dpercent), y = dpercent, fill =  group)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + 
  scale_fill_manual(values=c("darksalmon","darkseagreen4"), guide=FALSE) +
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey80", linetype="dashed"),
        axis.title.y = element_text(size =20)) + 
  xlab("") + ylab("Changes of percentage")  
g1 
ggsave(path = outdir, plot = g1, file = outputfile1, device = "jpeg", 
       width = 16, height = 9)
colorlist1 <- c(brewer.pal(8, "Purples"))
g2 <- ggplot(methy.dp.r2, aes(x = reorder(taxa, dpercent), y = 1, fill = CTAG)) + 
  geom_point(shape = 21, size = 10) + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank(),
        panel.background = element_rect(fill = "white"),
        axis.title.y = element_text(size =20)) + xlab("") + ylab("CTAG") +
  scale_fill_gradient(high ="purple4", low ="white")
g2 

ggsave(path = outdir, plot = g2, file = outputfile2, device = "jpeg", 
       width = 18, height = 9)

g3 <- ggplot(methy.dp.r2, aes(x = reorder(taxa, dpercent), y = 1, fill = GTCGAC)) + 
  geom_point(shape = 21, size = 10) + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank(),
        panel.background = element_rect(fill = "white"),
        axis.title.y = element_text(size =20)) + xlab("") + ylab("GTCGAC") +
  scale_fill_gradient(high ="saddlebrown", low ="white")
g3 

ggsave(path = outdir, plot = g3, file = outputfile3, device = "jpeg", 
       width = 18, height = 9)

#### plot r1.dp, r2.dp ###
r1.dp.sub <- r1.dp[(r1.dp[, 2]  > 0.5 | r1.dp[, 2] < 0), ]
group <- vector(mode = "character", length = length(r1.dp.sub[, 2]))

for (j in 1 : length(r1.dp.sub[, 2])){
  if (r1.dp.sub[j, 2] > 0){
    group[j] = "P"
  }
  if(r1.dp.sub[j, 2] < 0){
    group[j] = "N"
  }
}
g4 <- ggplot(r1.dp.sub, aes(x = reorder(taxa, dpercent), y = dpercent, fill =  group)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + 
  scale_fill_manual(values=c("darksalmon","darkseagreen4"), guide=FALSE) +
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey80", linetype="dashed"),
        axis.title.y = element_text(size =20)) + 
  xlab("") + ylab("Changes of percentage")  
g4 
ggsave(path = outdir, plot = g4, file = outputfile4, device = "jpeg", 
       width = 20, height = 9)