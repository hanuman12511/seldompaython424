user = ["user1","user2","user3","user4"]
password = [123,456,789,111]

productname = ["product1","product2","product3"]
productqty = [34,56,23] 
productrate = [100,200,300]
addtocart =[]
n = len(user)
username= input("enter name")
for u in range(n):
    if(user[u] == username):
        password1 = int(input("enter password"))
        if(password1 == password[u]):
            print("user login")
            pname = input("enter product name")
            if pname in productname:
                addtocart.append(pname)
                while(True):
                    qty = int(input("enter qty"))
                    pos = productname.index(pname)
                    if(qty <=productqty[pos]):
                        print("qty=",qty)
                        addtocart.append(qty)
                        addtocart.append(productrate[pos])
                        break
                    else:
                        print("not qty")
                        print("Enter again")
                    
              
            break
        else:
            print("not login")
            break


print(addtocart)

pay = addtocart[1]*addtocart[2]
while(True):
    print("ur payment is ",pay )
    userpay = int(input("enter amount"))
    if(pay<=userpay):
        print("ur amount is ",userpay-pay)
        print("thq")
        break
    else:
        print("enter right amount")


""" user = ["user1","user2","user3","user4"]
password = [123,456,789,111]

productname = ["product1","product2","product3"]
productqty = [34,56,23] 
n = len(user)
username= input("enter name")
for u in range(n):
    if(user[u] == username):
        password1 = int(input("enter password"))
        if(password1 == password[u]):
            print("user login")
            pname = input("enter product name")
            if pname in productname:
                qty = int(input("enter qty"))
                pos = productname.index(pname)
                if(qty <=productqty[pos]):
                    print("qty=",qty)
                else:
                    print("not qty")
                
              
            break
        else:
            print("not login")
            break
 """