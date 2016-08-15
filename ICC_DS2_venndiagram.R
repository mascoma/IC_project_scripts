library("VennDiagram")


venn.plot <- draw.pairwise.venn(area1 = 3718896,area2 = 3220928, 
                                cross.area = 2954720, fill = c("blue", "red"), 
                                alpha = c(0.3, 0.2), cex = 0.5, 
                                fontface = "bold", label.col = rep("gray30", 3), 
                                cat.col = rep("gray30", 2),
                                cat.fontface =  "bold", cat.dist = 0.1, 
                                cat.cex = 1, cat.pos = c(270, 90), 
                                cat.just = list(c(-0.5,0), c(2, 0)))


venn.plot <- draw.pairwise.venn(area1 = 3558692,area2 = 3220928,
                                cross.area = 2948488, fill = c("blue", "red"), 
                                alpha = c(0.2, 0.2), cex = 0.5, 
                                fontface =  "bold", label.col = rep("gray30", 3), 
                                cat.col = rep("gray30", 2),
                                cat.fontface =  "bold", cat.dist = 0.1, 
                                cat.cex = 1.8,cat.pos = c(270, 90), 
                                cat.just = list(c(-0.5,0), c(2, 0)))