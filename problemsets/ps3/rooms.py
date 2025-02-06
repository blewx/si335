#!/usr/bin/python3
#Brendan Lewis

#I want to store the number of people in each company, then just check to make
#sure that the slot I'm looking at as I iterate through has the correct
#alphabetical company. If not swap.
import sys

#Sources 
#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
#https://www.w3schools.com/python/ref_string_isnumeric.asp
print("we're running")
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
    
#Tried to do buckets but this doesn't work perfectly so I'm going to store an
# array of pointers to point to where each company is stored
#for i in companies:
    #print(type(i))
    #print(str(i) + " " + str(companies[i]))

sorted_comp = sorted(companies.items(), key = lambda x:x[1])
dictionary = dict(sorted_comp)

#print(dictionary)

pointers = {}
k = 0
#for i in range(len(companies)):
    #runs the number of times
for i in dictionary:
    #print(i)
    #print(dictionary[str(i)])
    temp_dict = {}
    #we want to change i 
    for z in dictionary:
        if z not in pointers:
            i = z
            break
    #print("dictionary[ " + i + "] === " + str(dictionary[i]))
    for j in range(dictionary[i]):
        #print(str(k) + "  -- ", end="")
        #here is where we want to do the thingy
        #print(array[k])
        if array[k].split(" ")[0] not in pointers:
            if array[k].split(" ")[0] in temp_dict:
                val = temp_dict[array[k].split(" ")[0]] + 1
                temp_dict.update({array[k].split(" ")[0]:val})
            else:
                temp_dict.update({array[k].split(" ")[0]:1})
        k += 1
    max_k = max(temp_dict, key=temp_dict.get)
    #print(" BIG HAYYYYYY " + str(companies.get(max_k)))
    

    #if companies.get(max_k) > dictionary[i]:
    k = k - dictionary[i] + companies.get(max_k)
    
    pointers.update({max_k: k-companies.get(max_k)})
    #dictionary.pop(max_k)

    #print("pointers --- " + str(pointers))
    #print(str(temp_dict) + " ---- " + str(max_k))


    #print()
    #print(k)

''' now that pointers are assinged, do math to figure out where you should be
looking to swap'''


''' iterate through the array and then when found num in wrong category, look in
the correct bucket for the num and try to swap using the pointers, but if you
can't do it then wait and continue to loop through to find perfect swaps then
afterwards go back and make non perfect swaps'''
print("pointers  --- " + str(pointers))
print("companies --- " + str(companies))
c = 0
num_in_company_counted = 0
t = -1
for i in range(len(array)):
    old_k = 0
    for k in pointers:
        print("i == " + str(i) + "  k == " + str(k) + "  t == " + str(t) + "  pointers_k == " +
              str(pointers[k]))
        if t == 0:
            c = int(old_k)
            break
        if i < pointers[k]:
            c = int(k)
            break
        t -= 1
        old_k = k
    t = pointers[str(c)] 
    print(c)
    
    '''if array[i].split(" ")[0] != str(c):
        k = i + 1
        while array[k].split(" ")[0] != str(c):
            k += 1

        #swappppppp
        print(str(array[i].split(" ")[1].strip()) + " " + str(array[k].split(" ")[1].strip()))
        temp = array[i]
        array[i] = array[k]
        array[k] = temp
    num_in_company_counted+= 1
    '''

#prints the whole list after swaps
#for i in array:
#    print(i, end="")
