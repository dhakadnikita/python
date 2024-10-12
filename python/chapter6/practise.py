a = int(input('Enter your no : '))
b = int(input('Enter your no : '))
c = int(input('Enter your no : '))
d = int(input('Enter your no : '))
e = int(input('Enter your no : '))

if(a>b and a>c and a>d and a>e ):
    print("Greatest number is a:", a)
elif(b>a and b>c and b>d and b>e):
    print("greates number is b:",b)

#problem2 
percentage = ((a+b+c+d+e)*100)/500

if(percentage >= 40 and a>=33 and b>=33 and c>=33 and d>=33 and e>=33):
    print("you are passed:", percentage)
else:
    print ("you are failed :",percentage)


