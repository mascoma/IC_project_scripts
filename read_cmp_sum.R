library("Hmisc")
readlen = read.table("ICW_concat_length.txt", sep = '\t')

readtag = read.table("ICW_concat_tag.txt", sep = '\t')
anyDuplicated(readtag)
readlen = as.matrix(readlen)
readtag = as.matrix(readtag)
readsum = readlen
rownames(readsum) = readtag[, 1]
range(readsum[,1])
length(readsum)  

readgroup1 = read.table("ICW_concat_hitdiam.txt", sep = '\t')
readgroup2 = read.table("ICW_concat_hitblstn.txt", sep = '\t')
readgroup1 = as.matrix(readgroup1)
length(readgroup1)
readgroup2 = as.matrix(readgroup2)
length(readgroup2)  
 

#subgroup1 = readsum[!(rownames(readsum) %in% readgroup1), ] # no hits in diafast
#hist(subgroup1, breaks = (max(subgroup1) - min(subgroup1)), xlab = "length of reads", 
#     ylab = "counts", main = "")
#length(readgroup1) #471118
#length(subgroup1) #1522666

subgroup2 = readsum[which(rownames(readsum) %nin% readgroup1), ] # no hits in diasens
length(subgroup2)  
subgroup3 = readsum[which(rownames(readsum) %nin% readgroup2), ]
length(subgroup3)  
subgroup4 = readsum[readgroup1, ] 
length(subgroup4)  
subgroup5 = readsum[readgroup2, ]  
length(subgroup5)
 

full = hist(readsum[, 1], breaks = (max(readsum[,1]) - min(readsum[,1])), xlab = "length of reads", 
     ylab = "counts", main = "")
g1 = hist(subgroup2, breaks = (max(subgroup2) - min(subgroup2)), xlab = "length of reads", 
          ylab = "counts", main = "")
g11 = hist(subgroup4, breaks = (max(subgroup4) - min(subgroup4)), xlab = "length of reads", 
           ylab = "counts", main = "")
g2 = hist(subgroup3, breaks = (max(subgroup3) - min(subgroup3)), xlab = "length of reads", 
          ylab = "counts", main = "")
g22 = hist(subgroup5, breaks = (max(subgroup4) - min(subgroup4)), xlab = "length of reads", 
           ylab = "counts", main = "")
color = c(rgb(224, 224, 224, maxColorValue=255), rgb(255,153,153, maxColorValue = 255), rgb(153,255,255, maxColorValue = 255))

png(filename="ICW_all_diam.png")
plot(full, col = rgb(224, 224, 224, maxColorValue=255), xlab = "length of reads",  
     ylab = "counts", main = "Diamond sensitive mode")
legend(30,100000, c("Complete", "No Hits", "Hits"), pch = 15, col = color, cex = 0.5)
plot(g1, col = rgb(255,153,153, maxColorValue = 255), add = T)
plot(g11, col = rgb(153,255,255, maxColorValue = 255), add = T)
dev.off()


png(filename="ICW_all_blastn.png")
plot(full, col = rgb(224, 224, 224, maxColorValue=255), xlab = "length of reads",  
     ylab = "counts", main = "Blastn")
legend(30,100000, c("Complete", "No Hits", "Hits"), pch = 15, col = color, cex = 0.8)
plot(g2, col = rgb(255,153,153, maxColorValue = 255), add = T)
plot(g22, col = rgb(153,255,255, maxColorValue = 255), add = T)
dev.off()










