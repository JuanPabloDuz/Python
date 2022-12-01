#!/usr/bin/env python3.7
#7 input
name =  input("name? ")
color = input("favorite color? ")
age = int(input("how old are you? "))

# print(name, end=" ")
# print("is " + str(age) + " years old", end=" ")
# print("favorite color of " + str(name) + " is " + str(color) + ".", end=" ")

print(name, 'is', age, 'years old and loves the color', color + '.', sep=" ")