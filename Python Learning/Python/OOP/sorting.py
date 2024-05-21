rollNumber = [2,5,3,4,1,9]
rollNumber.sort()
print(rollNumber)
rollNumber.sort(reverse=True)
print(rollNumber)

#Tuple doens't have index so we need to use sort Func
rollNumber = (2,5,3,4,1,9)
sortedNum = sorted(rollNumber)
rollNumber = (2,5,3,4,1,9)
sortedNum = sorted(rollNumber, reverse=True)


#Sorting values of diff type
data = [("Jaya ram", 3), ("Pavan Kumar", 1), ("Gopi", 2)]
grade = lambda grade: grade[1]
data.sort(key=grade)
print(data)
