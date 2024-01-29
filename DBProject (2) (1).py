#önce order oluştur sonra ekle malzemeleri malmezeleri ordan çekersin cart için en son submit tuşuna bastığında dateyi güncelle 
#
#
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime


cnx = mysql.connector.connect(user='root', password='yourpassword',
                              host='localhost',
                              database='dbproject')


pencere = tk.Tk()
pencere.geometry("600x500")
pencere.title("YemekSepeti")




def giris():
    startFrame.tkraise()

def register():
    cursor = cnx.cursor(buffered=True)
    if(register_entry_name.get() =="" or register_entry_surname.get()=="" or register_entry_address.get() =="" or register_entry_email.get()=="" or register_entry_password.get()==""):
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="bütün bilgileri doldurun."
        )
    else:
        selectID = ("SELECT ID "
            "FROM customer "
            "ORDER BY ID desc")

        cursor.execute(selectID)
        result = cursor.fetchone()

        if(result == None):
            customerID =1
        else:
            customerID = result[0] +1


        print(customerID)
        name = register_entry_name.get()
        surname= register_entry_surname.get()
        address= register_entry_address.get()
        email= register_entry_email.get()
        password= register_entry_password.get()

        

        insertCustomer=("INSERT INTO customer "
                        "VALUES (%s, %s,%s,%s,%s,%s)")
        
        values = (customerID,name,surname,address,email,password)
        cursor.execute(insertCustomer,values)
        cnx.commit()
        cursor.close()
        startFrame.tkraise()
    
def customerLogin():
    cursor = cnx.cursor(buffered=True)
    selectPass=("SELECT password , ID FROM customer WHERE email = %s")
    deneme = (login_entry_username.get(),)
    cursor.execute(selectPass,deneme)
    password = cursor.fetchall()

    print(password)
    global customerID
    customerID = password[0][1]

    if(password == None or login_entry_password.get() != password[0][0]):
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="yalnış şifre veya email"
        )
    else:
        print("sucsessful")
        cursor.close()
        customermenuFrame.tkraise()
        #customer page

def restaurantLogin():
    cursor = cnx.cursor(buffered=True)
    controlID = ("SELECT resID "
                "FROM manager "
                "Where email = %s")
    temp1 = (login_entry_username.get(),)
    cursor.execute(controlID,temp1)    
    controlpassword = cursor.fetchone()


    selectPass=("SELECT password FROM customer WHERE email = %s")
    deneme = (login_entry_username.get(),)
    cursor.execute(selectPass,deneme)
    password = cursor.fetchone()
    print(controlpassword)
    print(password)

    if(password == None or login_entry_password.get() != password[0] or controlpassword == None):
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="bilgiler yanlış"
        )
    else:
        print("sucsessful")
        cursor.close()
        menuCreateFrame.tkraise()
        global resID
        resID = controlpassword[0]
        print(resID)
        print(controlpassword)
        print(controlpassword[0])
        #restaurant page

def adminLogin():
    adminName="admin"
    adminPass = "1234"
    if(adminName == login_entry_username.get() and adminPass == login_entry_password.get()):
        print("sucsess")
        adminFrame.tkraise()
    else:
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="yalnış şifre veya email"
        )

def addRestaurant():
    cursor = cnx.cursor(buffered=True)

    controlID = ("SELECT ID "
                "FROM restaurant "
                "Where RestaurantAdress = %s and RestaurantName = %s")
    temp1 = (restaurant_address_entry.get(),restaurant_name_entry.get(),)
    cursor.execute(controlID,temp1)    
    password = cursor.fetchone()


    if((restaurant_name_entry.get() == "" and restaurant_address_entry.get()=="") or password !=None ):
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="Bütün bilgileri doldurun. Ya da bu işletme zaten bulunuyor"
        )
    else:
        selectID = ("SELECT ID "
                "FROM restaurant "
                "ORDER BY ID desc")

        cursor.execute(selectID)
        result = cursor.fetchone()

        if(result == None):
            restaurantID =1
        else:
            restaurantID = result[0] +1
        insertCustomer=("INSERT INTO restaurant "
                            "VALUES (%s, %s, %s)")
            
        values = (restaurantID,restaurant_name_entry.get(),restaurant_address_entry.get())
        cursor.execute(insertCustomer,values)
        cnx.commit()
        cursor.close()
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="restorant eklendi"
        )

def deleteRestaurant():
    cursor = cnx.cursor(buffered=True)
    controlID = ("SELECT ID "
                "FROM restaurant "
                "Where RestaurantAdress = %s and RestaurantName = %s")
    temp1 = (restaurant_address_entry.get(),restaurant_name_entry.get(),)
    cursor.execute(controlID,temp1)    
    password = cursor.fetchone()


    if((restaurant_name_entry.get() == "" and restaurant_address_entry.get()=="") or password ==None ):
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="bütün bilgileri doğru girin. Ya da böyle bir işletme bulunmuyor"
        )
    else:
        delete = ("DELETE FROM restaurant Where RestaurantAdress = %s and RestaurantName = %s")
        name = (restaurant_address_entry.get(),restaurant_name_entry.get(),)
        cursor.execute(delete,name)
        cnx.commit()
        cursor.close()
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="restorant silindi"
        )

