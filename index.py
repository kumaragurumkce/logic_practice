# def printOrder(arr,n) :
#     # sorting the array
#     arr.sort()
#     i=0
#     while i<=n/2:
#         print(arr[i])
#         i=i+1
#     j=n-1
#     while j>=n/2:
#         print(arr[j])
#         j=j-1
# # Driver code
# arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
# n = len(arr)
# printOrder(arr, n)

# def rev(A,start,end):
#     if start>=end:
#         return
#     A[start],A[end]=A[end],A[start]
#     rev(A,start+1,end-1)

# A=[10,20,30,40,50]
# rev(A,0,4)
# print(A)
# #calculate the sum of element in an array
# arr1=[10,89,9,56,4,80,8]
# sums=0
# for i in range(0,len(arr1)):
#     sums=sums+arr1[i]
# print(sums)
# #find second smallest number in bytearray
# import math
# arr=[1,2,3,4,5,6,7,8,9]
# first=0
# second=0
# for i in range(0,len(arr)):
#     if arr[i]>first:
#         first=arr[i]

# for i in range(0,len(arr)):
#     if arr[i]!=first and arr[i]>second:
#         second=arr[i]

# print(second)
    
    
# #Occurrence of  igit in a given number
# d=2
# num=12234563222
# count=0
# while num>0:
#     if num%10 == d:
#         count=count+1
#     num=num//10
# print(count)

# # count_digit

# def fun(num):
#     digit=0
#     while num>0:
#         num=num//10
#         digit=digit+1
#     return digit

# num=12345
# print(fun(num))

# num1=12345678000
# digit=0
# while num1>0:
#     num1=num1//10
#     digit=digit+1
# print(digit)



# # strong number
# no=145
# no2=no
# sums=0
# while no>0:
#     no3=no%10
#     fact=1
#     while no3>0:
#         fact=fact*no3
#         no3=no3-1
#     sums=sums+fact
#     no=no//10
    
# if sums==no2:
#     print("strong_number")
    
    
    
# print(220/10)
# find factors of number

# num=100
# i=1
# while i<=num:
#     if num%i==0:
#         print("print--->",i)
#     i=i+1
    

# n=100
# for x in range(1,n+1):
#     if n%x==0:
#         print(x,"for loop")
# # Prime_factors
# num=210
# Prime_factors=[]
# for i in range(1,num+1):
#     if i==1:
#         continue
#     if num%i==0:
#         flag=0
#         for j in range(2,i):
#             if i%j==0:
#                 flag=1
#                 break
#         if flag==0:
#             Prime_factors.append(i)
# print(Prime_factors)

    










# num = 5
# sum = 0
# for i in range(num+1):
#     sum+=i
# print(sum)

# num=5
# sum=0
# for i in range(num+1):
#     sum+=i
# print(sum)

# sum of n number

# num1=230
# num2=30
# if num1>=num2:
#     print(num1,"Greater number")
# else:
#     print("not greater")

# greate number
    
# num1=90
# num2=80
# num3=40
# if num1>=num2 and num1>=num3:
#     print(num1)
# elif num2>=num1 and num2>=num3:
#     print(num2)
# else:
#     print(num3)
# year=2000

# if (year%400==0) or (year%4==0 and year%100!=0):
#     print("leap")
# else:
#     print("Not Leap")
    
# num =15
# flag =0
# for i in range(2,num):
#     if num%i==0:
#         flag=1
#         break
# if flag ==1:
#     print('Not Prime')
# else:
#     print('Prime')
    
# num1=40
# flag=0
# for i in range(2,num1):
#     if num%i==0:
#         flag=1
#         break
# if flag==1:
#     print("Not prime")

# else:
#     print("Prime")
    
# low,high=2,10
# primes=[]
# for i in range(low,high+1):
#     flag=0
#     if i<2:
#         continue
#     if i==2:
#         primes.append(2)
#     for x in range(2,i):
#         if i%x==0:
#             flag=1
#             break
#     if flag==0:
#         primes.append(i)
# print(primes)   
        
# num=str(99)
# sum=0
# for i in num:
#     sum = sum + int(i)
# print(sum)

# num=134
# temp=num
# reverse=0
# while num>0:
#     rem=num%10
#     reverse=(reverse*10) + rem
#     num =num//10
# print(reverse)
# amstrong number3(3)+7(3)+(3)
# 373
num=370
temp=370
digit=0
sum=0
length=len(str(num))
for i in range(length):
    digit=num%10
    num=num/10
    sum=sum + pow(digit,length)
    
if sum==temp:
    print("amstrong")
    
else:
    print("Not Amstong")