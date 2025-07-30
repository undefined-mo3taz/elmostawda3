contacts=[]
def add_contact():
    name=input("enter name: ")
    phone=input("enter phone number ")
    email=input("enter email address ")
    contact=[name, phone, email]
    contacts.append(contact)
    print("added")
def view_contacts():
    if len(contacts)==0:
        print("no contacts found")
    else:
        print("all contacts:")
        i=0
        while i<len(contacts):
            print(f"name{contacts[i][0]},phone{contacts[i][1]},email{contacts[i][2]}")
            i+=1
def search_contact():
    x=input("enter the name or number to search ")
    i=0
    found=False
    while i<len(contacts):
        name=contacts[i][0]
        phone=contacts[i][1]
        if x==name or x==phone:
            print(f"name{contacts[i][0]},phone{contacts[i][1]},email{contacts[i][2]}")
            found = True
        i+=1

    if found==False:
        print("no matched contacts")
def delete_contact():
    name_2_delete=input("enter contact's name")
    i=0
    while i<len(contacts):
        if contacts[i][0]==name_2_delete:
            del contacts[i]
            print("deleted")
            return
        i+=1
def update_contact():
    update = input("enter contact's name ")
    i=0
    while i<len(contacts):
        if contacts[i][0]==update:
            print("enter the new informations")
            n_n=input("new name ")
            n_p=input("new phone ")
            n_e=input("new email ")
            if n_n != "":
                contacts[i][0] = n_n
            if n_p != "":
                contacts[i][1] = n_p
            if n_e != "":
                contacts[i][2] = n_e
            print("updated")
            return
        i+=1
def menu():
    while True:
        print("contact mangment ")
        print("1 add contact")
        print("2 view contacts")
        print("3 search")
        print("4 delete")
        print("5 update")
        print("0 exit")
        option=input("enter ur option")
        if option=="1":
            add_contact()
        elif option=="2":
            view_contacts()
        elif option=="3":
            search_contact()
        elif option=="4":
            delete_contact()
        elif option=="5":
            update_contact()
        elif option=="0":
            break
        else:
            print("mtzha2ne4 b2a y3m!!!!")
            break
menu()
