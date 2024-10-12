marks ={
    "Nikita":100,
    "Rahul": 50,
    "Ranik": 54
}
print(marks, type(marks))

# mutable -- changeable

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Nikita": 99})
print(marks)

print(marks.get("Nikita")) #print none
print(marks['Nikita'])  #error