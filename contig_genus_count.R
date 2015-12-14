library(data.table)
library(ggplot2)

contig = read.csv("/Users/Xin/Desktop/IC_project/output/Nov242015/contig_CLC_genus_counts.csv")
Percent = (contig[, 2]/sum(contig[,2]))*100
contig = cbind(contig, Percent)
ggplot(contig, aes(x = reorder(genus, count), y = Percent)) + 
  geom_bar(stat = "identity", fill="lightblue", colour="black") + 
  geom_text(aes( label = count), size = 8, vjust = -0.2) +   
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed"))+
  xlab("") +ylab("Percent") + theme(axis.title.y = element_text(size =20)) 
ggsave("/Users/Xin/Desktop/IC_project/output/Nov252015/contig_genus_count.png", width = 25, height = 15)
