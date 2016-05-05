

dat_slice <- function(dir, inputfile, i, group){ 
    # dir, inputfile, group are strings
    # i is a integer indicating how many rows kept

	directory <- dir
	inputname <- inputfile
	input <-  paste(directory, inputname, sep = '')
	var1 <- read.delim2(input, sep = '\t', header = F, as.is = T)
	var2 <- var1[order(var1[, 2], decreasing = T), ]
	var3 <- sum(var2[, 2])
	var4 <- var3 - sum(var2[1:i, 2])
	var5 <- c(var2[1:i, 2], var4)
	var6 <- (var2[1:i, 1], 'others')
	var7 <- (var5 / var3) *100
	var8 <- cbind(var6, var5, var7, group)
	var8 <- as.data.frame(var8, stringsAsFactors = F)
	names(var8) <- c("taxa", "count", "percent", "group")
	return(var8)
}

