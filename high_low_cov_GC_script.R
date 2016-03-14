#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=4) {
  stop("Four argument must be supplied arg[1] = inputfile, arg[2] = outputfile.\n", call.=FALSE)
}

inputcovdir <- args[1]
inputGCdir <- args[2]
outputdir <- args[3]
filename <- args[4]

library(dplyr)
graphdir <- paste(outputdir, filename, ".png", sep = "")
spacedir <- paste(outputdir, filename, ".RData", sep = "")
cov.high_low <- read.csv(inputcovdir, sep = '\t')
#cov_all <- read.csv("/isi/olga/xin/Halophile_project/output/20160308/DS2_1_map_Haloarcula_cov.csv")
GC_all <- read.csv(inputGCdir)
#cov_all <- cov_all[,1:2]
GC_all <- GC_all[, 1:2]
##in GC_all, Position data contain , in the number,
# to remove that:
Position <- as.character(GC_all$Position)
Position <- gsub(",","", Position)
Position <- as.integer(Position)
names(cov.high_low) <- c("genome","Position","cov")
GC_all$Position <- Position
cov.high_low_GC <- inner_join(cov.high_low, GC_all)
cov.high_low_GC$Value <- as.numeric(as.character(cov.high_low_GC[,4]))
cov.high_low_GC <- na.omit(cov.high_low_GC)
if (nlevels(cov.high_low_GC$cov) > 1) {
  cor(as.numeric(cov.high_low_GC[, 3]), cov.high_low_GC[,4])
  res <- lm(cov.high_low_GC[,4] ~ cov.high_low_GC[, 3], data = cov.high_low_GC)
  summary(res)
  png(file = graphdir)
  plot(as.numeric(cov.high_low_GC[, 3]), cov.high_low_GC[,4], main = filename,xlab = "coverage",ylab = "GC", pch = 20, col = "grey", type = "p")
  abline(res, col = "red")
  lines(lowess(as.numeric(cov.high_low_GC[, 3]), cov.high_low_GC[,4]),col="blue")
  dev.off()
}
if (nlevels(cov.high_low_GC$cov) == 1){
  png(file = graphdir)
  hist(cov.high_low_GC[,4], main =filename ,xlab = "GC content distribution" )
  dev.off()
}

save.image(spacedir)
