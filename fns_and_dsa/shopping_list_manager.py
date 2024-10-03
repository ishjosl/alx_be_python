def display_menu():    
    print("Shopping List Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the shopping list")
    print("4. Exit")

    shopping_list= []
    while True: 
        display_menu()   
        choice = input("Please enter your choice (1-4): ")

        if choice == '1':
            pass

        elif choice == '2':
            pass

        elif choice == '3':
            pass

        elif choice == '4':
            print("Goodbye!")
            break 

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