def addItem():
    cursor = cnx.cursor(buffered=True)

    selectID = ("SELECT ID "
            "FROM item "
            "ORDER BY ID desc")

    cursor.execute(selectID)
    result = cursor.fetchone()

    if(result == None):
        customerID =1
    else:
        customerID = result[0] +1

    controlID = ("SELECT ID "
                "FROM item "
                "Where foodname = %s and resID = %s")
    temp1 = (item_name_entry.get(),resID,)
    cursor.execute(controlID,temp1)    
    password = cursor.fetchone()


    if((item_price_entry.get() == "" and item_name_entry.get()=="") or password !=None ):
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="Bütün bilgileri doldurun. Ya da bu Item zaten bulunuyor"
        )
    else:
        insertCustomer=("INSERT INTO item "
                        "VALUES (%s, %s,%s,%s)")
        
        values = (customerID,resID,item_name_entry.get(),item_price_entry.get())
        cursor.execute(insertCustomer,values)
        cnx.commit()
        cursor.close()
        print(resID)
        menuCreateFrame.tkraise()

def currentItems():
    cursor = cnx.cursor(buffered=True)
    res =resID
    print("resıd"+str(res))
    resValue = (res,)
    sta = ("SELECT foodName from item inner join restaurant on item.resID = restaurant.ID where restaurant.ID = %s")

    cursor.execute(sta,resValue)
    global names
    names = cursor.fetchall()

    sta = ("SELECT foodPrice from item inner join restaurant on item.resID = restaurant.ID where restaurant.ID = %s")

    cursor.execute(sta,resValue)
    global prices
    prices = cursor.fetchall()

    sta = ("SELECT COUNT(foodName) from item inner join restaurant on item.resID = restaurant.ID where restaurant.ID = %s")
    cursor.execute(sta,resValue)
    global countitem
    countitem = cursor.fetchone()
    cursor.close()
    wroteitems()
    root.tkraise()


def deleteItem():
    cursor=cnx.cursor(buffered=True)
    sql = ("DELETE FROM item Where resID =%s and foodName =%s")
    ans =(resID,liste.get(liste_indeks[0]),)
    print(liste.get(liste_indeks[0]))
    cursor.execute(sql,ans)
    cnx.commit()
    cursor.close()
    liste.delete(0,tk.END)
    menuCreateFrame.tkraise()

def updateItem():
    cursor = cnx.cursor(buffered=True)
    updatequery=("UPDATE item SET foodName = %s , foodPrice = %s WHERE foodName =%s")
    updatevalue = (foodname_entry.get(),foodprice_entry.get(),val)
    cursor.execute(updatequery,updatevalue)
    cnx.commit()
    cursor.close()
    liste.delete(0,tk.END)
    foodprice_entry.delete(0,tk.END)
    foodname_entry.delete(0,tk.END)
    menuCreateFrame.tkraise()

def givePermission():
    cursor = cnx.cursor(buffered=True)

    selectID = ("SELECT ID "
            "FROM customer "
            "WHERE email = %s")

    emvalue=(restaurant_login_entry_username.get(),)
    cursor.execute(selectID,emvalue)
    result2 = cursor.fetchone()

    selectID = ("SELECT ID "
            "FROM manager "
            "ORDER BY ID desc")

    cursor.execute(selectID)
    result = cursor.fetchone()

    controlID = ("SELECT ID "
                "FROM restaurant "
                "Where RestaurantAdress = %s and RestaurantName = %s")
    temp1 = (restaurant_login_address_entry.get(),restaurant_login_name_entry.get(),)
    cursor.execute(controlID,temp1)    
    controlpassword = cursor.fetchone()

    if(result == None):
        customerID =1
    else:
        customerID = result[0] +1

    print(customerID)
    print(controlpassword[0])
    print(restaurant_login_entry_username.get())

    permissionquery=("INSERT INTO manager "
                     "VALUES (%s,%s,%s,%s) ")
    permvalues =(customerID,controlpassword[0],restaurant_login_entry_username.get(),result2[0],)

    cursor.execute(permissionquery,permvalues)
    cnx.commit()
    cursor.close()

def showRestaurants():
    cursor = cnx.cursor(buffered=True)
    ressta = ("SELECT RestaurantName FROM restaurant")
    cursor.execute(ressta)
    global allrest
    allrest = cursor.fetchall()
    cursor.close()
    wroteresitems()
    restaurantmenuFrame.tkraise()


