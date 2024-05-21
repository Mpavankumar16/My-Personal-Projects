#Won't work
#functionName("Pavan Kumar")

def functionName(name):
    print(name)
functionName("Pavan Kumar")

#Default argu
def functionaName(firstName, lastName="Kumar"):
    print(firstName+" "+lastName)
functionaName("Pavan")
functionaName("Pavan", "Kalyan")

#Keyword arguments should be after normal args
def functionaName(firstName, title, lastName, ):
    print(title+" "+firstName+" "+lastName)
functionaName("Pavan", lastName="Kumar", title="Mr.", )

#Multi args we get tuple in args whcih needs to be unpacked
def functionaName(*args):
    val = 0
    for arg in args:
        val+=arg
    print(val)
functionaName(1,2,3,4,5)

#Kwargs keyword multi args this gives a dict of args with key value
def func(**kwargs):
    for key, val in kwargs.items():
        print(key+" "+val)
func(firstName = "Pavan", lastName="Kumar", surname='Munganda')



#Higher order functions
#Pasing func as an argument

def loud(text):
    print("Loudly saying "+text)
def quit(text):
    print("Quetly saying "+text)
def sayHello(func):
    func("Hello")

sayHello(loud)

#A function that returns another functions
def divisor(x):
    def dividend(y):
        return x/y
    return dividend
divide = divisor(25)
print(divide(5))

#lambda parameters: expression
multipley = lambda x,y:x*y
ageCheck = lambda age:True if age>=18 else False
print(multipley(5,6))
print(ageCheck(20))