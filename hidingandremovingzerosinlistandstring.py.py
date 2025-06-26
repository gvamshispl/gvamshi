
#hideing the cardnumber of last 4 digits

def card(cardnumber):
    cdnumber=str(cardnumber)
    return '*'*(len(cdnumber)-4)+cdnumber[-4:]
cardnumber=int(input("enter your card number:"))
print(card(cardnumber))


#removing 0 in the list.

list1=[1,2,3,0,4,0,5,0,6,0,7]
for element in list1:
    if element==0:
        list1.remove(element)
        list1.append(element)
print(list1)