def showrestaurantitems():
    cursor = cnx.cursor(buffered=True)
    

    resIDsql =("SELECT ID from restaurant where RestaurantName = %s")
    resIDmenu = (valres,) 
    cursor.execute(resIDsql,resIDmenu)
    temp = cursor.fetchone()
    global resIDForMenu
    resIDForMenu=temp

    resmenusta = ("SELECT foodName FROM item WHERE resID = %s")
    menu =(resIDForMenu,)
    cursor.execute(resmenusta,resIDForMenu)
    global allrestmenu
    allrestmenu = cursor.fetchall()


    wroterestaurantitems()
    resmenuframe.tkraise()

def selectitem():
    cursor = cnx.cursor(buffered=True)
    resIDsql =("SELECT foodPrice from item where foodName= %s")
    resIDmenu = (itemval,) 
    cursor.execute(resIDsql,resIDmenu)
    temp = cursor.fetchone()
    global oneitemprice
    oneitemprice=temp

shoppingcart=[]
def addCart():
    if(currentamount.get()==""):
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="please type INTEGER Amount."
        )
        return None
    lastval= [itemval,oneitemprice[0],currentamount.get()]
    added = False
    for i in range(0,len(shoppingcart)):
        if(shoppingcart[i][0]==lastval[0]):
            shoppingcart[i][2] = int(shoppingcart[i][2]) +int(lastval[2])
            added =True
    if(added ==False):
        shoppingcart.append(lastval)
    print(shoppingcart)

def goCart():
    wrotecartitems()
    shoppingcartFrame.tkraise()

def deleteItemFromCart():
    for i in range(len(shoppingcart)):
        if(cartitemval == shoppingcart[i][0]):
            shoppingcart.pop(i) 
            customermenuFrame.tkraise()  

def giveOrder():
    cursor = cnx.cursor(buffered=True)
    itemid =[]
    if(len(shoppingcart)==0):
        mesaj = messagebox.showinfo(
        title="Bilgi",
        message="add items to cart."
        )
        customermenuFrame.tkraise()
        return None
    getitemid = ("select ID from item where foodName = %s")
    for i in range(len(shoppingcart)):
        itemidval = (shoppingcart[i][0],)
        cursor.execute(getitemid,itemidval)
        tempid = cursor.fetchone()
        itemid.append(tempid[0])

    print(itemid)

    selectID = ("SELECT orderItemID "
            "FROM orderItems "
            "ORDER BY orderItemID desc")

    cursor.execute(selectID)
    result1 = cursor.fetchone()

    if(result1 == None):
        orderItemID =1
    else:
        orderItemID = result1[0] +1

    selectID = ("SELECT orderID "
            "FROM orders "
            "ORDER BY orderID desc")

    cursor.execute(selectID)
    result = cursor.fetchone()

    if(result == None):
        orderID =1
    else:
        orderID = result[0] +1

    time= datetime.now()

    insertOrder = ("INSERT INTO orders VALUES (%s,%s,%s)")
    insvalues = (orderID,time,customerID)
    cursor.execute(insertOrder,insvalues)
    cnx.commit()

    insertItems = ("INSERT INTO orderItems VALUES (%s,%s,%s,%s)")
    for i in range(len(shoppingcart)):
        itemorderval = (orderItemID,orderID,itemid[i],shoppingcart[i][2])
        cursor.execute(insertItems,itemorderval)
        cnx.commit()
        orderItemID +=1
    shoppingcart.clear()
    customermenuFrame.tkraise()
    mesaj = messagebox.showinfo(
        title="Bilgi",
        message="order sucsessfully created."
        )

def restaurantorders():
    cursor = cnx.cursor(buffered=True)
    selecsta =("select  orders.orderID, item.foodName, orderItems.quantity, customer.email "
                "from restaurant "
                "inner join item on restaurant.ID = item.resID "
                "inner join orderitems on item.ID = orderitems.itemID "
                "inner join orders on orders.orderID = orderitems.orderID "
                "inner join customer on orders.customerID =customer.ID "
                "where restaurant.ID = %s "
                "order by orders.orderID ")
    restname =(resID,)
    cursor.execute(selecsta,restname)
    global restvalues
    restvalues =cursor.fetchall()
    print(restvalues)

    countsta =("select  count(distinct(orders.orderID)) "
                "from restaurant "
                "inner join item on restaurant.ID = item.resID "
                "inner join orderitems on item.ID = orderitems.itemID "
                "inner join orders on orders.orderID = orderitems.orderID "
                "inner join customer on orders.customerID =customer.ID "
                "where restaurant.ID = %s "
                "order by orders.orderID ")
    restname =(resID,)
    cursor.execute(countsta,restname)
    global ordercount
    ordercount =cursor.fetchone()



    cursor.close()
    wroteresrepitems()
    restaurantreportFrame.tkraise()

