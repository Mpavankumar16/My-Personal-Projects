import numpy as np

array = [1,2,3,4,5,6]
nparray = np.array(array)
print(nparray) #These are seperated by spacs not commas
print(type(nparray))
#Can perform all sorts of assignment and slicing and indexsing operations on it
nparray[2] = 10
print(nparray[2])
print(nparray[2:5])

#Multi dimensional numpy arrays
npMulti = np.array([[1,2,3],
                    [4,5,6]])
print(npMulti[0]) #Prints 1st row 
print(npMulti[0, 2]) #Prints 1st row 3rd element
print(npMulti[0][2]) #Prints 1st row 3rd element
print(npMulti.shape) #2rows 3 columns

#[[],[]]
npMulti = np.array([[[1,2,3], 
                    [4,5,6]],
                    [[1,2,3],
                    [4,5,6]]])
print(npMulti.shape) # 2 rows 2Internal rows  3 Columns 
print(npMulti.ndim)
print(npMulti.size)
print(npMulti.dtype)

#If numpy array has a string in it then all individual elements will be made string
npMulti = np.array([[1,2,3],
                    [4,"Hello",6]])
print(type(npMulti[0,0])) #Will return string even though we have int at that place
#If we have something like dict then everthing will be changed to Object 

#Creatin default arrays with fill
fillingArray = np.full((2,3), 3) #2 rows 3 columns array with fill 3
print(fillingArray)
print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.empty((3,3))) #Will just allocates space rather then values

#Filling value in arrays in a range
print(np.arange(0,20,5)) #with 5 steps will make it
print(np.linspace(0,1,5)) #It will create only 5 values with in range 0,1
print(np.isnan(np.nan))
print(np.isinf(np.inf)) #not a value and infinite

ar = [1,2,3,4,5]
npAr = np.array(ar)
print(ar*5) #will print the list 5 times and + operation won't even work
print(npAr*5) #Will multipy 5 with elements of list


#Array Functions
ar = np.array([1,2,3,4,5])
np.append(ar, [7,8,9]) #This will give new array won't change above one
ar = np.append(ar, [7,8,9])
ar = np.insert(ar,  4, [8,8,8])
print(ar)

ar = np.full((4,5), 9)
print(ar)
#reshape will give new array we need to use resize
print(ar.reshape((5,4)))
print(ar.reshape((20)))
print(ar.reshape((2,2,5)))
print(ar.flatten())
print(ar.ravel()) #Will use flatter view if we change it will reflect in original array
val = ar.ravel()
val[4] = 1000
print(ar)
ar.transpose()


#
a1 = np.array([[1,2,3],
                    [4,5,6]])

a2 = np.array([[7,8,9],
               [10,11,12]])

print(np.concatenate((a1,a2), axis=0))
print(np.concatenate((a1,a2), axis=1))
print(np.stack((a1,a2))) #Will add new dimension 

print()
print(str(a1.mean())+" "+str(a1.std())+" "+str(a1.min()))
print()

#Random
a1 = np.random.randint(90, 100, size=(3,3))
print(a1)

# Saving np arrays
np.save("Myarray.npy", a1)
print(np.load("Myarray.npy"))
np.savetxt("Myarray.csv", a1, delimiter=",")


