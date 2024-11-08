# Name: Jay Razdan

####################
### Exercise 3.1 ###
####################

# For such a described binary search algorithm, on a list of length n, the worst case scenario would be searching for a value with index either equal to 0 or -1 i.e. the first and last elements of the list;
# In other words, the question is to find out the number of times we recursively call the function till our index k is equal to 0;
# Generally, for any k-th recursion, the search space of the list, as we search for the first element of the list, is: A_k = [A[0],..., A[(n/2**k)-1]], for all k = 0, 1, 2,...;
# So, our problem then becomes: Find the x for which the limit of (n/2**k)-1) equals 0, as k approaches x;
# Solving this limit equation yields that: x = log_2(n);
# Therefore, for the worst case scenario, on a list of length n, the described binary search algorithm has to perform "log_2(n)" comparisons. 

####################
### Exercise 3.2 ###
####################

def binsearch(key,x,i,j):
    # finding the floor of the midpoint k between the lower and upper bounds, i and j
    k = (i+j)//2
    # if the requested key lies beyond the upper bound, then it should be placed at index equal to the length of the list
    if key > x[-1]:
        return len(x)
    # if the requested key is does not exist in the list, and is less than the last element of the list; 
    # Then, we recursively call the function as usual, but till the lower bound i exceeds the upper bound j such that i is the index where such a key should exist
    elif i > j:
        return i
    # if we find the requested key, we'll consider two cases:
    if key == x[k]:
        # if the key is the first of its kind in the list, then it is either the first element in the list or the element to the left of it is distinct
        if x[k-1] != key or k==0:
            return k
        # otherwise, recursively call the function with a shifted upper bound 
        else:
            return binsearch(key,x,i,k-1)
    # if the requested key is less than the value of the index equal to midpoint k, recursively call the function with a shifted upper bound 
    elif key < x[k]:
        return binsearch(key,x,i,k-1)
    # if the requested key is greater than the value of the index equal to midpoint k, recursively call the function with a shifted lower bound 
    elif key > x[k]:
        return binsearch(key,x,k+1,j)
    
####################
### Exercise 3.3 ###
####################

def test():
    ### Testing the binsearch() function ###
    test_request = "B"
    # we call the respective list
    if test_request == "A":
        test_list = [7,7,10,23,42,42,42,51,60]
    elif test_request == "B":
        test_list = list(range(1 , 200000000 , 2))
    elif test_request == "C":
        test_list = [9] * (10**8)
    request = int(12500001)
    # define a list of length greater than 100 as large
    if len(test_list) > 100:
        # since the list must be non-decreasing, a list with identical entries will have the same first and last element
        if test_list[0] == test_list[-1]:
            print(f"Testing a large list with {len(test_list)} identical entries: {test_list[0]}, {test_list[1]}, {test_list[2]} ... {test_list[-1]}")
        else:
            print(f"Testing a large list with {len(test_list)} entries: {test_list[0]}, {test_list[1]}, {test_list[2]} ... {test_list[-1]}")
    # otherwise, it is defined as small
    else:
        print(f"Testing a small list: {test_list}")
    # calling the binsearch function
    result = binsearch(key=request, x=test_list, i=0, j=len(test_list))
    # we output a statement according to whether the requested key is in the test list
    if request not in test_list:
        print(f"Key {request} not found, should be at index {result}.")
    else:
        print(f"Key {request} found at index {result}.")

    ### Testing the insert() function ###
    final_list = insert(key=request, x=test_list)
    test_list.append(request)
    test_list.sort()
    if final_list == test_list:
        return "The insert() function works! :)"
    else:
        return "The insert() function doesn't work :("

####################
### Exercise 3.4 ###
####################

def insert(key,x):
    # the index of the key to be inserted into the list is the output of the binsearch function
    index = binsearch(key=key, x=x, i=0, j=len(x))
    # the key is inserted at this index
    y = x[:index] + [key] + x[index:]
    return y

######################
### Testing Output ###
######################
Test = test()
print(Test)
