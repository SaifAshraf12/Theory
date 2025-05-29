'''# create a new python program that accept an integer value and return its fictorial
def factorial(n):
    f = 1
    for i in range (1,n+1):
        f*=i
    return f
s= input('Enter a number')
n=int(s)
print('factorial of', n, 'is ',factorial(n))
      
# write a function to accept two integers from user and return their sum
def sum(a,b):
    s=a+b
    return s
num1 = int(input('Enter first number'))
num2 = int(input('Enter 2nd number'))
sumation = sum(num1,num2)
print('Sum of given numbers is', sumation)


# Checking the given value is prime number or not
def prime(n):
    num = True
    for i in range(2,n):
        if n%i == 0:
            num = False
            break
    return num
s = input('Enter a number')
if prime(int(s))== True:
    print('Prime')
else:
    print('Not Prime')

'''
# accepts list of integers and return sum of its elements
def sum(list):
    s = 0
    for i in list:
        s+=i
    return s
list1 = [1,2,3,4,5,6,7,8,9,10]
sum = sum(list1)
print('Sum of elements of list is', sum)

# accept a list of integers and sort it in descending order
def list_sort(list):
    list.sort()
    list.reverse()
mylist = [2,45,67,12,89]
print('The given list is', mylist)
list_sort(mylist)
print('Sorted list is', mylist)
list_sort(mylist)
