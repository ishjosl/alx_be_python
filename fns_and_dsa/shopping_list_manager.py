# shopping_list.py

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        # Display the menu
        print("\nShopping List Menu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View the shopping list")
        print("4. Exit")

        # Prompt the user for their choice
        choice = input("Please enter your choice (1-4): ")

        if choice == '1':
            # Add an item
            item = input("Enter the name of the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            # Remove an item
            item = input("Enter the name of the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not found in your shopping list.")

        elif choice == '3':
            # View the shopping list
            if shopping_list:
                print("Current shopping list:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
