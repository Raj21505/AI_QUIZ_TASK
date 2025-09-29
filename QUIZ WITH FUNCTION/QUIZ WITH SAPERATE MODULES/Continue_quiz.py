def cont(action):
    print(f"Do you want to {action} further..? (Enter 'No' to Quit)")
    leave = input("Enter: ")
    print()
    if leave.upper() == "NO":
        print("Okay... Question list updated")
        return 0
    elif action == "add":
        from Quiz_add_que import add
        add()
    elif action == "remove":
        from Remove_quiz import remove
        remove()
    elif action == "update":
        from Update_quiz import update
        update()