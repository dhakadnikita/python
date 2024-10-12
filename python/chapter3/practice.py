# name = input("Enter your name:")

# print(f"Good Afternoon , {name}")

letter = '''Dear
 <|name|>,
You are selected !
<|Date|>'''

print(letter.replace("<|name|>","Nikita").replace("<|Date|>"," 25 june 2030"))

name = 'Nikita is a good girl  and'

print(name.find('  '))
print(name.replace("  "," "))