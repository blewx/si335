#!/usr/bin/python3
#Brendan Lewis

"""
This program sorts people into their respective companies for rooom assignment. It works by first 
reading through all of the input and storing it in a list. As it reads through it stores the number
of people in each company. After these numbers are collected "buckets" are assigned to them, the 
program looks at a portion of the array and figures out which company has the most people already within
the bucket. Once each bucket is assigned, the algorithm looks for perfect swaps ( swaps where after the swap
both elements are in the right bucket), and if it can't find them then it will begin doing imperfect swaps
where only one element is moved to the right location. Through the maxmimization of perfect swaps,
this program uses less swaps than selection sort.
"""


#Sources 
#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
#https://www.w3schools.com/python/ref_string_isnumeric.asp
#https://www.w3schools.com/python/python_ref_dictionary.asp
#https://www.w3schools.com/python/ref_func_sorted.asp

"""
This function is called after an imperfect swap. It checks to see if the person we just swapped has a 
perfect swap opportunity. If they do, it will swap them and return 1 implying that a swap happened
"""
def check_perfect_swap( index, co, num_swaps ):
    global array, pointers, companies
    '''
    co    - the company that the current pointer is pointing to.
    index - the place we just swapped with now we want to check and
    see if this new location has a perfect swap available
    num_swaps - used to check and see if there are still swaps
    happening
    '''

    actual_co = array[index].split(" ")[0]

    for k in range(companies[actual_co]):
        target = k + pointers[actual_co] 
        target_co = array[target][0] 
        
        
        if target_co == str(co):

            swaps.append(array[k] + " " + array[index])
           
             
            dummy_swaps.append(array[k] + " " + array[index])
            temp = array[index]
            array[index] = array[k]
            array[k] = temp
            return 1

    return 0

import sys


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




sorted_comp = sorted(companies.items(), key = lambda x:x[1])
dictionary = dict(sorted_comp)


#pointers stores the offsets for the beginning of each bucket for each company
pointers = {}


#create the pointers by traversing through the input and finding which company
#has the biggest percentage of people already in a bucket before assigning the bucket
#to a specific company
k = 0
for i in dictionary:

    temp_dict = {}
    for z in dictionary:
        if z not in pointers:
            i = z
            break

    for j in range(dictionary[i]):
        if array[k].split(" ")[0] not in pointers:
            if array[k].split(" ")[0] in temp_dict:
                val = temp_dict[array[k].split(" ")[0]] + 1
                temp_dict.update({array[k].split(" ")[0]:val})
            else:
                temp_dict.update({array[k].split(" ")[0]:1})
        k += 1

    if not temp_dict:
        for z in dictionary:
            if z not in pointers:
                max_k = z
                break

    else:
        max_k = max(temp_dict, key=temp_dict.get)

    k = k - dictionary[i] + companies.get(max_k)

    pointers.update({max_k: k-companies.get(max_k)})

''' Now that pointers are assigned, do math to figure out where you should be
looking to swap. iterate through the array and then when found a company in wrong the wrong buckey
, look in the correct bucket for the company and try to swap using the pointers, but if you
can't do it then wait and continue to loop through to find perfect swaps then
afterwards go back and make non perfect swaps'''
swaps = []
perfect_swaps = []
dummy_swaps = []
expected_c = 0
num_swaps = 1
num_iterations = 0
while(num_swaps > 0):
    num_swaps = 0
    for i in range(len(array)):
        old_k = 0
        for k in pointers:
            if i < int(companies[k]) + old_k:
                expected_c = int(k)
                break
            else:
                old_k += companies[k]
        # code above sets c so that it is the value of the company it should be

        #now we want to see where the most effective swap would be if we have somone
        #that is in the wrong area for their company
        actual_co = array[i].split(" ")[0]
        if str(expected_c) != actual_co:
            bruh= companies[actual_co] 
            
            for k in range(companies[actual_co]):
                target = k + pointers[actual_co] 
                target_co = array[target][0] 
                if str(expected_c) == target_co:
                    num_swaps += 1
                    
                    ################ Perform Swap ###################
                    swaps.append(array[i] + " " + array[k + pointers[actual_co]])
                    perfect_swaps.append(array[i] + " " + array[k + pointers[actual_co]])
                    temp = array[k + pointers[actual_co]]
                    array[k + pointers[actual_co]] = array[i]
                    array[i] = temp
                    break

                #num_iterations is used to tell which iteration of swaps we're on, on the first iteration
                # we only want to do perfect swaps hence the num_iterations >=1

                elif num_iterations >= 1 and array[k + pointers[actual_co]].split(" ")[0] != actual_co:
                    num_swaps += 1
                    
                    ################ Perform Swap ####################
                    
                    swaps.append(array[i] + " " + array[k +
                        pointers[actual_co]])
                    temp = array[k + pointers[actual_co]]
                    array[k + pointers[actual_co]] = array[i]
                    array[i] = temp
                   
                    num_swaps += check_perfect_swap(i,expected_c, num_swaps)      
                    break               
    num_iterations += 1        


#Print the output
for i in swaps:
    print( i.split(" ")[1].strip("\n")+ " " + i.split(" ")[3], end="")





