#!/usr/bin/env Rscript
# this function is to make the table of reads and their COG classes
library(Hmisc)
library(dplyr)
args = commandArgs(trailingOnly=TRUE)
# test if there is at least one argument: if not, return an error
if (length(args)!=1) {
  stop("One argument must be supplied arg[1] = sample.\n", 
       call.=FALSE)
}

sample <- args[1]

#sample <- "DS2_1"

inputhits <- paste("/isi/olga/xin/Halophile_project/output/20160301/", sample, 
                   "_blx_reduced.m8", sep = "")
inputcog <- paste("/isi/olga/xin/Halophile_project/output/20160301/",sample, 
                  "_cog.txt", sep = "")
outputdir <- paste("/isi/olga/xin/Halophile_project/output/20160311/", sample,
                   "_cog_final.txt", sep = "")
#print(inputhits)
blxhits <- read.table(inputhits, header = F)  
names(blxhits) <- c("reads","refseq")
cogs <- read.table(inputcog, header = F) 
names(cogs) <- c("reads","cog")
reads.count <- as.data.frame(table(blxhits[, 1]))
readslist <- reads.count[, 1]
reads.cog.final <- matrix(data = NA, length(readslist), 2)
for (i in 1:length(readslist)) {
  read <- as.data.frame(readslist[i])
  names(read) <- "reads"
  read.cog <- inner_join(cogs, read)
  print(i)
  if (length(read.cog$reads) == 1) {
    reads.cog.final[i, ] <- c(as.character(read.cog$reads), as.character(read.cog$cog))
  }
  if (length(read.cog$reads) > 1) {
    if (nlevels(as.factor(as.character(read.cog$cog))) == 1) {
      reads.cog.final[i,] <- c(as.character(read.cog$reads[1]), as.character(read.cog$cog[1]))
    }
    if (nlevels(as.factor(as.character(read.cog$cog))) == 2 && "NULL" %in% as.character(read.cog$cog)) {
      read.cog.notnull <- read.cog[(as.character(read.cog$cog) != "NULL"), ]
      reads.cog.final[i, ] <- c(as.character(read.cog.notnull$reads[1]), as.character(read.cog.notnull$cog[1]))
    }
    if (nlevels(as.factor(as.character(read.cog$cog))) == 2 && "NULL" %nin% as.character(read.cog$cog)) {
      reads.cog.final[i, ] <- c(as.character(read.cog$reads[1]), "Undecidable")
    }
    if (nlevels(as.factor(as.character(read.cog$cog))) > 2) {
      reads.cog.final[i, ] <- c(as.character(read.cog$reads[1]), "Undecidable")
    }
  }
} 
write.table(reads.cog.final, file = outputdir, sep = '\t')
