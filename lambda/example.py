#!/usr/bin/env python
#coding=utf-8

'''
使用lambda表达式, 按照人口大小升序显示
'''

countries = []

with open('countries_zh.csv') as f:
    for line in f:
        line = line.strip()
        arr = line.split(',')
        country = arr[1]
        capital = arr[3]
        population = int(arr[4])
        countries.append( (country, capital, population) )

countries.sort(key=lambda country: country[2])

for country in countries:
    print(str(country).decode('string-escape'))
