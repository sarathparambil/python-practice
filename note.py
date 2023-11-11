# a=["apple","orange","banana"]
# for i in a:
#     print(i)

# a=int(input("enter a value"))
# b=[1,2,3,4,5]
# for i in b:
#     print(i,"*",a,"=",i*a)

# a=int(input("enter a number"))
# for i in range(1,11):
#     print(i*a)
#     if i*a==8:
#         break


# for i in range(1,11):
#     print(i)


# a = int(input("Enter a number:"))
# for i in range(1,11):
#     print(i)

# a=2
# b=[1,2,3,4,5]
# for i in b:
#     print(i*a)

# a=int(input("enter a number"))
# for i in range(1,21):
#     print(i*a)

# a=int(input("enter a number"))
# for i in range(1,11):
#     print(i,"*",a,"=",i*a)

#  swap
# a=100
# b=50
# # print(a,b)
# a=a-b#100-50=50
# b=a+b#50+50=100
# print(a,b)

# factorial
# a=int(input("enter a number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)
      

# rows=int(input("enter rows and coloumns"))
# for i in range(rows):
#     for j in range(1+i):
#         print("*",end=" ")
#     print()
    
# rows=int(input("enter number"))
# n=1
# for i in range(rows):
#     for j in range(1+i):
#         print(n,end=" ")
#         n=n+1
#     print()

# a="abcdefg"
# print(a[3])

# a="abcdefg"
# print(a[-2])

# a="abcdefgh"
# print(a[0:4])

# a="abcdefgh"
# print(a[-5:])

# print("hello" + "world")

# print("hello"*4)

# print("hello good moring")

# print("hello \"good\" morning")

# print("hello\nworld")

# print("hello\tworld")

# a="hello world"
# print(a.capitalize())

# a="hello good morning"
# print(a.count("o"))

# a="hello world"
# print(a.startswith("h"))

# a="hello world"
# print(a.endswith("d"))

# a="hello world"
# print(a.find("a"))

# rows=int(input("enter rows and coloumns"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# rows=int(input("enter a number"))
# n=1
# for i in range(rows):
#     for j in range(1+i+1):
#         print(n,end=" ")
#         n=n+1
#     print()

# a="    string    "
# print(a.strip())

# a=int(input("enter number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# rows=int(input("enter rows and coloumns"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# rows=int(input("enter rows and coloumns"))
# n=1
# for i in range(rows):
#     for j in range(1+i):
#         print(n,end=" ")
#         n=n+1
#     print()

# a="apple"
# b=a[::-1]
# print(b)

# sum=0
# a=371
# m=len(str(a))
# c=a
# while c>0:
#     rem=c%10
#     sum=sum+(rem**m)
#     c=c//10
# if a==sum:
#         print("armstrong")
# else:
#         print("not armstrong")

# a=int(input("enter a number"))
# sum=0
# m=len(str(a))
# c=a
# while c>0:
#     rem=c%10
#     sum=sum+(rem**m)
#     c=c//10
# if a==sum:
#     print("armstrong")
# else:
#     print("not armstrong")

# a="abc"
# rev=" "
# count=len(a)
# while count>0:
#     rev=rev+a[count-1]
#     count=count-1
# print(rev)

# factorial
# a=int(input("enter a number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)


# rows=int(input("enter rows and colounm"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# rows=int(input("enter rows and coloumns"))
# n=1
# for i in range(rows):
#     for j in range(i+1):
#         print(n,end=" ")
#         n=n+1
#     print()

# a=[10,12,32,43,45]
# a[3]=[41,34,55]
# print(a)

#factorial

# a=int(input("enter a number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# rows=int(input("enter rows and coloumns"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# rows=int(input("enter rows and coloumns"))
# n=1
# for i in range(rows):
#     for j in range(i+1):
#         print(n,end=" ")
#         n=n+1
#     print()

# a="xyz"
# rev=" "
# for i in a:
#     rev=i+rev
# print(rev)


a=371
sum=0
l=len(str(a))
b=a
while b>0:
    rem=a%10
    sum=sum+(rem**l)
    b=b//10
if b==sum:
    print("it is armstrong")
else:
    print("not armstrong")