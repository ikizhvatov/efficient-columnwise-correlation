# R code courtesy Pedro Maat Massolino, https://github.com/pmassolino/

library(Hmisc)
#minimumValue <- -2^(1022)
#maximumValue <- 2^(1022)
minimumValue <- -2^(500)
maximumValue <- +2^(500)
numberOfTraces <- 100000
numberOfSamples <- 1000
numberOfPredictions <- 256

# dummy arrays for the dry run
foo <- matrix(runif(numberOfTraces*numberOfSamples, min=minimumValue, max=maximumValue), nrow=numberOfTraces, ncol=numberOfSamples)
bar <- matrix(runif(numberOfTraces*numberOfPredictions, min=minimumValue, max=maximumValue), nrow=numberOfTraces, ncol=numberOfPredictions)

# arrays representing real data
O <- matrix(runif(numberOfTraces*numberOfSamples, min=minimumValue, max=maximumValue), nrow=numberOfTraces, ncol=numberOfSamples)
P <- matrix(runif(numberOfTraces*numberOfPredictions, min=minimumValue, max=maximumValue), nrow=numberOfTraces, ncol=numberOfPredictions)

print("Dry run...")
system.time(cor(foo, bar, method = "pearson"))

print("Real run...")
system.time(cor(O, P, method = "pearson"))
