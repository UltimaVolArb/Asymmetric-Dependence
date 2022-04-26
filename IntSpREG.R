
library(readxl)
library(ggpubr)
library(urca)
DBP <- read_excel("D:/Stony Brook AMS/AMS 2022 Spring/AMS517/AMS517 project/Paper 6 draft/DBP.xlsx")
View(DBP)
DF<-as.data.frame(DBP)

T5YFF<-DBP$T5YFF
T10Y2Y<-DBP$T10Y2Y

pcr <- cor.test(T10Y2Y, T5YFF, 
                method = "pearson")
pcr


kcr<-cor.test(T10Y2Y, T5YFF,  method="kendall")
kcr

scr <-cor.test(T10Y2Y, T5YFF,  method = "spearman")
scr

#Johansen cointegration
jotest=ca.jo(data.frame(T10Y2Y, T5YFF), type="trace", K=2, ecdet="none", spec="longrun")
summary(jotest)