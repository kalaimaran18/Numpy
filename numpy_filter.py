import numpy as np

#numpy using filter()method

n=np.array([4,7,6,2,3,1])
c=[True,False,True,False,True,True]
b=n[c]
print(b)

#numpy using in even numbers only   (2nd Problem)

d=np.array([4,8,7,2,6,0])

#Create empty list
filter_d=[]

for element in d :

#To condition for even value
    if element%2==0:
        filter_d.append(True)
    else:
        filter_d.append(False)
e=d[filter_d]
print(filter_d)
print(e)


#numpy using odd numbers only (3rd problem)

v=np.array([6,5,2,7,9,3,4])

#Create empty list
filter_v=[]
for k in v:

# Give the condition for odd value
    if k%2==1:
        filter_v.append(True)
    else:
        filter_v.append(False)
x=v[filter_v]
print(filter_v)
print(x)