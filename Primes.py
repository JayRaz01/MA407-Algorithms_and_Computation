# Name: Jay Razdan, Student Number: 202135075

def primeAtLeast(n):
    if n <= 2: # if n is less than or equal to 2 the closest above prime is 2
        return 2
    if n % 2 == 0: # if n is divisible by 2, then it is even and we add 1 to make n the next odd integer
        n += 1
    count = 1 # initialize a count for the while loop
    while count == 1:
        if primeOrNot(n) == True: # if n is a prime number, then set p=n and de-initialize the count
            p = n
            count -= 1
        else: # otherwise add 2 to make n the next odd integer
            n += 2
    return p 
    
def primeOrNot(n):
    if n <= 1: # there are no prime numbers equal to or less than 1
        return False
    elif n == 2: # 2 is a prime number and is the only even prime number
        return True
    if n % 2 == 0: # even numbers cannot be prime numbers
        return False
    for i in range(3,int(n**0.5),2): # for every number 3 and above until sqrt(n)-1, if n is divisible by it, then n cannot be prime
            if n % i == 0:
                return False
    return True # otherwise, n is a prime number 

# TEST
result = primeAtLeast(n=345414453885)
print(result)