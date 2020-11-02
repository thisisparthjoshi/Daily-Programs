a = 100
b = 500
c = 2000
n=eval(input("Enter withdrawl amount"))
if 2000 <= n <= 25000 :
    print("Processing Transaction Please wait")
    print("you will recieve money in form of notes of rs", (c))
    print("Your transaction has been sucessfully completed ")
if 500 <= n < 2000 :
    print("Processing Transaction Please wait")
    print("you will recieve money in form of notes of rs", (a) or (b))
    print("Your transaction has been sucessfully completed ")
if 100 <= n < 500 :
    print("Processing Transaction Please wait")
    print('you will recieve money in form of notes of rs', (a))
    print("Your transaction has been sucessfully completed ")
if n <= 100 :
    print("Processing Transaction Please wait")
    print("Invalid Amount Entered")
if n > 25000 :
     print("Not allowed to withdraw above the limit")
     
