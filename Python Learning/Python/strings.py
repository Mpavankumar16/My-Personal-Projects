name = input("Enter your name: ")
print(len(name))
print(name.find("P")) #index 
print(name.rfind("a")) #Reverse index or last occurence
print(name.find("z"))
print(name.capitalize()+ " "+name.upper() + " " + name.lower())
print(f"{name.isdigit()} {name.isalnum()} {name.isalpha()}") 
print(name.count("a"))
print(name.replace('a', '-')) #Will give new string
help(str)

print(name[0:3:2]) #start inclusive and end exclusive

