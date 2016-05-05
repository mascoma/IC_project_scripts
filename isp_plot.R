library(ggplot2)
inputdir <- "/isi/olga/xin/Halophile_project/output/20160420/ICC_reads_isp.txt"
outputdir <- "/isi/olga/xin/Halophile_project/output/20160420/"
filename <- "ICC_reads_isp.jpeg"
dat <- read.delim2(inputdir, sep = '\t', header = F, stringsAsFactors = FALSE)
dat.iep <- as.numeric(dat[, 3])
dat.iep <- as.data.frame(dat.iep)
names(dat.iep) <- "isoelectric_point"
g <- ggplot(dat.iep, aes(x = isoelectric_point)) + geom_density( ) 
 
g
ggsave(path = outputdir, plot = g, file = filename, device = "jpeg", 
       width = 13, height = 9)