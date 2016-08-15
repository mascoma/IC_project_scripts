library(ShortRead)
library(ggplot2)
inputdir <- "/isi/olga/xin/Halophile_project/output/ICC_DS2_mapping_CLC/" 
inputtotal <- "/isi/olga/xin/Halophile_project/input/merged_reads_CLC_fq/ICC_CLC.fastq"
outputdir <- "/isi/olga/xin/Halophile_project/output/20160506/"
outputfile <- "IC_eaten_leftover_GC.jpeg"

inputfile1 <- "ICC_DS2_1_CLC_mapped.fq"
inputfile2 <- "ICC_DS2_1_CLC_unmapped.fq"
inputfile3 <- "ICC_DS2_2_CLC_mapped.fq"
inputfile4 <- "ICC_DS2_2_CLC_unmapped.fq"
input1 <- paste(inputdir, inputfile1, sep = '')
input2 <- paste(inputdir, inputfile2, sep = '')
input3 <- paste(inputdir, inputfile3, sep = '')
input4 <- paste(inputdir, inputfile4, sep = '')

make.GC.dist.table <- function(input, label) {
  fq <- readFastq(input)
  all.freq.collapsed <- alphabetFrequency(sread(fq), as.prob=TRUE, collapse=TRUE)
  GC.mean <- sum(all.freq.collapsed[c("G", "C")]) 
  print(GC.mean)
  all.freq <- alphabetFrequency(sread(fq), as.prob=TRUE)
  GC.dist <- (all.freq[,"G"] + all.freq[,"C"]) *100
  GC.dist <- as.data.frame(GC.dist)
  GC.dist <- cbind(GC.dist, label)
  colnames(GC.dist) <- c("GC", "group")
  return(GC.dist)
}

GC.dist.total <- make.GC.dist.table(inputtotal, "total") ## GC.median = 0.596917
GC.dist.r1.mapped <- make.GC.dist.table(input1, "leftover_replicate1") ## GC.median = 0.6017527
GC.dist.r1.unmapped <- make.GC.dist.table(input2, "eaten_replicate1")  ## GC.median = 0.5418941
GC.dist.r2.mapped <- make.GC.dist.table(input3, "leftover_replicate2") ## GC.median = 0.6018523
GC.dist.r2.unmapped <- make.GC.dist.table(input4, "eaten_replicate2")  ## GC.median = 0.5421658

 
GC.dist.all <- rbind(GC.dist.total, GC.dist.r1.mapped, GC.dist.r1.unmapped, 
                     GC.dist.r2.mapped, GC.dist.r2.unmapped)

g <- ggplot(GC.dist.all, aes(x = GC, colour = group)) + 
  geom_line(stat = "density", size =1, alpha = 0.8) + 
  geom_vline(xintercept = 65.6312, color = "darkblue", alpha = 0.6, 
             size = 1, linetype = "dashed") +
  xlab("GC content (%)") + ylab("Density") +  
  theme(legend.text = element_text(size = 20), text = element_text(size = 20),
        axis.text.y = element_text(size = 20)) +
  scale_colour_manual( name = "", values = c("gray20", "mediumpurple4", 
                                             "deeppink3", "mediumorchid1",
                                             "lightsalmon3"))

g

ggsave(path = outputdir, plot = g, file = outputfile, device = "jpeg", 
       width = 12, height = 9)
