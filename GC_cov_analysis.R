library(dplyr)
library(ggplot2)
cov = read.csv("/Users/Xin/Desktop/IC_project/output/Feb222016/Halonotius_J07HN6_cov.csv")
GC = read.csv("/Users/Xin/Desktop/IC_project/output/Feb222016/Halonotius_J07HN6_GC.csv")
cov  =  cov[, 1:2]
GC = GC[, 1:2]
GC_cov_inner = inner_join(GC, cov, by = "Position")
names(GC_cov_inner) = c("position", "GC", "coverage")
GC_cov_inner$position = as.numeric(row.names(GC_cov_inner))
str(GC_cov_inner)

GC_cov_inner2 = GC_cov_inner
indx <- sapply(GC_cov_inner, is.factor)
GC_cov_inner[indx] <- lapply(GC_cov_inner[indx], function(x) as.numeric(as.character(x)))

#plot(GC_cov_inner[, 1], (GC_cov_inner[,2]*100), xlim = c(0, 2600000), ylim = c(0, 450), type = "l", col = "gray50")
#lines(GC_cov_inner[, 1], GC_cov_inner[,3], col = "lightcoral")
median(GC_cov_inner[,2], na.rm = T)
GC_cov_new = GC_cov_inner[!is.na(GC_cov_inner[,2]),]
plot(GC_cov_new[,2], GC_cov_new[,3], pch = 20, ylab = "coverage", xlab = "GC content", 
     main = "GC content vs coverage for the reads mapped to Halonotius J07HN6", xlim = c(0,1), ylim = c(0, 450))
fit1 = lm(coverage ~ GC, data = GC_cov_new)
summary(fit1)
GC2 = GC_cov_new$GC^2
fit2 = lm(coverage ~ GC + GC2, data = GC_cov_new)
summary(fit2)
anova(fit1, fit2) # p= 0.2766

abline(fit1, lty = "solid", lwd = 2, col = "steelblue4")
abline(fit2, lty = "dashed", lwd = 3, col = "orangered4")
