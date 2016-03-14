!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=3) {
  stop("Three argument must be supplied arg[1] = inputfile, arg[2] = outputfile.\n", call.=FALSE)
}

inputdir <- args[1]
outputdir <- args[2]
filename <- args[3]
covdir <- paste(dir, filename, "_cov.csv", sep = "")
GCdir <- paste(dir, filename, "_GC.csv", sep = "")
graphdir <- paste(dir, filename, ".png", sep = "")
spacedir <- paste(dir, filename, ".RData", sep = "")
#covdir <- "/isi/olga/xin/Halophile_project/output/20160308/DS2_1_map_Halonotius_sp6_cov.csv"
#GCdir <- "/isi/olga/xin/Halophile_project/output/20160308/DS2_1_map_Halonotius_sp6_GC.csv"
cov <- read.csv(covdir)
GC <- read.csv(GCdir)
 
cov_GC <- cbind(as.character(cov[,1]),cov[,2],as.numeric(as.character(GC[,2])))
cov_GC <- na.omit(cov_GC)
cov_GC <- as.data.frame(cov_GC)
names(cov_GC) <- c("Position", "cov", "GC")
correlation <- cor.test(as.numeric(as.character(cov_GC[,2])), as.numeric(as.character(cov_GC[,3])))
res <- lm(as.numeric(as.character(cov_GC[,3])) ~ as.numeric(as.character(cov_GC[,2])), data = cov_GC)
summary(res)
png(file = graphdir)
plot(as.numeric(as.character(cov_GC[,2])), as.numeric(as.character(cov_GC[,3])), main = "filename",xlab = "coverage",ylab = "GC", pch = 20, col = "grey", type = "p")
abline(res, col = "red")

lines(lowess(as.numeric(as.character(cov_GC[,2])), as.numeric(as.character(cov_GC[,3]))), col="blue")
dev.off()
save.image(spacedir)
