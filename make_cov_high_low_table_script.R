#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=2) {
  stop("Two argument must be supplied arg[1] = inputfile, arg[2] = outputfile.\n", call.=FALSE)
}  

inputdir <- args[1]
outputdir <- args[2]
dat <- read.csv(inputdir, header = F)
colnames <- c("genome", "start", "end", "cov", "p", "length")
names(dat) <- colnames
head(dat)


colnames2 <- c("genome", "position", "cov")
tmpDF <- vector()
for(j in 1:length(dat[,"start"])){
  tmp = vector()
  for (i in dat[j, "start"]:dat[j, "end"]){
    if (dat[j,4] == "High Coverage"){
      if (length(tmp) == 0){
        tmp <- c(as.character(dat[j,1]),i, "H")
      }
      else{
        tmp <- rbind(tmp, c(as.character(dat[j,1]),i, "H"))
      }   
    }
    if (dat[j,4] == "Low Coverage") {
      if (length(tmp) == 0){
        tmp <- c(as.character(dat[j,1]),i, "L")
      }
      else{
        tmp <- rbind(tmp, c(as.character(dat[j,1]),i, "L"))
      }
    }
  }
  tmp <- as.data.frame(tmp)
  tmpDF <- rbind(tmpDF, tmp)
}

names(tmpDF) <- colnames2

write.table(tmpDF[,1:3], file = outputdir, sep = "\t", quote = FALSE,row.names = FALSE)
