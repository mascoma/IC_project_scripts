library(ggplot2)
 
# make plot

dat1<-read.table("DS2-1_R1_N_output.txt", sep='\t', header = T)
h<-ggplot(dat1, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("N703 seq in DS2-1_R1 (counts 5084)")
ggsave("indexSeqPos_DS2-1_R1_N.jpg")
 
dat2<-read.table("DS2-1_R1_S_output.txt", sep='\t', header = T)
h<-ggplot(dat2, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("S503 seq in DS2-1_R1 (counts 4823)")
ggsave("indexSeqPos_DS2-1_R1_S.jpg")
 
 
dat3<-read.table("DS2-1_R2_N_output.txt", sep='\t', header = T)
 
h<-ggplot(dat3, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("N703 seq in DS2-1_R2 (counts 4161)")
ggsave("indexSeqPos_DS2-1_R2_N.jpg")

dat4<-read.table("DS2-1_R2_S_output.txt", sep='\t', header = T)

h<-ggplot(dat4, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("S503 seq in DS2-1_R2 (counts 4936)")
ggsave("indexSeqPos_DS2-1_R2_S.jpg")

 
#######################################


dat5<-read.table("DS2-2_R1_N_output.txt", sep='\t', header = T)
h<-ggplot(dat5, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("N704 seq in DS2-2_R1 (counts 7246)")
ggsave("indexSeqPos_DS2-2_R1_N.jpg")

dat6<-read.table("DS2-2_R1_S_output.txt", sep='\t', header = T)
 
h<-ggplot(dat6, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("S503 seq in DS2-2_R1 (counts 4431)")
ggsave("indexSeqPos_DS2-2_R1_S.jpg")

dat7<-read.table("DS2-2_R2_N_output.txt", sep='\t', header = T)

h<-ggplot(dat7, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("N704 seq in DS2-2_R2 (counts 5711)")
ggsave("indexSeqPos_DS2-2_R2_N.jpg")

dat8<-read.table("DS2-2_R2_S_output.txt", sep='\t', header = T)

h<-ggplot(dat8, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("S503 seq in DS2-2_R2 (counts 4392)")
ggsave("indexSeqPos_DS2-2_R2_S.jpg")

##########################################

dat1<-read.table("ICC_R1_N_output.txt", sep='\t', header = T)
h<-ggplot(dat1, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("N701 seq in ICC_R1 (counts 2348)")
ggsave("indexSeqPos_ICC_R1_N.jpg")
 
dat2<-read.table("ICC_R1_S_output.txt", sep='\t', header = T)

h<-ggplot(dat2, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("S502 seq in ICC_R1 (counts 2912)")
ggsave("indexSeqPos_ICC_R1_S.jpg")
 
dat3<-read.table("ICC_R2_N_output.txt", sep='\t', header = T)

h<-ggplot(dat3, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("N701 seq in ICC_R2 (counts 1368)")
ggsave("indexSeqPos_ICC_R2_N.jpg")


dat4<-read.table("ICC_R2_S_output.txt", sep='\t', header = T)

h<-ggplot(dat4, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("S502 seq in ICC_R2 (counts 2905)")
ggsave("indexSeqPos_ICC_R2_S.jpg")

 
############################################


dat5<-read.table("ICW_R1_N_output.txt", sep='\t', header = T)

h<-ggplot(dat5, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("N706 seq in ICW_R1 (counts 2889)")
ggsave("indexSeqPos_ICW_R1_N.jpg")

dat6<-read.table("ICW_R1_S_output.txt", sep='\t', header = T)
 
h<-ggplot(dat6, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("S504 seq in ICW_R1 (counts 2553)")
ggsave("indexSeqPos_ICW_R1_S.jpg")
 
dat7<-read.table("ICW_R2_N_output.txt", sep='\t', header = T)

h<-ggplot(dat7, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("N706 seq in ICW_R2 (counts 2094)")
ggsave("indexSeqPos_ICW_R2_N.jpg")

 
dat8<-read.table("ICW_R2_S_output.txt", sep='\t', header = T)

h<-ggplot(dat8, aes(x = Start))
h <- h + geom_histogram(binwidth = 1, fill = "darkblue", color = "ghostwhite") 
h + xlab("Position") + ggtitle("S504 seq in ICW_R2 (counts 2581)")
ggsave("indexSeqPos_ICW_R2_S.jpg")
 