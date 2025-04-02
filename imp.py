#list comperhension
# import numpy as np
# print(np.arange(10))
# print(np.linspace(0,10,3))
# data = [10, 20, 30, 40]
# median = np.median(data)
# print(median)  
# data = [10, 20, 30, 40]
# print(np.mean(data))
# data = [10, 20, 30, 40]
# print(stats.mode(data))
# import numpy as np
# x=np.array([1,2,3,4])
# print(x)
# print("test if none of the element of the  said array is zero")
# print(np.all(x))
# import numpy as np
# x=np.array([1,2,3,4])
# print(x)
# print("test if none of the element of the  said array is zero")
# print(np.all(x>1))
# import numpy as np
# x=np.array([1,2,3,4])
# print(x)
# print("test if none of the element of the  said array is zero")
# print(np.all(x>=1))
# import numpy as np
# x=np.array([1,2,3,4])
# print(x)
# print("test if none of the element of the  said array is zero")
# print(np.all(x%2==0))
import numpy as np
x=np.array([1,2,3,4])
print(x)
print("test if none of the element of the  said array is zero")
print(np.all(x<=4))
import numpy as np
x=np.array(["hi","hello","bye","thank"])
print(x)
print("test if none of the element of the  said array is zero")
print(np.all(x=="hi"))x=np.array([1,2,3,4])
print(x)
print("test if all element is less than eqaul to 4")
print(np.all(x<=4))
x=np.array(["hi","hello","bye","thank"])
bool_arr=x>"hi"
print(bool_arr)
arr=np.array([0,2,4,0,8])
bool_arr=arr.astype(bool)
print(bool_arr)
arr= np.array([True ,True ,True])
result=np.all(arr)
print(result)
arr=np.array([1,2,4,5,3,7])
print(np.any(arr<3))
arr=np.array(["hi","hello","good","bye"])
print(np.any(arr=="thank"))
arr= np.array([True ,True ,True])
result=np.any(arr!=True)
print(result)
arr=np.array([2,4,8,9,15,20,30,25])
boo_arr=(arr%2==0)&(arr%3==0)
print(bool_arr)
a=([1,4,5])
b=([7,8,9])
print(np.multiply(a,b))
print(np.add(a,b))
print(np.subtract(a,b))
print(np.divide(a,b))
a=np.array([1+1j,1+0j,4.5,3,2,2j])
print("Original array")
print(a)

print("checking for complex number")
print(np.iscomplex(a))

print("checking for real number")
print(np.isreal(a))
a=np.array([[1,2],[3,4]])
b=np.array([[1,2],[3,4]])
c = a==b
print(c.all())
a=np.array([[[1,2],[3,4],[5,4]]])
b=np.array([[[1,2],[5,4],[3,4]]])
c = a==b
print(c.all())
zero=np.full(10,0)
ones=np.full(10,1)
five=np.full(10,5)
print(zero)
print(ones)
print(five)
print(np.concatenate((zero,ones,five)))




