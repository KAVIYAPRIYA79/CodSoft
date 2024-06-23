contact={}

def view_contact():
    print("name\t\tcontact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    print("1.Add new contact") 
    print("2.Search contact") 
    print("3.View contact") 
    print("4.update contact") 
    print("5.Delete contact") 
    print("6.Exit")
    choice=input("enter you choice 1/2/3/4/5/6:")

    if choice == '1':
        name=input("enter the contact name:")
        phone=input("enter the mobile number:")
        contact[name]=phone

    elif choice == '2':
        search_name=input("enter the contact name to be searched:")
        if search_name in contact:
            print(f"{search_name} contact number is ",contact[search_name])
        else:
            print(f"{search_name} is not found in contact book") 

    elif choice == '3':
        if not contact:
            print("your contack book is empty")
        else:
            view_contact()

    elif choice == '4':
        update_contact=input("enter the contact name to be updated:")
        if update_contact in contact:
            new_phone=input("enter the new mobile number:")
            contact[update_contact]=new_phone
            print("contact updated successfully")
            view_contact()
        else:
            print("Name is not found in contact book") 
            
    elif choice == '5':
        delete_contact=input("enter the contact  name to be deleted:")
        if delete_contact in contact:
            confirm=input("do you want to delete this contact yes/no?:") 
            if confirm == "yes":
                contact.pop(delete_contact)
                print(f"{name} is deleted successfully")
            else:
                view_contact()  
        else:
            print(f"{name}is not found in the contact book")     

    elif choice == '6':
        print("Exiting the contact book")
        break

    else:
        print("Invalid choice. Please try again.")

