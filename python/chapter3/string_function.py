name ='nikita'

print(len(name))
print(name.endswith('ita'))
print(name.startswith('ni'))
print(name.capitalize())


# functions list

# 1 function
s = "hello"
print(len(s))  #Output: 5

# 2 fun
num = 123
s = str(num)
print(s)  # Output: "123"

# 3 fun
s = "HELLO"
print(s.lower())  # Output: "hello"

# 4 fun
s = "hello"
print(s.upper())  # Output: "HELLO"

# 5 fun
s = "hello world"
print(s.split())  # Output: ["hello", "world"]


# 6 fun
words = ["hello", "world"]
s = " ".join(words)
print(s)  # Output: "hello world"


# 7 fun
s = "hello world"
print(s.replace("world", "Python"))  # Output: "hello Python"

#8 fun
s = "hello"
print(s.find("e"))  # Output: 1


# 9 fun 
s = " hello "
print(s.strip())  # Output: "hello"

# 10 fun 
s = "Hello, {}"
print(s.format("world"))  # Output: "Hello, world"



