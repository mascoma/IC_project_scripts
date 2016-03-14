#!/usr/bin/env Rscript
# this function is to make the table of reads and their COG classes
library(Hmisc)
library(dplyr)
args = commandArgs(trailingOnly=TRUE)
# test if there is at least one argument: if not, return an error
if (length(args)!=2) {
  stop("Two argument must be supplied args[1] = sample, args[2] = index.\n", 
       call.=FALSE)
}

sample <- args[1]
index <- args[2]

#sample = "ICC"
#index = 1
inputcog <- paste("/isi/olga/xin/Halophile_project/output/20160301/", sample, 
                   "_cog.txt", sep = "")
inputreads <- paste("/isi/olga/xin/Halophile_project/output/20160314/",sample, 
                  "_readslist_", index ,".txt", sep = "")
outputdir <- paste("/isi/olga/xin/Halophile_project/output/20160314/", sample,
                   "_cog_p", index ,".txt", sep = "")
#print(inputhits)

cogs <- read.table(inputcog, header = F) 
names(cogs) <- c("reads","cog")
readslist <- read.table(inputreads, header = T)
names(readslist) <- "reads"

reads.cog.final <- matrix(data = NA, length(readslist[,1]), 2)
subcogs <- inner_join(cogs, readslist)
for (i in 1:length(readslist[, 1])) {
  read <- as.data.frame(readslist[i, 1])
  names(read) <- "reads"
  read.cog <- inner_join(subcogs, read)
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