def showreport():
    tempval=restvalues[0][0]
    templist =[[]]
    tempcount=0
    for i in range(len(restvalues)):
        if tempval == restvalues[i][0]:
            templist[tempcount].append(restvalues[i])
        else:
            tempcount += 1
            templist.append([restvalues[i]])
            tempval = restvalues[i][0]
    print(templist)
        
    global tempitemname
    tempitemname =[]
    global tempitemamount
    tempitemamount = []
    global tempname
    tempname=""

    
    for s in range(len(templist[valresasdfa])):
        tempitemname.append(templist[valresasdfa][s][1])
        tempitemamount.append(templist[valresasdfa][s][2])
        tempname = templist[valresasdfa][s][3]

    print(tempitemamount)
    print(tempitemname)
    print(tempname)

    wrotereport()
    repframe.tkraise()

def clearas():
    shoppingcart.clear()
    loginFrame.tkraise()








#start page
startFrame = tk.Frame(
    pencere,
    width=600,
    height=500,
    bg="gray"
)
startFrame.grid(row=0,column=0)

registerButton = tk.Button(
    startFrame,
    text="Register",
    height=2,
    width=20,
    cursor="hand2",
    command= lambda: registerFrame.tkraise()
)

loginButton = tk.Button(
    startFrame,
    text="Login",
    height=2,
    width=20,
    cursor="hand2",
    command= lambda: loginFrame.tkraise()
)


registerButton.place(relx=0.37,rely=0.30)
loginButton.place(relx=0.37,rely=0.60)







#register page
registerFrame = tk.Frame(
    pencere,
    width=600,
    height=500,
    bg="gray"
)
registerFrame.grid(row=0,column=0)

label_customer_name = tk.Label(registerFrame, text="name")
label_customer_surname = tk.Label(registerFrame, text="surname")
label_customer_address =tk.Label(registerFrame, text="address")
label_customer_email = tk.Label(registerFrame, text="email:")
label_customer_password = tk.Label(registerFrame, text="Password:")

register_entry_name = tk.Entry(registerFrame)
register_entry_surname = tk.Entry(registerFrame)
register_entry_address = tk.Entry(registerFrame)
register_entry_email = tk.Entry(registerFrame)
register_entry_password = tk.Entry(registerFrame, show="*")  # Use show="*" to hide password characters

register_button = tk.Button(
    registerFrame, 
    text="Register", 
    command= register 
    )
back_register_button = tk.Button(
    registerFrame, 
    text="back", 
    command= lambda: startFrame.tkraise()
    )
back_register_button.place(x=300,y=450)

label_customer_name.place(x=100, y=150)
label_customer_surname.place(x=100,y=200)
label_customer_address.place(x=100,y=250)
label_customer_email.place(x=100, y=300)
label_customer_password.place(x=100, y=350)
register_entry_name.place(x=250,y=150)
register_entry_surname.place(x=250,y=200)
register_entry_address.place(x=250,y=250)
register_entry_email.place(x=250, y=300)
register_entry_password.place(x=250, y=350)
register_button.place(x=300, y=400)






#admin give permission page
restaurantLoginFrame = tk.Frame(
    pencere,
    width=600,
    height=500,
    bg="gray"
)
restaurantLoginFrame.grid(row=0,column=0)

label_username = tk.Label(restaurantLoginFrame, text="email:")
restaurant_name = tk.Label(restaurantLoginFrame, text="Restaurant Name")
restaurant_address = tk.Label(restaurantLoginFrame,text="Restaurant Address")

restaurant_login_entry_username = tk.Entry(restaurantLoginFrame)
restaurant_login_name_entry = tk.Entry(restaurantLoginFrame) 
restaurant_login_address_entry = tk.Entry(restaurantLoginFrame) 

login_button = tk.Button(
    restaurantLoginFrame, 
    text="Give Permission", 
    command= givePermission
    )
back_permission_button = tk.Button(
    restaurantLoginFrame, 
    text="back", 
    command= lambda: adminFrame.tkraise()
    )
back_permission_button.place(x=300,y=450)
label_username.place(x=100, y=150)
restaurant_login_entry_username.place(x=250, y=150)
login_button.place(x=300, y=300)
restaurant_name.place(x=100, y=200)
restaurant_address.place(x=100, y=250)
restaurant_login_name_entry.place(x=250, y=200)
restaurant_login_address_entry.place(x=250, y=250)






#login page
loginFrame = tk.Frame(
    pencere,
    width=600,
    height=500,
    bg="gray"
)
loginFrame.grid(row=0,column=0)

login_label_username = tk.Label(loginFrame, text="email:")
login_label_password = tk.Label(loginFrame, text="Password:")

adminlogin_label_username = tk.Label(loginFrame, text="admin email: admin")
adminlogin_label_password = tk.Label(loginFrame, text="admin Password:1234")

login_entry_username = tk.Entry(loginFrame)
login_entry_password = tk.Entry(loginFrame, show="*")  # Use show="*" to hide password characters

customer_login_button = tk.Button(
    loginFrame,
    text="customer login", 
    command= customerLogin 
)

