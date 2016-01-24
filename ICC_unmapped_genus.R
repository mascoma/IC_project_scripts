library(data.table)
library(ggplot2)
ICC = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_genus_graph.csv",stringsAsFactors = F, header = T, sep = ",")
ICC_DS2_1 = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_1_unmapped_genus_graph.csv",stringsAsFactors = F, header = T, sep = ",")
ICC_DS2_2 = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_2_unmapped_genus_graph.csv",stringsAsFactors = F, header = T, sep = ",")
head(ICC_DS2_1)
head(ICC_DS2_2)
head(ICC)
Sample = "ICC_DS2_1"
ICC_DS2_1_percent = Percent = (ICC_DS2_1[, 2]/78580)*100
ICC_DS2_1 = cbind(ICC_DS2_1, Percent)
ICC_DS2_1 = cbind(ICC_DS2_1, Sample)

Sample = "ICC_DS2_2"
ICC_DS2_2_percent = Percent = (ICC_DS2_2[, 2]/80403)*100
ICC_DS2_2 = cbind(ICC_DS2_2, Percent)
ICC_DS2_2 = cbind(ICC_DS2_2, Sample)

Sample = "ICC"
ICC_percent = Percent = (ICC[, 2]/2211826)*100
ICC = cbind(ICC, Percent)
ICC = cbind(ICC, Sample)

head(ICC_DS2_1)
head(ICC_DS2_2)
head(ICC)

DS2_1_ICC = rbind(ICC_DS2_1, ICC)
DS2_2_ICC = rbind(ICC_DS2_2, ICC)

ggplot(DS2_1_ICC, aes(x = reorder(taxa, Percent), y = Percent, fill =  Sample)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1", labels= c("ICC_unmapped", "ICC")) + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 15),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) + xlab("Genus")  

ggsave("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_1_unmapped_genus50.png", width = 25, height = 15)

ggplot(DS2_2_ICC, aes(x = reorder(taxa, Percent), y = Percent, fill =  Sample)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1", labels= c("ICC_unmapped", "ICC")) + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 15),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) + xlab("Genus")  
ggsave("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_2_unmapped_genus50.png", width = 25, height = 15)

