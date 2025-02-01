#!/usr/bin/python3
#Brendan Lewis

#I want to store the number of people in each company, then just check to make
#sure that the slot I'm looking at as I iterate through has the correct
#alphabetical company. If not swap.
import sys

#Sources 

#https://www.w3schools.com/python/ref_string_isnumeric.asp
array []
user_input = sys.stdin.readline()
while(user_input.split(" ")[0].isnumeric()):
    array.append(user_input)
    user_input = sys.stdin.readline()

print(array)

