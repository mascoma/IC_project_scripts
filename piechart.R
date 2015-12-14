library(plotrix)
dom = read.table("dom_level_sum.txt", sep = "\t", header = T)
head(dom)
lbls = dom[, 1]
DS2_1 = (dom[, 2]/sum(dom[, 2]))*100
DS2_2 = (dom[, 3]/sum(dom[, 3]))*100
ICC = (dom[, 4]/sum(dom[, 4]))*100

lbls1 = vector("character", length = 7)
for (i in 1: length(lbls)){
  lbls1[i] = paste(lbls[i]," (", round(DS2_1[i], 2), "%)", sep ="")
}
lbls2 = vector("character", length = 7)
for (i in 1: length(lbls)){
  lbls2[i] = paste(lbls[i]," (", round(DS2_2[i], 2), "%)", sep ="")
}
lbls3 = vector("character", length = 7)
for (i in 1: length(lbls)){
  lbls3[i] = paste(lbls[i]," (", round(ICC[i], 2), "%)", sep ="")
}
pie(DS2_1,labels = lbls1,col= topo.colors(7, alpha = 0.5),cex = 0.8,
    main="DS2_1")
pie(DS2_2,labels = lbls2, col= topo.colors(7, alpha = 0.5),cex = 0.8,
    main="DS2_2")
pie(ICC,labels = lbls3, col= topo.colors(7, alpha = 0.5),cex = 0.8,
    main="ICC")