library(data.table)
library(ggplot2)
ICC = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_genus_graph2.csv",stringsAsFactors = F, header = T, sep = ",")
ICC_DS2_1 = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_1_unmapped_genus_graph2.csv",stringsAsFactors = F, header = T, sep = ",")
ICC_DS2_2 = read.delim("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_2_unmapped_genus_graph2.csv",stringsAsFactors = F, header = T, sep = ",")
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

df1 = ICC_DS2_1[, 3] - ICC[, 3]
df2 = ICC_DS2_2[, 3] - ICC[, 3]

ICC = cbind(ICC, df1)
ICC = cbind(ICC, df2)
head(ICC)
abundance1= vector("numeric", length(df1))
for (i in 1: length(df1)){
  if (df1[i] > 0) {
    abundance1[i] = df1[i] + 0.1
  }
  if (df1[i] < 0) {
    abundance1[i] = 0.1
  } 
}

abundance2= vector("numeric", length(df2))
for (i in 1: length(df2)){
  if (df2[i] > 0) {
    abundance2[i] = df2[i] + 0.1
  }
  if (df2[i] < 0 || df2[i] == 0) {
    abundance2[i] = 0.1
  } 
}


fill1 = vector("character", length(df1))
for (i in 1: length(df1)){
  if (df1[i] > 0) {
    fill1[i] = "P"
  }
  if (df1[i] < 0) {
    fill1[i] = "N"
  } 
}

fill2 = vector("character", length(df2))
df22 = reorder(ICC[, "df2"], ICC[, "df1"])
df22 = as.vector(df22)
df22 = as.numeric(df22)
for (i in 1: length(df2)){
  if (df2[i] > 0) {
    fill2[i] = "P"
  }
  if (df2[i] < 0 || df2[i] == 0) {
    fill2[i] = "N"
  } 
}




ggplot(ICC, aes(x = reorder(taxa, df1), y = df1, fill =  fill1)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1") +
  geom_text(aes(y= abundance1+ 0.2, label = round(ICC_DS2_1_percent, 1)), size = 6 ) + geom_text(aes(y= abundance1 +0.7, label = round(ICC_percent, 1)), size = 6 ) +
  scale_fill_manual(values=c("darksalmon","darkseagreen4"), guide=FALSE) + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) + xlab("") + ylab("Changes of percentage") +
  theme(axis.title.y = element_text(size =20)) 
ggsave("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_1_unmapped_changes.png", width = 25, height = 15)

ggplot(ICC, aes(x = reorder(taxa, df2), y = df2, fill =  fill2)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1") + 
  geom_text(aes(y= abundance2+0.2, label = round(ICC_DS2_2_percent, 1)), size = 6 ) + 
  geom_text(aes(y= abundance2 + 0.7, label = round(ICC_percent, 1)),size = 6 ) + scale_fill_manual(values=c("darksalmon","darkseagreen4"), guide=FALSE) +
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 20),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) +  xlab("") + ylab("Changes of percentage") +
  theme(axis.title.y = element_text(size =20)) 
ggsave("/Users/Xin/Desktop/IC_project/output/Jan222016/ICC_DS2_2_unmapped_changes.png", width = 25, height = 15)

