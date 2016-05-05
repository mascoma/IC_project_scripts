library(ggplot2)
inputdir1 <- "/isi/olga/xin/Halophile_project/output/20160421/SS37_reads_isp.txt"
inputdir2 <- "/isi/olga/xin/Halophile_project/output/20160420/ICC_reads_isp.txt"
outputdir <- "/isi/olga/xin/Halophile_project/output/20160426/"
filename <- "IC37_SS37_isp.jpeg"
SS37 <- read.delim2(inputdir1, sep = '\t', header = F, stringsAsFactors = FALSE)
SS37.iep <- as.numeric(SS37[, 3])
SS37.iep <- cbind(SS37.iep, "SS_37")
SS37.iep <- as.data.frame(SS37.iep)
names(SS37.iep) <- c("isoelectric_point", "group")
IC37 <- read.delim2(inputdir2, sep = '\t', header = F, stringsAsFactors = FALSE)
IC37.iep <- as.numeric(IC37[, 3])
IC37.iep <- cbind(IC37.iep, "IC_37")
IC37.iep <- as.data.frame(IC37.iep)
names(IC37.iep) <- c("isoelectric_point", "group")
IC.SS.iep <- rbind(IC37.iep, SS37.iep)
g <- ggplot(IC.SS.iep, aes(x = isoelectric_point, colour = group)) + 
  geom_line(stat = "density", size = 2) + 
  xlab("isoelectric point") + ylab("density") +  
  theme(legend.text = element_text(size = 14), text = element_text(size = 14)) +
  scale_colour_manual(name = "", values = c("dodgerblue4","skyblue3"))  
g

ggsave(path = outputdir, plot = g, file = filename, device = "jpeg", 
       width = 13, height = 9)