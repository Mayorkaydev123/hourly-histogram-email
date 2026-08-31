todo_list = []
status = True

with open("list.txt","r") as file:
    for line in file:
        todo_list.append(line)
while status == True:
    print('=' * 15)
    print(" TO-DO LIST")
    print('=' * 15)
    print("1. Add item\n2. Remove item\n3. View List\n4. Exit")
    action = input("what action do you want me to perform:")
    if action == "1":
       new_entry = input(">")
       todo_list.append(new_entry)
       with open("list.txt", "a") as file:
           file.write(f"\n{new_entry}")
    elif action == "2":
        i = 1
        for item in todo_list:
            print(f"{i}. {item}")
            i += 1
        index = int(input("what item do you want me to remove:"))
        todo_list.pop(int(index) - 1)
        print(todo_list)
    elif action == "3":
        print('=' * 15)
        print(" TO-DO LIST")
        print('=' * 15)
        i = 1
        for item in todo_list:
            print(f" {i}. {item}")
            i += 1
        print('=' * 15)
    elif action == "4":
        status = False
    else:
        pass 
    with open("list.txt","w") as file:
         for line in todo_list:
            file.write(line)
