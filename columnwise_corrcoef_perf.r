# R code courtesy Pedro Maat Massolino, https://github.com/pmassolino/

library(Hmisc)
#minimumValue <- -2^(1022)
#maximumValue <- 2^(1022)
minimumValue <- -2^(500)
maximumValue <- +2^(500)
numberOfTraces <- 100000
numberOfSamples <- 1000
numberOfPredictions <- 256
O <- matrix(runif(numberOfTraces*numberOfSamples, min=minimumValue, max=maximumValue), nrow=numberOfTraces, ncol=numberOfSamples)
P <- matrix(runif(numberOfTraces*numberOfPredictions, min=minimumValue, max=maximumValue), nrow=numberOfTraces, ncol=numberOfPredictions)
#print (O)
#print (P)
system.time(cor(O, P, method = "pearson"))
