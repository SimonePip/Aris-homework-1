#Say "Hello, World!" With Python
print("Hello, World!")



#Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys

"""    
If is odd, print Weird
If is even and in the inclusive range of [2,5] print Not Weird
If is even and in the inclusive range of [6,20] print Weird
If is even and >20 print Not Weird
"""


if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0: print("Weird")
    if n%2==0 and 2<=n<=5: print("Not Weird")
    if n%2==0 and 6<=n<=20: print("Weird")
    if n%2==0 and n>20: print("Not Weird")
    


#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n): print(i**2)



#Write a function
def is_leap(year):
    leap = False
    if year%4==0 and year%100!=0: leap=True
    if year%4==0 and year%100==0: leap=False
    if year%400==0: leap=True
    
    return leap

"""
In the Gregorian calendar, three conditions are used to identify leap years:
    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year
"""                
    
    
year = int(input())
print(is_leap(year))



#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
l=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                l.append([i,j,k])
print(l)



#Find the Runner-Up Score! 
if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ll=[]
    for i in l:
        if i not in ll: ll.append(i)
print(ll[-2])



#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    query_marks=student_marks[query_name]
    somma=0
    for i in range(len(query_marks)):
        somma+=query_marks[i]
    media=somma/len(query_marks)
    print("%.2f" %media)



#Nested Lists

def noDuplicates(l):
  return list(dict.fromkeys(l))

if __name__ == '__main__':
    names=[]
    grades=[]
    grades_copy=[]
    n=int(input())
    for i in range(0,n):
        names.append(input())
        score = float(input())
        #names[i]=name
        grades.append(score)
        grades_copy.append(score)
    grades_copy.sort()
    grades_copy=noDuplicates(grades_copy)
    low2=grades_copy[1]
    index=[]
    for i in range(0,n):
        if grades[i]==low2:
            index.append(1)
        else: index.append(0)
    final=[]
    for i in range(0,n):
        if index[i]==1: final.append(names[i])
    #print in alphabetic order
    final=sorted(final)
    for i in range(len(final)): print(final[i])



#String Split and Join
def split_and_join(line):
    # write your code here
    split=line.split(" ")
    joint="-".join(split)
    return joint
    
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print("Hello", first_name,last_name+"!","You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
    
#Mutations
def mutate_string(string, position, character):
    l=list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)  
    
    
    
#Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
    

#String Validators
def checking(s):
    checkAlnum, checkAlpha, checkDigit, checkLower, checkUpper=False,False,False,False,False
    
    for i in range(len(s)):
        if s[i].isalnum()==True:
            checkAlnum=True
    for i in range(len(s)):
        if s[i].isalpha()==True:
            checkAlpha=True
    for i in range(len(s)):
        if s[i].isdigit()==True:
            checkDigit=True
    for i in range(len(s)):
        if s[i].islower()==True:
            checkLower=True
    for i in range(len(s)):
        if s[i].isupper()==True:
            checkUpper=True                                    
    return checkAlnum, checkAlpha, checkDigit, checkLower, checkUpper

if __name__ == '__main__':
    s = input()
    #alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. 
    #print (s.isalnum())
    #print (s.isalpha())
    #print (s.isdigit())
    #print (s.islower())
    #print (s.isupper())
    a, b, c, d, e=checking(s)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)



#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



#Designer Door Mat
def printCenter(l,n):
    for i in range(n):
        l.append(".|.")
    return

def printSide(l,n):
    for i in range(n):
        l.append("-")
    return

    
N,M= map(int,input().split(" "))

