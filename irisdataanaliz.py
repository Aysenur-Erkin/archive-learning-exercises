# -*- coding: utf-8 -*-
# Although the code is saved in a .py file, it is written in R language. Please run it in an R environment.
#Kod .py dosyasinda kaydedilmis olmasina ragmen, R dilinde yazilmistir. Lutfen bir R ortaminda calistirin.

library(ggplot2)

data(iris)
head(iris)
summary(iris)

mean_sepal_length <- mean(iris$Sepal.Length)
median_sepal_length <- median(iris$Sepal.Length)
sd_sepal_length <- sd(iris$Sepal.Length)

cat("Sepal Length Mean:", mean_sepal_length, "\n")
cat("Sepal Length Median:", median_sepal_length, "\n")
cat("Sepal Length Standard Deviation:", sd_sepal_length, "\n")

ggplot(iris, aes(x=Sepal.Length)) +
  geom_histogram(binwidth=0.5, fill="blue", color="black", alpha=0.7) +
  labs(title="Distribution of Sepal Length", x="Sepal Length", y="Frequency")

ggplot(iris, aes(x=Species, y=Sepal.Length, fill=Species)) +
  geom_boxplot() +
  labs(title="Boxplot of Sepal Length by Species", x="Species", y="Sepal Length")

setosa_data <- subset(iris, Species == "setosa")
versicolor_data <- subset(iris, Species == "versicolor")
virginica_data <- subset(iris, Species == "virginica")

mean_setosa_sepal_length <- mean(setosa_data$Sepal.Length)
mean_versicolor_sepal_length <- mean(versicolor_data$Sepal.Length)
mean_virginica_sepal_length <- mean(virginica_data$Sepal.Length)

cat("Setosa Sepal Length Mean:", mean_setosa_sepal_length, "\n")
cat("Versicolor Sepal Length Mean:", mean_versicolor_sepal_length, "\n")
cat("Virginica Sepal Length Mean:", mean_virginica_sepal_length, "\n")