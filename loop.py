while True:
    print("Menu:")
    print("1. Greet")
    print("2. Show IPL Team")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print("Hello, welcome to CMART SOLUTIONS!")
        case "2":
            print("Your favorite team is RCB!")
        case "3":
            print("Exiting the program. Goodbye!")
            break 
        case _:
            print("Invalid choice")
