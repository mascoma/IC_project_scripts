library(ShortRead)
library(ggplot2)
IC37.input <- "/isi/olga/xin/Halophile_project/input/merged_reads_CLC_fa/ICC_CLC.fasta"
SS37.input <- "/isi/olga/georgia/SS37/fasta/trimmed_SS37.fasta"
outputdir <- "/isi/olga/xin/Halophile_project/output/20160426/"
outputfile <- "IC37_SS37_GCdist.jpeg"

IC37 <- readFasta(IC37.input)
SS37 <- readFasta(SS37.input)
IC37.alf <- alphabetFrequency(sread(IC37), as.prob=TRUE, collapse=TRUE)
sum(IC37.alf[c("G", "C")])  #0.596917
IC37.alf.dist <- alphabetFrequency(sread(IC37), as.prob=TRUE)
IC37_GCdist <- (IC37.alf.dist[,"G"] + IC37.alf.dist[,"C"]) *100
IC37_GCdist <- as.data.frame(IC37_GCdist)
IC37_GCdist <- cbind(IC37_GCdist, "IC_37")
colnames(IC37_GCdist) = c("GC", "name") 

SS37.alf <- alphabetFrequency(sread(SS37), as.prob=TRUE, collapse=TRUE)
sum(SS37.alf[c("G", "C")])  #0.4998151
SS37.alf.dist <- alphabetFrequency(sread(SS37), as.prob=TRUE)
SS37_GCdist <- (SS37.alf.dist[,"G"] + SS37.alf.dist[,"C"]) *100
SS37_GCdist <- as.data.frame(SS37_GCdist)
SS37_GCdist <- cbind(SS37_GCdist, "SS_37")
colnames(SS37_GCdist) <- c("GC", "name")  


IC_SS_GCdist <- rbind(IC37_GCdist, SS37_GCdist)

g <- ggplot(IC_SS_GCdist, aes(x = GC, colour = name)) + 
  geom_line(stat = "density", size = 2) + 
  xlab("GC content (%)") + ylab("Density") +  
  theme(legend.text = element_text(size = 14), text = element_text(size = 14)) +
  scale_colour_manual( name = "", values = c("coral3","pink3"))
g
 
ggsave(path = outputdir, plot = g, file = outputfile, device = "jpeg", 
       width = 13, height = 9)