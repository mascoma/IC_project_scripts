library(data.table)
library(ggplot2)
inputfile = "/Users/Xin/Desktop/IC_project/output/reads_assigned_bl_dd/ICW_rpoB_taxon_count.csv"
outputfile = "/Users/Xin/Desktop/IC_project/output/reads_assigned_bl_dd/ICW_rpoB_count.png"
rpoB = read.csv(inputfile, header = T)
Percent = (rpoB[, 2]/sum(rpoB[,2]))*100
rpoB = cbind(rpoB, Percent)
ggplot(rpoB, aes(x = reorder(genus, count), y = Percent)) + 
  geom_bar(stat = "identity", fill="lightblue", colour="black") + 
  geom_text(aes( label = count), size = 8, vjust = -0.2) +   
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed"))+
  xlab("") +ylab("Percent") + theme(axis.title.y = element_text(size =20)) 
ggsave(outputfile, width = 25, height = 15)
