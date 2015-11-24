library("VennDiagram")

 
venn.plot <- draw.pairwise.venn(area1 = 3212306,area2 = 2783985,cross.area = 2553208,category = c("DS2-1", "ICC"),fill = c("blue", "red"), 
alpha = c(0.2, 0.2),lty = "blank",cex = 1, fontface =  "bold", label.col = rep("gray30", 3), cat.col = rep("gray30", 2),cat.fontface =  "bold", 
cat.dist = 0.1, cat.cex = 1.8,cat.pos = c(270, 90), cat.just = list(c(-0.5,0),c(2, 0)));


venn.plot <- draw.pairwise.venn(area1 = 3090724,area2 = 2783985,cross.area = 2538685,category = c("DS2-2", "ICC"),fill = c("blue", "red"), 
                                alpha = c(0.2, 0.2),lty = "blank",cex = 1, fontface =  "bold", label.col = rep("gray30", 3), cat.col = rep("gray30", 2),cat.fontface =  "bold", 
                                cat.dist = 0.1, cat.cex = 1.8,cat.pos = c(270, 90), cat.just = list(c(-0.5,0),c(2, 0)));
grid.draw(venn.plot);
grid.newpage();