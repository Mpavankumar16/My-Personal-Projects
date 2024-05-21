#Map applies fucntion to all iterable

storeItems = [("Milk", 40),("Chicken", 200), ("Mutton",250), ("Eggs", 80)]

usdConverteer = lambda items: (items[0]+" Price in $", items[1]/80)

print(list(map(usdConverteer, storeItems)))

#Filter func to filter items
#only get prices greater than 200
highPrice = lambda items: items[1]>=200
print(list(filter(highPrice, storeItems)))


#Reduce
import functools
letters = ["H","E","L","L","O"]
print(functools.reduce(lambda x,y: x+y, letters))

#List Comprehensions
#[Expression ForITem Condition]
#[Expression IfElse ForITem]
squares = [i*i for i in range(1,11)]
studScores = [100,90,76,85,60,54,40]
print(list(filter(lambda i: i>=90, studScores)))
print([i for i in studScores if i>=90])
print([i if i>=90 else "False" for i in studScores])


#Dictionary comprehensions
USprices = {"Milk":40, "Chicken":300, "Mutton": 1000}
print({key: value*80 for key, value in USprices.items()})
print({key: value*80 for key, value in USprices.items() if value>=1000})
print({("Lamb" if key=="Mutton" else key): value for key, value in USprices.items()})


#Zip
users = ["Pavan Kumar", "Gopi", "Jaya Ram"]
passwords = ["Pavan@1", "Gopi11", "Java14"]

loginInfo = zip(users, passwords)
for i in loginInfo:
    print(i)

loginInfo = dict(zip(users, passwords))
for key, value in loginInfo.items():
    print(key+" : "+value)