library(data.table)
library(ggplot2)
DS2_1 = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/DS2_1_taxa_graph.csv", stringsAsFactors = F,header = T, sep = ",")
DS2_2 = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/DS2_2_taxa_graph.csv", stringsAsFactors = F, header = T, sep = ",")
ICC = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_taxa_graph.csv",stringsAsFactors = F, header = T, sep = ",")
head(DS2_1)
head(DS2_2)
head(ICC)
Sample = "DS2_1"
DS2_1_percent = Percent = (DS2_1[, 2]/2560484)*100
DS2_1 = cbind(DS2_1, Percent)
DS2_1 = cbind(DS2_1, Sample)

Sample = "DS2_2"
DS2_2_percent = Percent = (DS2_2[, 2]/2484110)*100
DS2_2 = cbind(DS2_2, Percent)
DS2_2 = cbind(DS2_2, Sample)

Sample = "ICC"
ICC_percent = Percent = (ICC[, 2]/2211826)*100
ICC = cbind(ICC, Percent)
ICC = cbind(ICC, Sample)

head(DS2_1)
head(DS2_2)
head(ICC)

DS2_1_ICC = rbind(DS2_1, ICC)
DS2_2_ICC = rbind(DS2_2, ICC)

ggplot(DS2_1_ICC, aes(x = reorder(taxa, Percent), y = Percent, fill =  Sample)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1") + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 15),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) + xlab("Taxa")  
ggsave("/Users/Xin/Desktop/IC_project/output/Jan222016/DS2_1_ICC_taxa70.png", width = 25, height = 15)

ggplot(DS2_2_ICC, aes(x = reorder(taxa, Percent), y = Percent, fill =  Sample)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1") + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 15),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) + xlab("Taxa")  
ggsave("/Users/Xin/Desktop/IC_project/output/Jan222016/DS2_2_ICC_taxa70.png", width = 25, height = 15)
