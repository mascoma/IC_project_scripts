library(RColorBrewer)
library(ggplot2)
library(reshape)

slice_data <- function(dir, inputfile, i, group){ 
  # dir, inputfile, group are strings
  # i is a integer indicating how many rows kept
  directory <- dir
  inputname <- inputfile
  input <-  paste(directory, inputname, sep = '')
  var1 <- read.delim2(input, sep = '\t', header = F, as.is = T)
  var2 <- var1[order(var1[, 2], decreasing = T), ]
  var3 <- sum(var2[, 2])
  var4 <- var3 - sum(var2[1:i, 2])
  var5 <- c(var2[1:i, 2], var4)
  var6 <- c(var2[1:i, 1], 'others')
  var7 <- (var5 / var3) *100
  var8 <- cbind(var6, var5, var7, group)
  var8 <- as.data.frame(var8, stringsAsFactors = F)
  names(var8) <- c("taxa", "count", "percent", "group")
  return(var8)
}
dir <- "/isi/olga/xin/Halophile_project/output/20160429/"
inputfile1 <- "ICC_DS2_1_mapped_genus_count.txt"
inputfile2 <- "ICC_DS2_1_unmapped_genus_count.txt"
inputfile3 <- "ICC_DS2_2_mapped_genus_count.txt"
inputfile4 <- "ICC_DS2_2_unmapped_genus_count.txt"
inputfile5 <- "ICC_genus_count.txt"
outdir <- "/isi/olga/xin/Halophile_project/output/20160505/"
outputfile <- "IC_DS2_genus.jpeg"
DS2_1.map.dat <- slice_data(dir, inputfile1, 13, "Replicate1 left over")
DS2_1.unmap.dat <- slice_data(dir, inputfile2, 30, "Replicate1 eaten")
DS2_2.map.dat <- slice_data(dir, inputfile3, 13, "Replicate2 left over")
DS2_2.unmap.dat <- slice_data(dir, inputfile4, 30, "Replicate2 eaten")
IC.dat <- slice_data(dir, inputfile5, 12, "IC37")
genus.dat <- rbind(IC.dat, DS2_1.map.dat, DS2_1.unmap.dat, DS2_2.map.dat, DS2_2.unmap.dat) 
genus.dat[, 3] <- as.numeric(as.character(genus.dat[, 3]))

genera <- names(table(genus.dat[, 1]))
colorlist <- c("#FF4040", "#8B2323","#A6CEE3", "#1F78B4", "#B2DF8A", "#33A02C", 
               "#0000EE", "#8B7355", "#FB9A99", "#E31A1C", "#556B2F", "#6E8B3D", 
               "#00FFFF", "#8A2BE2", "#FDBF6F", "#838B8B", "#FF7F00", "#CAB2D6", 
               "#6A3D9A", "#FFFF99", "#97FFFF", "#CD1076", "#00688B", "#CD2626", 
               "#FFD700", "#B15928", "#CDC673", "#2F4F4F", "#8B008B", "#8B5F65", 
               "#8B7500", "#666666")

names(colorlist) <- genera


g <- ggplot(genus.dat, aes(x = group, y = percent, fill = taxa)) +
  geom_bar(stat = "identity", color = "black", width = 0.2) + coord_flip() +
  theme(legend.text = element_text(size = 20, face="italic"), 
        legend.title=element_blank(),
        axis.text.y = element_text(size = 20),
        text = element_text(size = 20), 
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank(),
        panel.background = element_rect(fill = "white")) +  
  xlab("") + scale_fill_manual(values = colorlist) 

g 

ggsave(path = outdir, plot = g, file = outputfile, device = "jpeg", 
       width = 35, height = 20)
