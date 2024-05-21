#Lists [] Ordered and Duplicates allowed
fruits = ["Apple", "PineApple", "Banana", "Orange"]
fruits[3] = "Sapota" #Re assigning
print(fruits)
fruits.append("Orange")
fruits.insert(1, "Guava")
print("Guava" in fruits)
fruits.reverse()
print(fruits)
print(fruits.sort())
print(fruits)
print(fruits.count("sapota"))
#print(help(fruits))

#Set {} Unordered  NO duplicated
setColl = {"Apple", "PineApple", "Banana", "Orange", "Apple"}
len(setColl)
"Appple" in setColl
setColl.add("O")
print(setColl.pop())
print(setColl)


#Tupple () not adding and Duplciates allowed Fixed size
fruits = ("Apple", "PineApple", "Banana", "Orange")
#print(dir(fruits))
print(fruits.index("PineApple"))

#Dictionaries {}
groceries = {"Milk": 38, "Tomatoes": 25, "Coconut flower": 49}
#print(dir(groceries))
print(groceries.get("Milk"))
print(groceries.get("Bringal")) #None
groceries.update({"Mangoes": 100}) #Adding new dic items
groceries.update({"Tomatoes": 20}) #Updating existing values
groceries.pop("Mangoes")
groceries.popitem() #will remvoe latest added values
print(groceries)
print(groceries.keys()) #Gives list of keys
print(groceries.values()) 
print(groceries.items())
for key, value in groceries.items():
    print(f"{key}: {value}")