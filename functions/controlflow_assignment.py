# Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50. 

def even_number():
    z = 0
    while z<=50:
        z+=1
        if z%2!=0:
            continue
        print(z)

# Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.


def sum_even_numbers(numbers):
     num = 0
     for n in numbers:
          if n % 2 == 0:
              num += n
     print(num)

# Write a function that takes any two integers as input, and 
# prints the sum of all the numbers between the two integers 
# (inclusive) that are divisible by 3.

def two_nums(a,b):
    numbs = 0
    x = range(a,b)
    for n in x:
        if n % 3 == 0:
            numbs += n
    print(numbs)

# Write a function that takes an integer argument 
# and prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.

def primenumbers(num):
    if(num<=1):
        print("not prime")
    elif(num>1):
        for i in range(2,num):
            if num % i ==0:
                print("not prime")
                break
        else:
            print("prime")
