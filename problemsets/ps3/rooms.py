#!/usr/bin/python3
#Brendan Lewis

#I want to store the number of people in each company, then just check to make
#sure that the slot I'm looking at as I iterate through has the correct
#alphabetical company. If not swap.
import sys

#Sources 
#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
#https://www.w3schools.com/python/ref_string_isnumeric.asp
#print("we're running")



##### Function to that follows the place we swapped to to see if it
## can also be swapped
##returns 1 or 0 depending on if there was a successful swap
def check_perfect_swap( index, co, num_swaps ):
    global array, pointers, companies
    '''
    co    - the company that the current pointer is pointing to.
    index - the place we just swapped with now we want to check and
    see if this new location has a perfect swap available
    num_swaps - used to check and see if there are still swaps
    happening
    '''
    #print("checking for perfect swap")

    #now intc stores the value of the company we should be looking
    #at 


    ##actual company that our number is supposed to be in
    actual_co = array[index].split(" ")[0]
    

    for k in range(companies[actual_co]):
        target = k + pointers[actual_co] 
        target_co = array[target][0] 
        if target_co == str(co):
            #print("PERFECT SWAPPPP, we're looking at " +
            #        str(expected_c))
            #print("the swap is    " + array[target] +"  " + array[index])
            #for a in array:
            #    print(a, end="") 
            #print()
            swaps.append(array[k] + " " + array[i])
            perfect_swaps.append(array[k] + " " + array[index])
            temp = array[index]
            array[index] = array[k]
            array[k] = temp
            #for a in array:
            #    print(a, end="") 
            #print()
            return 1

    return 0




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
        #print(pointers)
        #print(j)
    #print(pointers.keys())
    #print("temp_dict == " + str(temp_dict))
    if not temp_dict:
        for z in dictionary:
            #print(z + " -> ", end="")
            if z not in pointers:
                #print("choosing company " + z)
                max_k = z
                break

    else:
        max_k = max(temp_dict, key=temp_dict.get)
    #print("MAXK = " + max_k)
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
#print("pointers  --- " + str(pointers))
#print("companies --- " + str(companies))

swaps = []
perfect_swaps = []
expected_c = 0
num_swaps = 1
p = 0
while(num_swaps > 0):
    num_swaps = 0
    for i in range(len(array)):
        

        old_k = 0
        for k in pointers:
            #print("i == " + str(i) + "  k == " + str(k) + "  t == " + str(t) + "  pointers_k == " +
            #    str(companies[k]))
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
                      
            for k in range(companies[actual_co]):
                #print(k + pointers[actual_co]) 
                target = k + pointers[actual_co]  
                if str(expected_c) == array[target][0]:
                    num_swaps += 1
                    ################ Perform Swap ####################
                    #print("PERFECT SWAPPPP, we're looking at " +
                    #        str(c))
                    #print("the swap is    " + array[k + pointers[actual_co]] +"  " + array[i])
                    swaps.append(array[i] + " " + array[k + pointers[actual_co]])
                    perfect_swaps.append(array[i] + " " + array[k + pointers[actual_co]])
                    temp = array[k + pointers[actual_co]]
                    array[k + pointers[actual_co]] = array[i]
                    array[i] = temp
                    break
                    
                #p is used to tell which iteration of swaps we're on

                elif p >= 1 and array[k + pointers[actual_co]][0] != actual_co:
                    num_swaps += 1
                    #for a in array:
                    #    print(a, end="") 
                    #print()
                    ################ Perform Swap ####################
                    #print("performing non_perfect swap, we're looking at "
                    #        +str(expected_c))
                    #print("the swap is    " + array[k + pointers[actual_co]] +"  " + array[i])
                    swaps.append(array[i] + " " + array[k +
                        pointers[actual_co]])
                    temp = array[k + pointers[actual_co]]
                    array[k + pointers[actual_co]] = array[i]
                    array[i] = temp
                    #print("\n after swap\n")
                    #for a in array:
                    #    print(a, end="")
                    #print()
                    num_swaps += check_perfect_swap(i,expected_c, num_swaps)      
                    break               
                    
            #print(len(swaps))

    p += 1        
    
    #prints the whole list after swaps
    #for i in array:
    #    print(i, end="")


for i in swaps:
    print( i.split(" ")[1].strip("\n")+ " " + i.split(" ")[3], end="")
#print(len(swaps))


#print("pef swaps")
#for i in perfect_swaps:
#    print( i.split(" ")[1].strip("\n")+ " " + i.split(" ")[3], end="")
#print(len(perfect_swaps))





