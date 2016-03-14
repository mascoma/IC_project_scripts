library(dplyr)
library(Hmisc)
inputdir1 = "/Users/Xin/Desktop/IC_project/output/Jan282016/DS2_2_taxa_count.csv"
inputdir2 = "/Users/Xin/Desktop/IC_project/output/Jan282016/DS2_2_genus_count.csv"
outputdir1 = "/Users/Xin/Desktop/IC_project/output/Jan282016/DS2_2_highlevel_count.csv"
taxa = read.delim(inputdir1, sep = ",", header = F)
genus = read.delim(inputdir2, sep = ",", header = F)
names(taxa) = c("taxa","count")
names(genus) = c("taxa", "count")

for (i in 1 : length(taxa[, 1])){
  tmp1 = taxa[i,1]
  if (tmp1 %nin% genus[, 1]) {
     t = taxa[i,1]
     c = taxa[i,2]
     line  = paste (t, c, sep = ',')
     write(line, file = outputdir1, append = T)
  }
}
  
 