admin_login_button = tk.Button(
    loginFrame,
    text="admin login", 
    command= adminLogin
)
restaurant_login_button = tk.Button(
    loginFrame,
    text="restaurant login", 
    command= restaurantLogin
)
back_login_button = tk.Button(
    loginFrame, 
    text="back", 
    command= lambda: startFrame.tkraise()
    )
back_login_button.place(x=300,y=450)
login_label_username.place(x=100, y=150)
login_entry_username.place(x=250, y=150)
login_label_password.place(x=100, y=200)
login_entry_password.place(x=250, y=200)
customer_login_button.place(x=250, y=250)
admin_login_button.place(x=350,y=250)
restaurant_login_button.place(x=450,y=250)
adminlogin_label_username.place(x=10, y=30)
adminlogin_label_password.place(x=10, y=50)





#for menu create page
menuCreateFrame =tk.Frame(
    pencere,
    width=600,
    height=500,
    bg="gray"
)
menuCreateFrame.grid(row=0,column=0)
add_item_button = tk.Button(
    menuCreateFrame,
    text="add item", 
    height=2,
    width=20,
    command= lambda: addItemFrame.tkraise()
)
current_items_button = tk.Button(
    menuCreateFrame,
    text="current items", 
    height=2,
    width=20,
    command= currentItems
)
restaurantorders_button = tk.Button(
    menuCreateFrame,
    text="all orders", 
    height=2,
    width=20,
    command= restaurantorders
)

back_menu_button = tk.Button(
    menuCreateFrame, 
    text="back", 
    command= lambda: loginFrame.tkraise()
    )
back_menu_button.place(x=300,y=450)

add_item_button.place(relx=0.37,rely=0.3)
current_items_button.place(relx=0.37,rely=0.5)
restaurantorders_button.place(relx=0.37,rely=0.7)





#add item page
addItemFrame = tk.Frame(
    pencere,
    width=600,
    height=500,
    bg="gray"
)
addItemFrame.grid(row=0,column=0)

item_name_label = tk.Label(addItemFrame, text="item name")
item_price_label = tk.Label(addItemFrame, text="item price")

item_name_entry = tk.Entry(addItemFrame)
item_price_entry = tk.Entry(addItemFrame)  

addItem_button = tk.Button(
    addItemFrame,
    text="add item", 
    command= addItem 
)
back_additem_button = tk.Button(
    addItemFrame, 
    text="back", 
    command= lambda: menuCreateFrame.tkraise()
    )
back_additem_button.place(x=300,y=450)

item_name_label.place(x=100, y=150)
item_name_entry.place(x=250, y=150)
item_price_label.place(x=100, y=200)
item_price_entry.place(x=250, y=200)
addItem_button.place(x=250,y=250)






#admin  page
adminFrame = tk.Frame(
    pencere,
    width=600,
    height=500,
    bg="gray"
)
adminFrame.grid(row=0,column=0)

res_name_label = tk.Label(adminFrame, text="restaurant name")
res_address_label = tk.Label(adminFrame, text="restaurant address")

restaurant_name_entry = tk.Entry(adminFrame)
restaurant_address_entry = tk.Entry(adminFrame)

add_restaurant_button = tk.Button(
    adminFrame, 
    text="add restaurant", 
    command= addRestaurant 
    )
delete_restaurant_button = tk.Button(
    adminFrame, 
    text="delete restaurant", 
    command= deleteRestaurant
    )
givepermission_button = tk.Button(
    adminFrame, 
    text="give manager permission", 
    command=lambda: restaurantLoginFrame.tkraise()
    )
back_admin_button = tk.Button(
    adminFrame, 
    text="back", 
    command= lambda: loginFrame.tkraise()
    )
back_admin_button.place(x=300,y=450)

res_name_label.place(x=100, y=150)
res_address_label.place(x=100, y=200)
restaurant_name_entry.place(x=250, y=150)
restaurant_address_entry.place(x=250, y=200)
add_restaurant_button.place(x=200, y=300)
delete_restaurant_button.place(x=300, y=300)
givepermission_button.place(x=400,y=300)

#get report page
reportFrame = tk.Frame(
        pencere,
        width=600,
        height=500,
        bg="gray"
    )
reportFrame.grid(row=0,column=0)





#current item page
root = tk.Frame(pencere,
                width=600,
                height=500,
                bg="gray")
root.grid(row=0,column=0)


bilesenler = ttk.Notebook(
    root,
    width=550,
    height=400
)
bilesenler.place(x = 25, y = 25)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)


bilesenler.add(
    bilesen2,
    text="current items"
)

scrollbar = tk.Scrollbar(bilesen2)
scrollbar.pack( side ="left", fill="y" )

liste = tk.Listbox(bilesen2, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set,height=22)
foodname_label = tk.Label(
            bilesen2,
            text="food name:"
            )
foodname_label.place(x=200,y=100)

