p1 = 'Make a lot of money'
p2 = 'buy new one'
p3 = 'subscriber'
p4 = 'click this'

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("this comment is not spam")