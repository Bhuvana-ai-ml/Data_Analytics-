# list1=["hi","hello","bye","thank"]
# list2=[12,14,56,8,9]
# list1.sort()
# print(list1)
# list2.sort(reverse=True)
# print(list2)
# list2.append(4)
# print(list2)
# list1=["hi","hello","bye","thank"]
# list3=["good","bad"]
# list1.extend(list3)
# print(list1)
# print(list3)
# def sum(a,b):
#     print(a+b)
#     return (a+b)
# sum(2,3)
# list2=[12,14,56,8,9]
# print(max(list2))
# print(min(list2))
# list2=[12,14,56,8,9]
# list2.pop()
# print(list2)
# list2.remove(12)
# print(list2)
# list2.insert(2,15)
# print(list2)
# num=[1,2,4,3,5,6]
# num[1:3]=[20,30]
# print(num)
# num[3]=5
# print(num)
# ls1=[1,2,3]
# ls2=[5,6,8]
# ls3=ls1+ls2
# print(ls3)
# print(ls3*3)
# ls1=[1,2,3,55,6,89,47,22,8]
# ls2=[x for x in ls1 if(x%2!=0)]
# print(ls2)
ls1=[1,2,3,55,6,89,47,22,8]
# sqr=["sqaure:"+str(x**2) for x in ls1 ]
# print(sqr)
# print("sqaure:(x**2)" for x in sqr)
def even(a):
    if(a%2==0):
        return("even")
    else:
        return("odd")
even=list(map(even,ls1))
print(even)
even= lambda x : x%2==0
print(even(5))
