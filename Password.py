passwords = {"Oliver":"Potato79","Anjali":"AbC123","Jeffery":"Jeffery6.5!@"}
x = input("Insert Username:") 
if(x in passwords):

    y = input("Insert Password")
    if (y==passwords[x]):
        print("Successfully Logged In")
    else:
        print("Invalid Password")
else:
        print ("Invalid Username")