foodprice_label = tk.Label(
        bilesen2,
        text="food price:"
        )
foodprice_label.place(x=200,y=150)

foodname_entry = tk.Entry(bilesen2)
foodprice_entry = tk.Entry(bilesen2)
foodname_entry.place(x=300,y=100)

foodprice_entry.place(x=300,y=150)

remove_item_button=tk.Button(bilesen2,
                            text="delete item",
                            command=deleteItem
                            )
remove_item_button.place(x=300,y=200)
update_item_button=tk.Button(bilesen2,
                            text="update item",
                            command=updateItem
                            )
update_item_button.place(x=400,y=200)

currentfoodname_labelasa = tk.Label(
    bilesen2,
    text="food name: "
    )
currentfoodname_labelasa.place(x=200,y=40)
currentfoodprice_labelasa = tk.Label(
    bilesen2,
    text="food price: "
    )
currentfoodprice_labelasa.place(x=400,y=40)

currentguide_label = tk.Label(
    bilesen2,
    text="To update or delete item first select."
    )
currentguide_label.place(x=170,y=300)
currentguide_label2 = tk.Label(
    bilesen2,
    text="To update first select, then type name and price"
    )
currentguide_label2.place(x=170,y=320)

def wroteitems():
    for i in range(countitem[0]):
        liste.insert(i, "{}".format(names[i][0]))

    liste.place(x=30, y=5)
def currentitem31():  
    global liste_indeks
    liste_indeks = liste.curselection()
    print(liste_indeks[0])
    for l in liste_indeks:
        print(l)
        print(liste.get(l))
        global val
        val = liste.get(l)
    
    currentfoodname_labelasa.config(text="food name: {}".format(val))
    currentfoodprice_labelasa.config(text="food price: {}".format(prices[liste_indeks[0]][0]))
scrollbar.config( command = liste.yview)

def clear():
    liste.delete(0,tk.END)
    menuCreateFrame.tkraise()

selectbuton = tk.Button(
        bilesen2,
        text="Seç",
        command=currentitem31
    )
selectbuton.place(x=75, y=370)
back_currentitem_button = tk.Button(
    root, 
    text="back", 
    command= clear
    )
back_currentitem_button.place(x=300,y=450)





#customer menü page

customermenuFrame = tk.Frame(pencere,
                width=600,
                height=500,
                bg="gray")
customermenuFrame.grid(row=0,column=0)


shopping_cart_button = tk.Button(
    customermenuFrame,
    height=2,
    width=20,
    text="shopping cart", 
    command= goCart
)

restaurant_choose_button = tk.Button(
    customermenuFrame,
    height=2,
    width=20,
    text="restaurants", 
    command= showRestaurants
)

shopping_cart_button.place(relx=0.37,rely=0.30)
restaurant_choose_button.place(relx=0.37,rely=0.60)

back_currentitemas_button = tk.Button(
    customermenuFrame, 
    text="back", 
    command= clearas
    )
back_currentitemas_button.place(x=300,y=450)














#restaurants page
restaurantmenuFrame = tk.Frame(pencere,
                width=600,
                height=500,
                bg="gray")
restaurantmenuFrame.grid(row=0,column=0)



bilesenler = ttk.Notebook(
    restaurantmenuFrame,
    width=550,
    height=400
)
bilesenler.place(x = 25, y = 25)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)


bilesenler.add(
    bilesen2,
    text="restaurants"
)

scrollbar = tk.Scrollbar(bilesen2)
scrollbar.pack( side ="left", fill="y" )

liste2 = tk.Listbox(bilesen2, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set,height=22)



currentguide_label = tk.Label(
    bilesen2,
    text="select a restaurant"
    )
currentguide_label.place(x=170,y=300)


def wroteresitems():
    liste2.delete(0,tk.END)
    for i in range(len(allrest)):
        liste2.insert(i, "{}".format(allrest[i][0]))

    liste2.place(x=30, y=5)
def restaurantsh():  
    global restaurant_indeks
    restaurant_indeks = liste2.curselection()
    print(restaurant_indeks[0])
    for l in restaurant_indeks:
        print(l)
        print(liste2.get(l))
        global valres
        valres = liste2.get(l)
    showrestaurantitems()
scrollbar.config( command = liste2.yview)

def clear2():
    liste2.delete(0,tk.END)
    customermenuFrame.tkraise()

selectbuton = tk.Button(
        bilesen2,
        text="Seç",
        command=restaurantsh
    )
selectbuton.place(x=75, y=370)
back_currentitem_button = tk.Button(
    restaurantmenuFrame, 
    text="back", 
    command= clear2
    )
back_currentitem_button.place(x=300,y=450)




#res menü page

resmenuframe = tk.Frame(pencere,
                width=600,
                height=500,
                bg="gray")
resmenuframe.grid(row=0,column=0)


bilesenler = ttk.Notebook(
    resmenuframe,
    width=550,
    height=400
)
bilesenler.place(x = 25, y = 25)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)


