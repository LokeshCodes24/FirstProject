def load_todos(filename):
    try:
        with open(filename,"r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_todos(filename,todos):
    with open(filename,"w") as file:
        for todo in todos:
            file.write(todo + "\n")

filename="todos.txt"
todos=load_todos(filename)

while True:
    user_action=input("Type add,show,edit or exit:").strip().lower()
    match user_action:
        case 'add':
            todo=input("Enter a todo: ").strip()
            if todo:
                todos.append(todo)
                save_todos(filename,todos)

        case 'show':
            for index,item in enumerate(todos):
                row=f"{index+1}-{item}"
                print(row)        

        case 'edit':
            try:
                number=int(input("Number of the todo to edit: "))-1
                if 0<=number<len(todos):
                    new_todo=input("Enter the new todo: ").strip()
                    if new_todo:
                        todos[number]=new_todo
                        save_todos(filename,todos)              
                else:
                    print("Invalid number")
            except ValueError:
                print("Please enter a valid number.")
        case 'exit':
            break
        case _:
            print("Invalid option,please try again.")