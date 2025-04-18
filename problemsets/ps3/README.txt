Brendan Lewis m263708

Sources:
https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
https://www.w3schools.com/python/ref_string_isnumeric.asp
https://www.w3schools.com/python/python_ref_dictionary.asp
https://www.w3schools.com/python/ref_func_sorted.asp

Explanation of how my program works:
This program sorts people into their respective companies for rooom assignment. It works by first reading through all of the input and storing it in a list. As it reads through it stores the number of people in each company. After these numbers are collected "buckets" are assigned to them, the program looks at a portion of the array and figures out which company has the most people already within the bucket. Once each bucket is assigned, the algorithm looks for perfect swaps ( swaps where after the swap both elements are in the right bucket), and if it can't find them then it will begin doing imperfect swaps where only one element is moved to the right location. Through the maxmimization of perfect swaps, this program uses less swaps than selection sort.

How I came up with the idea:
My intention when deciding how to decrease the number of swaps was to
maximize the number of perfect swaps that I used. In order to know when
a swap would be perfect I needed some way to determine where each
company was supposed to go. So to solve that I figured out a way to put
specific ranges of the data into buckets and then from there I did all
the perfect swaps available. Once these we're all complete, I started to
do imperfect swaps, but in order to maximize perfect swaps I would check
the element of the swap that went to the wrong company area to see if
it's new location allowed for a perfect swap.

Runtime Analysis Using K and N:
There are a couple main cases to consider to find overall runtime
1 - Input             -> O(n)
2 - Sorting Companies -> O(klog(k)) #This is because sorted uses timsort
3 - Assigning Buckets -> O(n)
4 - Swapping :
    4.1 the While loop            -> O(n) 
        #this is O(n) in the worst case where all
        elements are misplaced and only one element is
        corrected over each iteration. This is highly
        unlikely, and the program is written so this
        wouldn't happen. On average this will run
        significantly less iterations. Therefore for big
        theta I will assume it is closer to log(n). it is 
        Big-Omega of 1 because if there are all perfect swaps
        this loop will only be called twice.
    4.2 For loop #1               -> O(n)
        This will run n times everytime it is called
    4.3 For k in pointers         -> O(k)
        This will run k times each time it is called
    4.4 for k in range(companies) -> O(n/k)
        This will run when there is a swap found, so it will
        not be called every iteration through n, but when it 
        it called n/k time is used.
Big-O     = (n^3)
Big-Theta = (n^2log(n))
Big-Omega = (nk)

Swap Analysis Using K and N:
Big-O     = (n) # This will run atmost n - c times, where c is the
                # of already correctly sorted elements
Big-Theta = (n) # The worst case is O(n) similar to selection sort,
                # however, by optimizing perfect swaps the constant
                # value is lowered.
Big-Omega = (0) # In the case that the list is already sorted