bilesenler.add(
    bilesen2,
    text="menü"
)

scrollbar = tk.Scrollbar(bilesen2)
scrollbar.pack( side ="left", fill="y" )

liste3 = tk.Listbox(bilesen2, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set,height=22)
foodname_label = tk.Label(
            bilesen2,
            text="write amount :"
            )
foodname_label.place(x=200,y=100)



addcart_button=tk.Button(bilesen2,
                            text="add cart",
                            command=addCart
                            )
addcart_button.place(x=300,y=200)

currentfoodname_labelas = tk.Label(
    bilesen2,
    text="food name: "
    )
currentfoodname_labelas.place(x=200,y=40)

currentamount = tk.Entry(resmenuframe)
currentamount.place(x = 330,y=150)


currentfoodprice_labelas = tk.Label(
    bilesen2,
    text="food price: "
    )
currentfoodprice_labelas.place(x=400,y=40)

currentguide_label = tk.Label(
    bilesen2,
    text="To add cart item first select."
    )
currentguide_label.place(x=170,y=300)
currentguide_label2 = tk.Label(
    bilesen2,
    text="Then type amount (INTEGER)"
    )
currentguide_label2.place(x=170,y=320)






def wroterestaurantitems():
    for i in range(len(allrestmenu)):
        liste3.insert(i, "{}".format(allrestmenu[i][0]))

    liste3.place(x=30, y=5)
def currentitem():  
    global liste3_indeks
    liste3_indeks = liste3.curselection()
    print(liste3_indeks[0])
    for l in liste3_indeks:
        print(l)
        print(liste3.get(l))
        global itemval
        itemval = liste3.get(l)
    selectitem()
    currentfoodname_labelas.config(text="food name: {}".format(itemval))
    currentfoodprice_labelas.config(text="food price: {}".format(oneitemprice[0]))
scrollbar.config( command = liste3.yview)

def clear3():
    liste3.delete(0,tk.END)
    restaurantmenuFrame.tkraise()

selectbuton = tk.Button(
        bilesen2,
        text="Seç",
        command=currentitem
    )
selectbuton.place(x=75, y=370)
back_currentitem_button = tk.Button(
    resmenuframe, 
    text="back", 
    command= clear3
    )
back_currentitem_button.place(x=300,y=450)





#shopping cart 

shoppingcartFrame = tk.Frame(pencere,
                width=600,
                height=500,
                bg="gray")
shoppingcartFrame.grid(row=0,column=0)



bilesenler = ttk.Notebook(
    shoppingcartFrame,
    width=550,
    height=400
)
bilesenler.place(x = 25, y = 25)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)


bilesenler.add(
    bilesen2,
    text="shopping cart"
)

scrollbar = tk.Scrollbar(bilesen2)
scrollbar.pack( side ="left", fill="y" )

liste5 = tk.Listbox(bilesen2, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set,height=22)

shoppingcartitemname = tk.Label(shoppingcartFrame,
                                text="item name: ")
shoppingcartitemname.place(x=200,y=100)
shoppingcartitemprice = tk.Label(shoppingcartFrame,
                                text="item price: ")
shoppingcartitemprice.place(x=400,y=100)
shoppingcartitemamount = tk.Label(shoppingcartFrame,
                                text="item amount: ")
shoppingcartitemamount.place(x=200,y=200)
shoppingcartitemtotalprice = tk.Label(shoppingcartFrame,
                                text="total price: ")
shoppingcartitemtotalprice.place(x=400,y=200)

deleteItem_button = tk.Button(
    shoppingcartFrame, 
    text="remove item from cart", 
    command= deleteItemFromCart
    )
deleteItem_button.place(x=250,y=300)

order_button = tk.Button(
    shoppingcartFrame, 
    text="give order", 
    command= giveOrder
    )
order_button.place(x=400,y=300)

currentguide_label = tk.Label(
    bilesen2,
    text=""
    )
currentguide_label.place(x=170,y=300)


def wrotecartitems():
    liste5.delete(0,tk.END)
    for i in range(len(shoppingcart)):
        liste5.insert(i, "{}".format(shoppingcart[i][0]))

    liste5.place(x=30, y=5)
def shoppingcartselect():  
    global cart_indeks
    cart_indeks = liste5.curselection()
    print(cart_indeks[0])
    for l in cart_indeks:
        print(l)
        print(liste5.get(l))
        global cartitemval
        cartitemval = liste5.get(l)
    tempprice=0
    tempamount =0
    for i in range(len(shoppingcart)):
        if(cartitemval == shoppingcart[i][0]):
            tempprice =shoppingcart[i][1]
            tempamount = shoppingcart[i][2]
    totalprice=int(tempamount)*int(tempprice)
    shoppingcartitemname.config(text="item name : {}".format(cartitemval))
    shoppingcartitemamount.config(text="total amount : {}".format(tempamount))
    shoppingcartitemprice.config(text="item price : {}".format(tempprice))
    shoppingcartitemtotalprice.config(text="total price : {}".format(totalprice))
