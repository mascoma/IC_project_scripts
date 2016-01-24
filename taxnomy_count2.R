library(data.table)
library(ggplot2)
inputfile = "/Users/Xin/Desktop/IC_project/output/01142016/ICC_rpoB_group.csv"
outputfile = "/Users/Xin/Desktop/IC_project/output/01142016/ICC_rpoB_group.png"
taxa = read.csv(inputfile, header = T)
Percent = (taxa[, 2]/sum(taxa[,2]))*100
taxa = cbind(taxa, Percent)
ggplot(taxa, aes(x = reorder(taxa, count), y = Percent)) + 
  geom_bar(stat = "identity", fill="gray25", colour="black") + 
  geom_text(aes( label = count), size = 6, vjust = -0.2) +  theme_bw() + 
  theme(axis.text.x = element_text(angle=20, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank())+
  xlab("") +ylab("Percent") + theme(axis.title.y = element_text(size =10)) 
ggsave(outputfile, width = 8, height = 8)