l1=[]
l2=[]
l3=[]
k=0
for i in range(N):
    if i<(N//2):
        n=2*(i+1)-1
        l1.append(n)
        printSide(l2,(M-(3*n))//2)
        printCenter(l2,n)
        printSide(l2,(M-(3*n))//2)
    
    if i==N//2:
        printSide(l3,(M-7)//2)
        l3.append("WELCOME")
        printSide(l3,(M-7)//2)
        l1.reverse()
    """else:
        #print(l1[k])
        printSide(l2,(M-(3*n))//2)
        printCenter(l2,n)
        printSide(l2,(M-(3*n))//2)
        k+=1
"""
l4=l2
l2=("".join(l2))
l3=("".join(l3))

for i in range(0,len(l2),M):
        print(l2[i:i+M])
for i in range(0,len(l3),M):
        print(l3[i:i+M])
        
l4.reverse()
l4=("".join(l4))
for i in range(0,len(l4),M):
        print(l4[i:i+M])



#Lists
def commands(l,actions):
#insert+2,print,remove+1,append+1, sort, pop, reverse
    
    
    if actions[0]=="insert":    l.insert(int(actions[1]),int(actions[2]))
    if actions[0]=="print":     print(l)
    if actions[0]=="remove":    l.remove(int(actions[1]))
    if actions[0]=="append":    l.append(int(actions[1]))
    if actions[0]=="sort":      l.sort()
    if actions[0]=="pop":       l.pop()
    if actions[0]=="reverse":   l.reverse()
      
    return

if __name__ == '__main__':
     
    N = int(input())
    l=[]
    for i in range(N):
        actions=((input().split(" "))) #risolvere come vengono presi valori in input
        commands(l,actions)
    #print(actions)
    


#Text Wrap
import textwrap

def wrap(string, max_width):
    l=[]
    for i in range(0,len(string),max_width):
        l.append(string[i:i+max_width])
    return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
    
#Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if s[0].isupper()==False:
        s=s[0].upper()+s[1:]
    for i in range(len(list(s))):
        if s[i]==" " and s[i+1].islower()==True:
            s=s[:i]+s[i]+s[i+1].upper()+s[i+2:]
            print(s)
            
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
    

#sWAP cASE
def swap_case(s):
    s=list(s)
    for i in range(len(s)):
        if s[i].isupper()==True:
            s[i]=s[i].lower()
        else:
            s[i]=s[i].upper()
    s="".join(s)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    

#Introduction to Sets
def average(array):
    # your code goes here

    return sum(set(arr))/len(set(arr))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
    
#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
nm=input().split()
arr=input().split()
A=set(input().split())
B=set(input().split())
happiness=0
for i in range(len(arr)):
    if arr[i] in A: happiness+=1
    if arr[i] in B: happiness-=1
print(happiness)



#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
M=input()
a=set(input().split())
N=input()
b=set(input().split())
output= a.difference(b)
output=output.union(b.difference(a))
output=list(output)
integers = [int(value) for value in output]
integers=sorted(integers)
for i in range(len(integers)): print(integers[i])



#Set .add() 
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
countries=[]
for i in range(N):
    countries.append(input())
print(len(set(countries)))



#Set .discard(), .remove() & .pop()
def execute(n,s,commands):
    for i in range(N):       
        if commands[i][0]=="remove":   
            s.remove(int(commands[i][1]))
            #print("removed")
        if commands[i][0]=="discard":  
            s.discard(int(commands[i][1]))
            #print("discarded")
        if commands[i][0]=="pop":      
            s.pop()
            #print("popped")
    return

n = int(input())
s = set(map(int, input().split()))
N=int(input())
commands=[]
for i in range(N):
    commands.append(input().split())
    
execute(N,s,commands)
print(sum(s))



#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng=int(input())
e_studs=set(input().split(" "))
french=int(input())
f_studs=set(input().split(" "))
union=f_studs.union(e_studs)
print(len(union))





#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng=int(input())
e_studs=set(input().split(" "))
french=int(input())
f_studs=set(input().split(" "))
intersect=f_studs.intersection(e_studs)
print(len(intersect))



#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng=int(input())
e_studs=set(input().split(" "))
french=int(input())
f_studs=set(input().split(" "))

intersect=f_studs.intersection(e_studs)

print(len(e_studs.difference(intersect)))



#Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng=int(input())
e_studs=set(input().split(" "))
french=int(input())
f_studs=set(input().split(" "))
req=f_studs.symmetric_difference(e_studs)
print(len(req))



#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
def execute(n,s,commands):

    for i in range(1,2*n):       
        if commands[i-1][0]=="intersection_update": 
            s.intersection_update(set(commands[i][:]))
            #print("int update:",s)
                
        if commands[i-1][0]=="symmetric_difference_update":  
            s.symmetric_difference_update(set(commands[i][:]))
            #print("symm diff update:",s)
        
        if commands[i-1][0]=="difference_update":   
            s.difference_update(set(commands[i][:]))
            #print("diff update",s)        
                
        if commands[i-1][0]=="update":   
            s.update(set(commands[i][:]))
            #print("update",s)
              
    return

l_A=int(input())
A=set(input().split())
N=int(input())
commands=[]
for i in range(2*N):
    commands.append(input().split())
execute(N,A,commands)
#print(commands)
A1=list(A)
integers = [int(value) for value in A1]
print(sum(integers))




#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
def isInside(A,B):
    print(A.issubset(B))
    return
    
T=int(input())
l_A,l_B=[],[]
for i in range(T):
    l_A.append(int(input()))
    A=set(input().split())
    l_B.append(int(input()))
    B=set(input().split())
    isInside(A,B)



#Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(input().split())
n=int(input())
results=[]
for i in range(n):
    B=set(input().split())
    results.append(A.issuperset(B))
conta=0
for i in range(n):
    if results[i]==True:
        conta+=1
if conta==n:
    print(True)
else:
    print(False)



#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter as c
X=int(input()) #numbers of shoes
size=(input().split()) #size available
#dic=dict(size)
N=int(input())

l=[]
gain=0
for i in range(N):
    l.append(input().split())
    if l[i][0] in size[:]:
        gain+=int(l[i][1])
        size.remove(l[i][0])
print(gain)



#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = input().split()
N = int(n)
M = int(m)
A = defaultdict(list)
B = []
for i in range(N):
    A[input()].append(i+1) 
for i in range(M):
    B.append(input())
    

for word in B:
    if word in A:
        print(" ".join(map(str,A[word]) ))
    else:
        print("-1")



#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N=int(input())
cols=(input().split())
info=namedtuple("info", cols[:])
index=0
for i in range(len(cols)):
    if cols[i]=="MARKS":
        index=i
        
somma=0
for i in range(N):
    info0,info1,info2,info3=input().split()
    l=info(info0,info1,info2,info3)
    somma+=int(l.MARKS)
    #print(somma)
print("{:.2f}".format(somma/N))



#Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N=int(input())
food = OrderedDict()
for i in range(N):
    item, space, price= input().rpartition(" ")
    food[item]=food.get(item,0)+int(price)
    #print(food.get(item))
for item,price in food.items():
    print(item,price)




#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
words=OrderedDict()
for i in range(n):
    word=input()
    words[word]=words.get(word,0)+1

count=0
for word in words:
    count+=1
print(count)
a=[]
for word in words:
    a.append(str(words[word]))
print(" ".join(a))



#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def execute(methods):
    d=deque()
    for i in range(len(methods)):
        if methods[i][0]=="append":
            d.append(methods[i][1])
            #print(d)
        if methods[i][0]=="appendleft":
            d.appendleft(methods[i][1])
            #print(d)
        if methods[i][0]=="pop":
            d.pop()
            #print(d)
        if methods[i][0]=="popleft":
            d.popleft()
            #print(d)
    return   d


N=int(input())
methods=[]
d=deque()
for i in range(N):
    methods.append(input().split()) 
#print(methods)
d=execute(methods)
print(" ".join(d))




#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month, day, year = (input().split())
month,day,year=int(month),int(day),int(year)
s=(calendar.day_name[calendar.weekday(year,month,day)])
print(s.upper())



#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(T):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as v:
        s=a.isnumeric()
        if s==True:
            print("Error Code: invalid literal for int() with base 10:","'{}'".format(b))
        else:
            print("Error Code: invalid literal for int() with base 10:","'{}'".format(a))
            




#Zipped!	
# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X=map(int,input().split())
grades=[]
for i in range(X):
    grades.append(map(float,(input().split())))

for i in zip(*grades):
    print("{:.1f}".format(sum(i)/X))



#Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())
    
    arr=sorted(arr, key=lambda x: x[k])
    for i in range(len(arr)):
        print(*arr[i][:])


#ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
#lower>upper>odd>even
s=input()
l,u,o,e= [],[],[],[]
for i in s:
    if i.islower() == True:
        l+=i
    elif i.isupper() == True:
        u+=i
    elif int(i)%2!= 0:
        o+=i
    else:
        e+=i
l.sort()
u.sort()
o.sort()
e.sort()
print("".join(l)+"".join(u)+"".join(o)+"".join(e))



#Map and Lambda Function
cube = lambda x:pow(x,3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    lis=[0,1]
    for i in range(n-2):
        lis.append(lis[-2] + lis[-1])
    return(lis[:n])
    
  

    
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    
    
    
#Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
def check(N):
    a=[]
    ok=['+','-','.','0','1','2','3','4','5','6','7','8','9']
    numbers=['1','2','3','4','5','6','7','8','9']
    if N[0] not in ok:
       a.append(False)
    else:
        a.append(True)
    count=0
    index=0
    for i in range(len(N)):
        if N[i]==".":
            count+=1
            index=i
    if count==1:
        a.append(True)
    else:
        a.append(False)
        
    for i in range(1,len(N)):
        if i!=index:
            if N[i].isnumeric()==False:
                a.append(False)
        
    if False in a:
        print(False)
    else:
        print(True)
    return
    


T=int(input())
for i in range(T):
    N=input()
    check(N)




#Re.split()
regex_pattern = r",|\."	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


#Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
numbers=["0","1","2","3","4","5","6","7","8","9"]
l=[]
for i in range(1,len(s)):
    if s[i]==s[i-1] and (s[i].isalpha()==True or s[i] in numbers):
        l.append(s[i])

if len(l)>0:
    print(l[0])
else:
    print("-1")



#Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr=numpy.array(arr,dtype=numpy.float64)
    return (numpy.flip(arr))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)



#Shape and Reshape
import numpy as np

numbers=np.array(input().split(),dtype=np.int64)
print(np.reshape(numbers,(3,3)))




#Transpose and Flatten
import numpy as np

N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(input().split())
arr=np.array(arr,dtype=int)
print ("".join(str(np.transpose(arr))))
print ("".join(str(arr.flatten())))



#Concatenate
import numpy as np
N,M,P=map(int,input().split())
arr1,arr2=[],[]
for i in range(N):
    arr1.append(input().split())
for i in range(M):
    arr2.append(input().split())
arr1=np.array(arr1,dtype=int)
arr2=np.array(arr2,dtype=int)
print(np.concatenate((arr1,arr2),axis=0))




#Zeros and Ones
import numpy as np

size=tuple(map(int,input().split()))

print(np.zeros((size),int))
print(np.ones((size),int))



#Eye and Identity
import numpy as np

np.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
print(np.eye(n,m, k = 0))




#Array Mathematics	
import numpy as np
N,M=map(int,input().split())
A=np.array([input().split() for i in range(N)],int)
B=np.array([input().split() for i in range(N)],int)
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)



#Floor, Ceil and Rint
import numpy as np
np.set_printoptions(legacy='1.13')
arr=np.array(input().split(),float)
print (np.floor(arr))
print (np.ceil(arr))
print (np.rint(arr))



#Sum and Prod
import numpy as np
N,M=map(int,input().split())
arr=np.array([input().split() for i in range(N)],int)

arr1=np.sum(arr, axis = 0) 
arr2=np.prod(arr1)

print(arr2)



#Min and Max
import numpy as np

N,M=map(int,input().split())
arr=np.array([input().split() for i in range(N)],int)
print(np.max(np.min(arr,axis=1)))



#Mean, Var, and Std
import numpy as np
n,m=map(int,input().split())
arr=np.array([input().split() for i in range(n)],int)
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(round(np.std(arr),11))




#Dot and Cross
import numpy as np
n=int(input())
A=np.array([input().split() for i in range(n)],int)
B=np.array([input().split() for i in range(n)],int)
print(np.dot(A,B))



#Inner and Outer
import numpy as np
A=np.array(input().split(),int)
B=np.array(input().split(),int)
print(np.inner(A,B))
print(np.outer(A,B))



#Polynomials
import numpy as np
P=np.array(input().split(),float)
x=int(input())
print(np.polyval(P,x))



#Linear Algebra
import numpy as np
N=int(input())
matrix=np.array([input().split() for i in range(N)],float)
print(round(np.linalg.det(matrix),2))




#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy as np

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    c=sorted(candles)
    return c.count(c[-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()



#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)



#Print Function
if __name__ == '__main__':
    n = int(input())
    [print(n-(n-i),end="") for i in range (1,n+1)]



#Tuples 
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))



#Number Line Jumps
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    #number of jumps n  x1+nv1=x2+nv2==> n=(x1-x2)/(v2-v1)
    x1,x2,v1,v2=float(x1),float(x2),float(v1),float(v2)
    if v2-v1!=0:
        n=(x1-x2)/(v2-v1)
    else:
        return("NO")
    if n>0 and n.is_integer():
        #print(n)
        return("YES")
    else:
        return("NO")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()




#Viral Advertising
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    likes=2
    shared=5
    cumulative=2
    for i in range(1,n):
        shared=likes*3
        likes=int(shared/2)
        cumulative+=likes
        
    return cumulative
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()



#Recursive Digit Sum
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    if len(n)>1:
        value=0
        for i in n:
            value+=int(i)
        return superDigit(str(value*k),1)
    else:
        return int(n)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



#Insertion Sort - 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    value=arr[n-1]
    arr[n-1]=arr[n-2]
    for i in range(1,n):
        
        if arr[n-i]>=arr[n-i-1] and value<= arr[n-i-1]:
            arr[n-i]=arr[n-i-1]
            print(*arr)
        else:
            arr[n-i]=value
            print(*arr)
            break
    
    if arr[0]==arr[1]:
        arr[0]=value
        print(*arr)
    return

if __name__ == '__main__':    
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)





#Insertion Sort -2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1,n):
        for j in range(n):
            if arr[i]<arr[j] and j<i:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
        print(*arr)     
    return


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

#Validating Roman Numerals
#discussions helped me a bit
migliaia = 'M{0,3}'
centinaia = '(CM|CD|D?C{0,3})'
decine = '(XC|XL|L?X{0,3})'
cifre = '(IX|IV|V?I{0,3})'

regex_pattern = r"%s%s%s%s$"%(migliaia, centinaia, decine, cifre)	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S,k=input(),input()
   #match---->(start index,end index)
#no match---->(-1,-1)
count=0
for i,value in enumerate(S):
    if re.match(k,S[i:]):
        print((i,i+len(k)-1))
        count+=1
if count==0:
    print((-1,-1))



#Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT

def check_punto(email):
    index=-1
    for i in range(len(email)):
        if email[i]==".":
            index=i
    return index

def check_chiocciola(email):
    index=-1
    count=0
    for i in range(len(email)):
        if email[i]=="@":
            index=i
            count+=1
    return index,count

def check(email):
    if "@" not in email:
        return False
    valid=["-","_",".","@"]
    TF=True
    j=-1
    z=-1
    if email[0].isalpha()==False:
        return False
    j=check_punto(email)
    if j!=-1:
        #print(email[j:])
        if len(email[j:])>4:
            #print("+++")
            return False     
    z,count=check_chiocciola(email)
    if len(email[z:])<2:
        return False
    if count>1:
        return False
    if z!=-1:
        for i in range(z+1,len(email)):
            if i!=j: 
                if email[i].isalpha()==False:
                    #print(email[i])
                    return False       
    for i in range(len(email)):
        #print(email[i])
        if email[i].isalnum()==False:
            #print("+++")
            if email[i] not in valid:
                #print("+++")
                TF=False
                #print(type(email[i]),email[i],TF)
            
    return TF


n=int(input())
for j in range(n):
    name,email=input().split()
    email1=email[1:len(email)-1] #this line removes "<,>"
    TF=check(email1)
    #print(TF)
    if TF==True:
        print(name,email)



#Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
def check_reps(cc):
    reps=-1
    for i in range(3,len(cc)):
        if cc[i-3]==cc[i-2]==cc[i-1]==cc[i]:
            reps=1
            return reps
    return reps

def check_spacing(cc):
    for i in range(4,len(cc),5):
        if cc[i]!="-" or cc[i]==cc[i-1]:
            return -1
    return(0)

def check_cc(cc1):
    ok_starter=["4","5","6"]
    l=list(cc1)
    cc=list(filter(lambda a: a != "-", l))
    cc=("".join(cc))
    #print(cc,len(cc))
    reps=check_reps(cc)
    if (cc.isnumeric()) and (len(cc1)==16 or len(cc1)==19) and (cc[0] in ok_starter) and (reps==-1):
        if len(cc1)==19:
            
            k=check_spacing(cc1)
            if k==-1:
                #print("+++")
                return print("Invalid")
            else:
                #print(cc1)
                #print("***")
                return print("Valid")
        else:
            print("Valid")
    else:
        #print("---")
        return print("Invalid")
        
    
    
    
N=int(input())
cc=""
for i in range(N):
    cc=input()
    #print(cc)
    check_cc(cc)


#The Captain's Room -> WORKS BUT TAKES TOO LONG TO RUN
# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input()) #numero di membri per gruppo
rooms=input().split()
Rooms = set(rooms)

l=[0]*len(Rooms)
temp=list(Rooms)
#print(temp)
for i in range(len(Rooms)):
    for j in range(len(rooms)):
        if temp[i]==rooms[j]:
            l[i]+=1

for i in range(len(l)):
    if l[i]==1: print(temp[i])
           
           
           
            
#RE.FINDALL()
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
s = '[b-df-hj-np-tv-z]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a) or "-1")




#REGEX.SUBSTITUTION()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
text=[]
for i in range(n):
    text.append(str(input()))

for i in range(n):
    text[i]=re.sub(r'(?<= )(&&)(?= )',"and",text[i])
    print(re.sub(r'(?<= )(\|\|)(?= )',"or",text[i]))










#VALIDATING PHONE NUMBERS
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for i in range(N):
    number=str(input())
    if re.match(r'^[7-9]', number) and len(number)==10 and number.isdigit():
        print("YES")
    else: print("NO")





#HEXCOLOR CODE
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
inside_css_flag=0

for i in range(N):
    text=str(input())
    #if text=="{":inside_css_flag=1
    #elif text=="}":inside_css_flag=0

    #if inside_css_flag==1:
    pattern=r"(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)"
    for word in re.findall(pattern,text,re.IGNORECASE):
        if len(word)==4 or len(word)==7:
            print(word)