scrollbar.config( command = liste5.yview)

def clear4():
    customermenuFrame.tkraise()

selectbuton = tk.Button(
        bilesen2,
        text="Seç",
        command=shoppingcartselect
    )
selectbuton.place(x=75, y=370)
back_currentitem_button = tk.Button(
    shoppingcartFrame, 
    text="back", 
    command= clear4
    )
back_currentitem_button.place(x=300,y=450)




#restaurant report page
restaurantreportFrame = tk.Frame(pencere,
                width=600,
                height=500,
                bg="gray")
restaurantreportFrame.grid(row=0,column=0)



bilesenler = ttk.Notebook(
    restaurantreportFrame,
    width=550,
    height=400
)
bilesenler.place(x = 25, y = 25)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)


bilesenler.add(
    bilesen2,
    text="all reports"
)

scrollbar = tk.Scrollbar(bilesen2)
scrollbar.pack( side ="left", fill="y" )

liste31 = tk.Listbox(bilesen2, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set,height=22)



currentguide_label = tk.Label(
    bilesen2,
    text="select a order"
    )
currentguide_label.place(x=170,y=300)


def wroteresrepitems():
    liste31.delete(0,tk.END)
    for i in range(ordercount[0]):
        liste31.insert(i, "order {}".format(i+1))

    liste31.place(x=30, y=5)
def restaurantrepsh():  
    global restaurantrep_indeks
    restaurantrep_indeks = liste31.curselection()
    print(restaurantrep_indeks[0])
    for l in restaurantrep_indeks:
        print(l)
        print(liste31.get(l))
        global valresasdfa
        valresasdfa = l
    showreport()
scrollbar.config( command = liste31.yview)

def clear31():
    liste31.delete(0,tk.END)
    menuCreateFrame.tkraise()

selectbuton = tk.Button(
        bilesen2,
        text="Seç",
        command=restaurantrepsh
    )
selectbuton.place(x=75, y=370)
back_currentitemass_button = tk.Button(
    restaurantreportFrame, 
    text="back", 
    command= clear31
    )
back_currentitemass_button.place(x=300,y=450)




#rep page
repframe = tk.Frame(pencere,
                width=600,
                height=500,
                bg="gray")
repframe.grid(row=0,column=0)


bilesenler = ttk.Notebook(
    repframe,
    width=550,
    height=400
)
bilesenler.place(x = 25, y = 25)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)


bilesenler.add(
    bilesen2,
    text="order report"
)

scrollbar = tk.Scrollbar(bilesen2)
scrollbar.pack( side ="left", fill="y" )

liste32 = tk.Listbox(bilesen2, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set,height=22)
foodname_label = tk.Label(
            bilesen2,
            text="ordered by : "
            )
foodname_label.place(x=200,y=100)


currentorder_label = tk.Label(
    bilesen2,
    text="order : "
    )
currentorder_label.place(x=200,y=20)

currentfoodname_label = tk.Label(
    bilesen2,
    text="food name: "
    )
currentfoodname_label.place(x=200,y=40)

currentamount = tk.Entry(resmenuframe)
currentamount.place(x = 330,y=150)


currentfoodprice_label = tk.Label(
    bilesen2,
    text="food price: "
    )
currentfoodprice_label.place(x=400,y=40)

currentguide_label = tk.Label(
    bilesen2,
    text="select item, from orders to see amount ."
    )
currentguide_label.place(x=170,y=300)
currentguide_label2 = tk.Label(
    bilesen2,
    
    )
currentguide_label2.place(x=170,y=320)


def wrotereport():
    for i in range(len(tempitemname)):
        liste32.insert(i, "{}".format(tempitemname[i]))

    liste32.place(x=30, y=5)
def currentitem32():  
    global liste32_indeks
    liste32_indeks = liste32.curselection()
    print(liste32_indeks[0])
    for l in liste32_indeks:
        print(l)
        print(liste32.get(l))
        global itemnumber
        itemnumber = l
    currentfoodname_label.config(text="food name: {}".format(tempitemname[itemnumber]))
    currentfoodprice_label.config(text="amount : {}".format(tempitemamount[itemnumber]))
    foodname_label.config(text="ordered by : {}".format(tempname))
    currentorder_label.config(text="order : {}".format(valresasdfa+1))
scrollbar.config( command = liste32.yview)

def clear35():
    liste32.delete(0,tk.END)
    restaurantorders()

selectbuton = tk.Button(
        bilesen2,
        text="Seç",
        command=currentitem32
    )
selectbuton.place(x=75, y=370)
back_rep_button = tk.Button(
    repframe, 
    text="back", 
    command= clear35
    )
back_rep_button.place(x=300,y=450)




giris()

pencere.mainloop()