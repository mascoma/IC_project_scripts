library(data.table)
library(ggplot2)
inputfile = "/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_2_unmapped_genus_graph2.csv"
outputfile = "/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_2_unmapped_genus_count.png"
taxa = read.csv(inputfile, header = T)
Percent = (taxa[, 2]/80403)*100
taxa = cbind(taxa, Percent)
ggplot(taxa, aes(x = reorder(taxa, count), y = Percent)) + 
  geom_bar(stat = "identity", fill="lightblue", colour="black") + 
  geom_text(aes( label = count), size = 6, vjust = -0.2) +   
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed"))+
  xlab("") +ylab("Percent") + theme(axis.title.y = element_text(size =20)) 
ggsave(outputfile, width = 30, height = 15)
