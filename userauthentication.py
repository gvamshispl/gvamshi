tuple1=("vamshi","abhi","teja")
tuple2=("123456","789456","321789")
name=input("enter user name:")
password=input("enter your passward:")
if name not in tuple1:
    print("user not found!")
else:
    index=tuple1.index(name)
    pswd=tuple2[index]
    if(password==pswd):
        print("user found")
    else:
        print("user not found")
