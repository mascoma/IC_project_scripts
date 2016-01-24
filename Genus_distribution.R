library(data.table)
library(ggplot2)
DS2_1 = read.table("./genus/DS2_1_genus.txt", header = T)
DS2_2 = read.table("./genus/DS2_2_genus.txt", header = T)
ICC = read.table("./genus/ICC_genus.txt", header = T)
head(DS2_1)
head(DS2_2)
head(ICC)
Sample = "DS2_1"
DS2_1_percent = Percent = (DS2_1[, 2]/sum(DS2_1[,2]))*100
DS2_1 = cbind(DS2_1, Percent)
DS2_1 = cbind(DS2_1, Sample)

Sample = "DS2_2"
DS2_2_percent = Percent = (DS2_2[, 2]/sum(DS2_2[,2]))*100
DS2_2 = cbind(DS2_2, Percent)
DS2_2 = cbind(DS2_2, Sample)

Sample = "ICC"
ICC_percent = Percent = (ICC[, 2]/sum(ICC[,2]))*100
ICC = cbind(ICC, Percent)
ICC = cbind(ICC, Sample)

head(DS2_1)
head(DS2_2)
head(ICC)

DS2_1_ICC = rbind(DS2_1, ICC)
DS2_2_ICC = rbind(DS2_2, ICC)


ggplot(DS2_1_ICC, aes(x = reorder(genus, Percent), y = Percent, fill =  Sample)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1") + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 15),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) + xlab("Genus")  
ggsave("ICC_DS2_1_distribution_genus.png", width = 25, height = 15)

ggplot(DS2_2_ICC, aes(x = reorder(genus, Percent), y = Percent, fill =  Sample)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1") + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 15),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) + xlab("Genus")  
ggsave("ICC_DS2_2_distribution_genus.png", width = 25, height = 15)




df1 = ICC[, 3] - DS2_1[, 3]
df2 = ICC[, 3] - DS2_2[, 3]

ICC = cbind(ICC, df1)
ICC = cbind(ICC, df2)
head(ICC)
abundance1= vector("numeric", length(df1))
for (i in 1: length(df1)){
  if (df1[i] > 0) {
    abundance1[i] = df1[i] + 0.05
  }
  if (df1[i] < 0) {
    abundance1[i] = 0.05  
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




ggplot(ICC, aes(x = reorder(genus, df1), y = df1, fill =  fill1)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1") +
  geom_text(aes(y= abundance1+ 0.02, label = round(DS2_1_percent, 2)), size = 5 ) + geom_text(aes(y= abundance1 +0.15, label = round(ICC_percent, 2)), size = 5 ) +
  scale_fill_manual(values=c("#CCEEFF", "#FFDDDD"), guide=FALSE) + 
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 15),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) + xlab("Genus") + ylab("Changes of percentage after feeding DS2-1")
ggsave("ICC_DS2_1_genus_changes.png", width = 25, height = 15)

ggplot(ICC, aes(x = reorder(genus, df2), y = df2, fill =  fill2)) + 
  geom_bar(stat = "identity",position = "dodge",  colour = "black") + scale_fill_brewer(palette = "Pastel1") + 
  geom_text(aes(y= abundance2+0.02, label = round(DS2_2_percent, 2)), size = 5 ) + 
  geom_text(aes(y= abundance2 + 0.15, label = round(ICC_percent, 2)),size = 5 ) + scale_fill_manual(values=c("#CCEEFF", "#FFDDDD"), guide=FALSE) +
  theme(axis.text.x = element_text(angle=75, hjust=1, size = 15),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_line(colour="grey60", linetype="dashed")) +  
  xlab("Genus") + ylab("Changes of percentage after feeding DS2-2")
ggsave("ICC_DS2_2_genus_changes.png", width = 25, height = 15)
