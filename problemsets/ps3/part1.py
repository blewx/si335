#!/usr/bin/python3
#Brendan Lewis

#I want to store the number of people in each company, then just check to make
#sure that the slot I'm looking at as I iterate through has the correct
#alphabetical company. If not swap.
import sys

#Sources 

#https://www.w3schools.com/python/ref_string_isnumeric.asp
array = []
companies = {} #k = company number , v = num ppl in company
user_input = sys.stdin.readline()
while(user_input.split(" ")[0].isnumeric()):
    array.append(user_input)
    if user_input.split(" ")[0] in companies:
        val = companies[user_input.split(" ")[0]] + 1
        companies.update({user_input.split(" ")[0]:val})
    else:
        companies.update({user_input.split(" ")[0]:1})
    user_input = sys.stdin.readline()
    
print(array)
print(companies)
num_in_company_counted = 0
c = 1 #which company we're using first
for i in range(len(array)):
    print(str(c) + " ___ " + str(i) + " ____ " + str(len(array)))
    if array[i].split(" ")[0] != str(c):
        k = i + 1
        while array[k].split(" ")[0] != str(c):
            k += 1

        #swappppppp
        temp = array[i]
        array[i] = array[k]
        array[k] = temp
        print(array)
    num_in_company_counted+= 1

    if num_in_company_counted == companies[str(c)]:
        num_in_company_counted = 0
        c += 1
    print()
    print(array)
    print()
print(array)
print(companies)
