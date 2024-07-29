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
    
    
    
print(220/10)
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