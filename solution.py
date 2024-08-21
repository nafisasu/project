# input1=int(input())
# input2=int(input())
# arr=list(map(int,input().split()))
# mx=-1
# for i in range(0,len(arr)-input2+1):
#     tmp=arr[i:i+input2]
#     k,s=1,0
#     for j in tmp:
#         s+=(j*k)
#         k+=1
#     if s>mx:
#         mx=s
# print(mx)
# n=int(input())
# a=list(map(int,input().split()))
# c=0
# for i in range(n):
#     if sum(a[:i+1])==0:
#         c+=1
# print(c)
# n=int(input())
# l=list(map(int,input().split()))
# a=0
# for i in l:
#     a=a+(i//3)
#     if i%3!=0:
#         a+=1
#     else:
#         a+=0
# print(a)
# n=int(input())
# p=int(input())
# x=240-p
# c=0
# for i in range (1,n+1):
#     if x>0 and x>i*5:
#         x=x-(i*5)
#         c+=1
#     else:
#         break
# print(c)
# n=int(input())
# arr=list(map(int,input().split()))
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# b=list(d.values())
# r=b.copy()
# m=max(b)
# b.remove(m)
# key_max=max(d,key=d.get)
# if m in b:
#     print(-1)
# else:
#     print(key_max)
# s=input()
# v='aeiou'
# max=0
# vowel=''
# for i in v:
#     if s.count(i)>max:
#         max=s.count(i)
#         vowel=i
# print(vowel)
# n=int(input())
# arr=list(map(int,input().split()))
# m=int(input())
# arr.sort()
# k,count=0,0
# pro=1
# for k in range(n-2):
#     i,j=k+1,n-1
#     while i<j:
#         pro=arr[i]*arr[j]*arr[k]
#         if pro>m:
#             j-=1
#         elif pro<m:
#             i+=1
#         else:
#             count+=1
#             i+=1
#             j-=1
# print(count)
# n=int(input())
# arr=list(map(int,input().split()))
# arr.sort()
# m1=arr[-1]
# m2=arr[-2]
# avg=(m1+m2)/2
# sum=0
# for i in arr:
#     if i>=avg:
#         sum+=i
# print(sum)

# def is_prime(k):
#     if k<=1:
#         return False
#     for i in range(2,int(k**0.5)+1):
#         if k%i==0:
#             return False
#     return True
# inp=int(input())
# num=inp+1
# while True:
#     if is_prime(num):
#         print(num)
#         break
#     num+=1

    
# inp=input()
# d={}
# mx=-999
# for i in inp:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
#     if d[i]>mx:
#         mx=d[i]
# print(len(inp)-mx)

# inp=input()
# for i in range(len(inp)):
#     print(int(inp[i])**2,end='')

# n=int(input())
# arr=list(map(int,input().split()))
# flag=True
# for i in range(n):
#     arr1,arr2=arr[0:i],arr[i+1:n+1]
#     if sum(arr1)==sum(arr2):
#         flag=False
#         print(i+1)
# if flag:
#     print("not found")

# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# def lcm(a,b):
#     l=(a*b)//gcd(a,b)
#     return l
# a,b=map(int,input().split())
# print(gcd(a,b))
# print(lcm(a,b))

# alpha=set('abcdefghijklmnopqrstuvwxyz')
# inp=input()
# n=set(inp.lower())
# missing=alpha-n
# res=''.join(sorted(missing))
# print(res)

# inp=list(map(str,input().split()))
# print(inp[::-1])

# arr=list(map(int,input().split()))
# target=int(input())
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             print([i,j])

# def peak(arr):
#     n=len(arr)
#     if n==1 or arr[0]>=arr[1]:
#         return 0
#     if arr[n-1]>arr[n-2]:
#         return n-1
#     for i in range(1,n-1):
#         if arr[1]>=arr[i-1] and arr[i]>=arr[i+1]:
#             return i
# n=int(input())
# arr=list(map(int,input().split()))
# print(peak(arr))

# n=int(input())
# num=list(map(int,input().split()))
# max_here=num[0]
# max_far=num[0]
# for i in num[1:]:
#     max_here=max(i,i+max_here)
#     max_far=max(max_here,max_far)
# print(max_far)

# n=list(map(int,input().split()))
# s=0
# m=0
# for i in range(len(n)):
#     s+=n[i]
#     if abs(s)>m:
#         m=abs(s)
# print(m)

# n,k,i=(map(int,input().split()))
# a=i
# while k>i:
#     i+=1
#     k-=1
#     if i>n:
#         i=1
# print(i)

# n=input()
# i=0
# res=0
# while i<len(n):
#     if i<len(n)-1 and n[i]=='0' and n[i+1]=='0':
#         i+=2
#     else:
#         i+=1
#     res+=1
# print(res)

# s=input()
# p=int(input())
# k=int(input())
# start=max(0,p-k-1)
# end=min(len(s),p+k)
# print(min(list(s[start:end])))

# n=input()
# s=input()
# res=0
# for i in n:
#     d=0
#     mn=100
#     for j in s:
#         d=abs(ord(i)-ord(j))
#         if d<mn:
#             mn=d
#     res+=mn
# print(res)

# n=int(input())
# arr=list(map(int,input().split()))
# a,b=0,0
# for num in set(arr):
#     if num%2==0:
#         if arr.count(num)%2==0:
#             a+=1
#         else:
#             b+=1
#     else:
#         if arr.count(num)%2==0:
#             b+=1
#         else:
#             a+=1
# if a>b:
#     print('a',a-b)
# elif a==b:
#     print('t 0')
# else:
#     print('b',b-a)

# n=int(input())
# res=0
# cur=1000
# comma=1
# while cur<=n:


#     next=cur*1000
#     nums=min(n-cur+1,next-cur)
#     res+=nums*1
#     cur=next
#     comma+=1
# print(res)

# def ans(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return ans(n-1)*ans(n-1)+ans(n-2)*ans(n-2)%47
# n=4
# print(ans(n))

# a,b,c=map(int,input().split())
# ans=max(a+b,b+c,a+c)
# print(ans)

# def ans(n,a):
#     max_product=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if (a[i]+a[j]==18 and a[i]>a[j]):
#                 if(a[i]*a[j]>max_product):
#                     max_product=a[i]*a[j]
#                     ans=[a[i],a[j]]
#     return ans
# n=8
# a=[11,12,2,8,10,11,9,8]
# print(ans(n,a))
# n,m=list(map(int,input().split(" ")))
# arr=list(map(int,input().split(" ")))
# product=[]
# for i in range(m):
#     price,weight=list(map(int,input().split(" ")))
#     product.append([price,weight])
# ans=[]
# for person in arr:
#     total=0
#     for prc,we in product:
#         if prc<=person:
#             total+=we
#     ans.append(total)
# print(*ans, sep=" ")