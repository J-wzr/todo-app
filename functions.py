
def get_todos():
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos

def add_todos(todo_arg):
    with open("todos.txt", "w") as file:
        file.writelines(todo_arg)