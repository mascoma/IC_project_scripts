#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=3) {
  stop("Three argument must be supplied arg[1] = inputfile, arg[2] = outputfile.\n", call.=FALSE)
}

inputdir <- args[1]
outputdir <- args[2]
filename <- args[3]
covdir <- paste(inputdir, filename, "_cov.csv", sep = "")
GCdir <- paste(inputdir, filename, "_GC.csv", sep = "")
graphdir <- paste(outputdir, filename, ".png", sep = "")
spacedir <- paste(outputdir, filename, ".RData", sep = "")
cov <- read.csv(covdir)
GC <- read.csv(GCdir)
covap <- vector("numeric", length = 3901495)
for (i in 1:length(cov[,1])){
  if (cov[i,2]!=0){
    covap[i] <- 1
  }
}
cov_GC <- cbind(as.character(cov[,1]), covap, as.character(GC[,2]))
cov_GC <- as.data.frame(cov_GC)
names(cov_GC) <- c("position", "covap", "GC")
correlation <- cor(as.numeric(cov_GC[,2]), as.numeric(cov_GC[, 3]))
res <- lm(as.numeric(cov_GC[,3]) ~ as.numeric(cov_GC[, 2], data = cov_GC))
summary(res)
png(file = graphdir)
plot(as.numeric(cov_GC[, 2]), as.numeric(cov_GC[,3]), main = " ",xlab = "coverage",ylab = "GC", pch = 20, col = "grey", type = "p")
abline(res, col = "red")

lines(lowess(as.numeric(cov_GC[, 2]), as.numeric(cov_GC[,3])), col="blue")
dev.off()
save.image(spacedir)
