#!/usr/bin/env python3
N = 10
sum = 0
count = 0
print("Please input 10 numbers:")
while N > count:
    number = float(input("Please input the {} number:".format(count+1)))
    sum = sum + number
    count = count + 1
average = sum / N
print("N = {}, sum = {}".format(N,sum))
print("Average = {:.2f}".format(average))
